# pylint: disable=no-self-use
import re
import time
from json.decoder import JSONDecodeError
import requests
from rdf.parser.abstract_parser import AbstractParser, EntityType
from rdf.parser.sparql_reader import read_sparql

WIKIDATA_ENDPOINT = 'https://query.wikidata.org/sparql'
RETRY_COUNT = 10 # How many retry attempts we'll make
RETRY_DELAY = 0.1 # Wait a tenth of a second before retrying
PERSON_ENTITY_TYPES = ["human"]
BOOK_ENTITY_TYPES = ["literary work", "novel series"]

def wikidata_sparql_query(query: str) -> dict:
    """ Makes a SPARQL query request to the Wikidata endpoint. Because it fails
        occasionally, retry up to RETRY_COUNT times, while waiting RETRY_DELAY seconds
        between retries.
    """

    for _ in range(0, RETRY_COUNT):
        try:
            params = { 'format': 'json', 'query': query }
            req = requests.get(WIKIDATA_ENDPOINT, params)
            return req.json()
        except JSONDecodeError:
            # if the request fails, it will throw a JSONDecodeError.
            # As such, catch it and wait RETRY_DELAY seconds before trying again
            print("Wikidata query failed! Retrying")
            # If we retry without waiting, it will fail nearly 100% of the time
            time.sleep(RETRY_DELAY)

    # Reached max amount of retries and still couldn't get a response, so return None
    return None

class UnsupportedEntityTypeException(Exception):
    """ Thrown by get_entity_type when there's an entity type it doesn't recognize """

class WikidataParser(AbstractParser):
    """parses wikidata sources"""

    def __init__(self, uri):
        super().__init__(uri)
        self.entity_id = self._get_wikidata_id_from_uri()
        if self.entity_id is None:
            raise Exception("Invalid Wikidata URI")

    def _get_wikidata_id_from_uri(self) -> str:
        """ Does a Regex match to get the Wikidata ID from the URI """
        return re.search('Q[0-9]+', self.uri).group(0)

    def parse(self) -> dict:
        """call this method to start parsing"""
        try:
            entity_type =  self.get_entity_type()
        except UnsupportedEntityTypeException as err:
            print(err)
            return None

        if not entity_type: # entity type is None, most likely because it failed
            return None

        if entity_type == EntityType.BOOK:
            return self.parse_book()
        if entity_type == EntityType.PERSON:
            return self.parse_person()

        return None

    def get_entity_type(self) -> str:
        """ gets the entity type """
        query = read_sparql("get_instance.sparql", self.entity_id)
        response =  wikidata_sparql_query(query)

        if not response: # Response failed, so return None
            return None

        for entry in response['results']['bindings']:
            entity_type = entry['label']['value']

            if entity_type in PERSON_ENTITY_TYPES:
                return EntityType.PERSON
            if entity_type in BOOK_ENTITY_TYPES:
                return EntityType.BOOK

        raise UnsupportedEntityTypeException("Unsupported entity type")

    def parse_person(self) -> dict:
        """ Parses a person entity type """
        query = read_sparql("get_name.sparql", self.entity_id)
        return wikidata_sparql_query(query)

    def parse_book(self) -> dict:
        """ Parses a book entity type """

        query = read_sparql("get_book.sparql", self.entity_id)
        return wikidata_sparql_query(query)

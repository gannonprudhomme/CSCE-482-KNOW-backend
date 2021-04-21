# pylint: disable=no-self-use
import re
import time
from json.decoder import JSONDecodeError
import requests
from rdf.parser.abstract_parser import AbstractParser, EntityType
from rdf.parser.sparql_reader import read_sparql
from rdf.parser.wikidata_formatter import (
    format_landmark, format_country, format_book, format_person
)

WIKIDATA_ENDPOINT = 'https://query.wikidata.org/sparql'
RETRY_COUNT = 10 # How many retry attempts we'll make
RETRY_DELAY = 0.1 # Wait a tenth of a second before retrying
PERSON_ENTITY_TYPES = ["human"]
BOOK_ENTITY_TYPES = [
    "literary work",
    "novel series",
    "written work",
    "book series",
    "poem",
]
COUNTRY_TYPES = ["country", "sovereign state"]
LANDMARK_TYPES = ["landmark", "tourist attraction"]

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

    def parse(self) -> dict: # pylint: disable=too-many-return-statements
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
        if entity_type == EntityType.COUNTRY:
            return self.parse_country()
        if entity_type == EntityType.LANDMARK:
            return self.parse_landmark()

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
            if entity_type in COUNTRY_TYPES:
                return EntityType.COUNTRY
            if entity_type in LANDMARK_TYPES:
                return EntityType.LANDMARK

        raise UnsupportedEntityTypeException("Unsupported entity type")

    def parse_person(self) -> dict:
        """ Parses a person entity type """
        query = read_sparql("get_person.sparql", self.entity_id)
        response = wikidata_sparql_query(query)
        return format_person(response)

    def parse_book(self) -> dict:
        """ Parses a book entity type """

        query = read_sparql("get_book.sparql", self.entity_id)
        response = wikidata_sparql_query(query)
        return format_book(response)
    def parse_country(self) -> dict:
        """ Parse a country entity type
            Examples:
                - France: https://www.wikidata.org/wiki/Q142
                - United States: https://www.wikidata.org/wiki/Q30
                - Ghana: https://www.wikidata.org/wiki/Q117
        """
        query = read_sparql("get_country.sparql", self.entity_id)
        response = wikidata_sparql_query(query)

        return format_country(response)
        # return response

    def parse_landmark(self) -> dict:
        """ Parse a landmark entity type
            Examples:
                - Great Pyramid of Giza: https://www.wikidata.org/wiki/Q37200
                - Lincoln Memorial: https://www.wikidata.org/wiki/Q213559
                - Mount Rushmore: https://www.wikidata.org/wiki/Q83497
                - Eiffel Tower: https://www.wikidata.org/wiki/Q243
                - Table Mountain: https://www.wikidata.org/wiki/Q213360
        """
        query = read_sparql("get_landmark.sparql", self.entity_id)
        response =  wikidata_sparql_query(query)

        # Format the query
        return format_landmark(response)

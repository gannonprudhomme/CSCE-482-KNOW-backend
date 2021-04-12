# pylint: disable=no-self-use,unused-import,
import re
from qwikidata.sparql import return_sparql_query_results
from rdf.parser.abstract_parser import AbstractParser, EntityType
from rdf.parser.sparql_reader import read_sparql
class WikidataParser(AbstractParser):
    """parses wikidata sources"""

    def __init__(self, uri):
        super().__init__(uri)
        self.entity_id = re.search('Q[0-9]+', self.uri).group(0)
        if self.entity_id is None:
            raise Exception("Invalid Wikidata URI")

    def parse(self) -> dict:
        """call this method to start parsing"""
        entity_type =  self.get_entity_type()
        if entity_type == EntityType.BOOK:
            return self.parse_book()
        if entity_type == EntityType.PERSON:
            return self.parse_person()
        raise Exception("Unsupported entity type!") # pylint: disable=inconsistent-return-statements
    def get_entity_type(self) -> str:
        "gets the entity type"
        query = read_sparql("get_instance.sparql", self.entity_id)
        response =  return_sparql_query_results(query)
        for i in response['results']['bindings']:
            if i['label']['value'] == 'human':
                return EntityType.PERSON
            if i['label']['value'] == 'literary work' or i == 'novel series':
                return EntityType.BOOK
        return None

    def parse_person(self) -> dict:
        """ Parses a person entity type """
        query = read_sparql("get_name.sparql", self.entity_id)
        response = return_sparql_query_results(query)
        return response

    def parse_book(self) -> dict:
        """ Parses a book entity type """
        query = read_sparql("get_book.sparql", self.entity_id)
        response = return_sparql_query_results(query)
        return response

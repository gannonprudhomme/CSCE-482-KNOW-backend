# pylint: disable=no-self-use,unused-import
import re
from abstract_parser import AbstractParser, EntityType
class ViafParser(AbstractParser):
    """parses viaf sources"""

    def __init__(self, uri: str):
        super().__init__(uri)
        self.entity_id = re.search('[0-9]+', self.uri)
        if self.entity_id is None:
            raise Exception("Invalid VIAF URI")
        self.rdf_uri = "placeholder"
        # need to construct rdf_uri from uri

    def parse(self) -> dict:
        """call this method to start parsing"""
        return dict()

    def get_entity_type(self) -> str:
        """returns appropriate entity type as string"""
        return ""

    def parse_person(self) -> dict:
        """ Parses a person entity type """
        return dict()

    def parse_work_of_art(self) -> dict:
        """ Parses a work of art entity type """
        return dict()

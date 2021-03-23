
from abstract_parser import AbstractParser

class WikidataParser(AbstractParser):
    """parses wikidata sources"""

    def __init__(self, entity_id):
        self.entity_id = entity_id

    def parse(self) -> dict:
        """call this method to start parsing"""
        entity_type = self.get_entity_type()
        #TODO call correct parsing function based on entity type
        return dict()
    def get_entity_type(self) -> str:
        """returns appropriate entity type as string"""
        return ""

    def parse_person(self) -> dict:
        return dict()

    def parse_work_of_art(self) -> dict:
        return dict()

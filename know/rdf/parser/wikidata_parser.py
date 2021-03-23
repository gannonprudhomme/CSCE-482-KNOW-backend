class WikidataParser:
    """parses wikidata sources"""

    def __init__(self, entity_id):
        self.entity_id = entity_id

    def parse(self):
        """call this method to start parsing"""
        entity_type = self.get_entity_type()
        #TODO call correct parsing function based on entity type

    def get_entity_type(self):
        """returns appropriate entity type as string"""
        return "needs implementing"

    def parse_person(self):
        return "needs implementing"

    def parse_work_of_art(self):
        return "needs implementing"
        
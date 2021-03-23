class ViafParser:
    """parses viaf sources"""

    def __init__(self, rdf_uri):
        self.rdf_uri = rdf_uri

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
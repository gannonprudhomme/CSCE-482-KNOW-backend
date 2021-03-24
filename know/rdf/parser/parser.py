import re
from .wikidata_parser import WikidataParser
from .viaf_parser import ViafParser
class Parser:
    """parses all sources"""

    def __init__(self, uri):
        self.uri = uri

    def parse(self):
        """Checks which resource uri came from.
            Depending on the source creates appropriate parser and parses.
        """
        entity_id = self.valid_wikidata()
        rdf_uri = self.valid_viaf()
        if entity_id:
            wiki_parser = WikidataParser(entity_id)
            return wiki_parser.parse()
        if rdf_uri:
            viaf_parser = ViafParser(rdf_uri)
            return viaf_parser.parse()
        return 500 #arbitraty error code

    def valid_wikidata(self):
        """If the uri is a valid wikidata uri it returns the entity id.
            Otherwise returns false
        """
        entity_id = re.search('Q[0-9]+', self.uri)
        if 'wikidata' in self.uri and entity_id is not None:
            return entity_id
        return False

    def valid_viaf(self):
        """If the uri is a valid viaf uri it returns the uri for retrieving the rdf file.
            Otherwise returns false
        """
        entity_id = re.search('[0-9]+', self.uri)
        if 'viaf' in self.uri and entity_id is not None:
            #TODO construct viaf rdf file URI from entity URI
            viaf_uri = "empty for now"
            return viaf_uri
        return False

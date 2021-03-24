from .wikidata_parser import WikidataParser
from .viaf_parser import ViafParser
class Summarizer:
    """ Returns summarizing information for any source """

    def __init__(self, uri: str):
        self.uri = uri

    def summarize(self):
        """ Checks which resource uri came from.
            Depending on the source creates appropriate parser and parses.
        """
        if self.valid_wikidata():
            wiki_parser = WikidataParser(self.uri)
            return wiki_parser.parse()
        if self.valid_viaf():
            viaf_parser = ViafParser(self.uri)
            return viaf_parser.parse()
        return None

    def valid_wikidata(self):
        """ If the uri is a valid wikidata uri it returns True.
            Otherwise returns false
        """
        return 'wikidata' in self.uri

    def valid_viaf(self):
        """ If the uri is a valid viaf uri it returns True
            Otherwise returns false
        """
        return 'viaf' in self.uri

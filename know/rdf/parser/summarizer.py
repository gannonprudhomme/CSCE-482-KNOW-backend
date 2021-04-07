import re
import rdflib
from rdflib import Namespace
from rdf.parser.wikidata_parser import WikidataParser
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
            wikidata_uri = self.get_wikidata_uri()
            wiki_parser = WikidataParser(wikidata_uri)
            return wiki_parser.parse()
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

    def get_wikidata_uri(self):
        """ Parse viaf rdf file and search for a wikidata
            resource that is the 'sameAs' the given one.
        """
        graph = rdflib.Graph()
        graph.parse(self.uri)

        viaf_uri_base = "http://viaf.org/viaf/"
        entity_id = re.search('[0-9]+', self.uri).group(0)
        viaf_entity = rdflib.URIRef(viaf_uri_base + entity_id)

        schema = Namespace('http://schema.org/')
        for _, __, obj in graph.triples((viaf_entity, schema.sameAs, None)):
            if 'wikidata' in str(obj):
                return str(obj)

        raise Exception("Couldn't find associated wikidata URI!")

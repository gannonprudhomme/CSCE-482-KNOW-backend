from django.core.management.base import BaseCommand
from rdf.parser.summarizer import Summarizer

class Command(BaseCommand):
    """ Receives a URI and passes it into the Summarizer
        Execute it like python manage.py test_wikidata -u https://wikidata.org/wiki/Q23
    """

    def add_arguments(self, parser):
        """ Adds arguments to the command """
        parser.add_argument('--uri', '-u', type=str, help="input the uri to find")

    def handle(self, *_, **options):
        """ Execute the query """
        uri = options['uri']
        summarizer = Summarizer(uri)
        res = summarizer.summarize()
        print(res)
        print(f"Passed in test_wikidata query: and uri: {uri}")

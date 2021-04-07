from django.core.management.base import BaseCommand
import requests
from rdf.parser.sparql_reader import read_sparql

class Command(BaseCommand):
    """ This commmand will take the .sparql file and replace the
        $0 identifier with the desired uri and return the query string
        Execute it like python manage.py test_wikidata -q query.sparql -u Q12345
    """
    def add_arguments(self, parser):
        """ Adds arguments to the command """
        parser.add_argument('--query', '-q', type=str, help="input the .sparql file")
        parser.add_argument('--uri', '-u', type=str, help="input the uri to find")

    def handle(self, *_, **options):
        """ Execute the query """
        query = options['query']
        if not query:
            raise Exception("please pass a query")

        uri = options['uri']
        query_string = read_sparql(query,uri)
        query_params = {'format': 'json', 'query': query_string}
        query_request = requests.get('https://query.wikidata.org/sparql', query_params)
        print(query_request.json())
        print(f"Passed in test_wikidata query: {query} and uri: {uri}")

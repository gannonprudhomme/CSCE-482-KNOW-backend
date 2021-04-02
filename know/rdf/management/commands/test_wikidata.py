from django.core.management.base import BaseCommand
from rdf.parser.sparql_reader import read

class Command(BaseCommand):
    """ Sample Django command.
        Execute it like python manage.py sample -q query.sparql -u q:12345
    """
    def add_arguments(self, parser):
        """ Adds arguments to the command """
        parser.add_argument('--query', '-q', type=str, help="describe query")
        parser.add_argument('--uri', '-u', type=str, help="describe uri")

    def handle(self, *_, **options):
        """ Execute the query """
        query = options['query']
        if not query:
            raise Exception("please pass a query")

        uri = options['uri']
        read(query,uri)
        print(f"Passed in test_wikidata query: {query} and uri: {uri}")

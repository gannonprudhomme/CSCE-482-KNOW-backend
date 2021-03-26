from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Sample Django command.
        Execute it like python manage.py sample -q query.sparql -u q:12345
    """
    def add_arguments(self, parser):
        """ """
        parser.add_argument('--query', '-q', type=str, help="describe query")
        parser.add_argument('--uri', '-u', type=str, help="describe uri")

    def handle(self, *_, **options):
        """ """
        query = options['query']
        if not query:
            raise Exception("please pass a query")

        uri = options['uri']

        print(f"Passed in query: {query} and uri: {uri}")

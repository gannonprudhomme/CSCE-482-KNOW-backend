from rest_framework.decorators import api_view
from rest_framework.response import Response
from rdf.parser.summarizer import Summarizer

@api_view(['GET'])
def get_knowledge_panel_data(request):
    """ Gets the URI parameter from the request and calls summarize on Summarizer, then
        returns the Response.
        Returns Error code 400 if the URI is not provided, or if summarize returns None
    """
    uri = request.query_params.get('uri')

    if not uri:
        return Response(status=400)

    data = Summarizer(uri).summarize()
    if not data:
        return Response(status=400)

    return Response(data)

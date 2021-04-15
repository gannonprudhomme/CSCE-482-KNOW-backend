from django.urls import re_path
from rdf.views import get_knowledge_panel_data

urlpatterns = [
    re_path(r'^$', get_knowledge_panel_data)
]

import sys
import os

def read_sparql(query_file: str, entity_id: str) -> str:
    """ Reads the .sparql file and replaces $0 with the given entity ID"""
    relative_path = sys.path[0]
    path_name = os.path.join(relative_path, "rdf", "queries", "wikidata", query_file)
    query_string = ""
    query_input = open(path_name, "r")
    for line in query_input:
        if line.find("#") == -1:
            if line.find("$0") != -1:
                query_string += line.replace("$0", entity_id)
            else:
                query_string += line
    return query_string

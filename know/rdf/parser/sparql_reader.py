import sys
import os


def read(query_file, uri):
    """ Reads the .sparql file and replaces $0 with the uri """
    relative_path = sys.path[0]
    path_name = os.path.join(relative_path, "rdf", "queries", "wikidata", query_file)
    query_string = ""
    query_input = open(path_name, "r")
    for line in query_input:
        if line.find("#") == -1:
            if line.find("$0") != -1:
                query_string += line.replace("$0", uri)
            else:
                query_string += line
    print(query_string)
    return query_string

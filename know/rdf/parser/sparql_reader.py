import requests
import sys
import os

def read(queryFile, uri):
    relativePath = sys.path[0]
    pathName = os.path.join(relativePath, "rdf", "queries", "wikidata", queryFile)
    queryString = ""
    f = open(pathName, "r")
    for x in f:
        if x.find("#") == -1:
            if x.find("$0") != -1:
                queryString += x.replace("$0", "wd:" + uri)
            else:
                queryString += x
    print(queryString)
    r = requests.get('https://query.wikidata.org/sparql', params = {'format': 'json', 'query': queryString})
    print(r.json())

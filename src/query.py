import abox
import sparql
import rdflib
import re

def del_prefix(string):
    return re.findall(".*#(.*)", string)[0]

# load final.owl
file_name = "../ontologies/final.owl"
bet = abox.load_graph(file_name)

# define queries
dir = "../ontologies/sparql-final/"
queries = {
    "High probabilities" : "highProb.sql",
    "Medium probabilities" : "medProb.sql",
    "Low probabilities" : "lowProb.sql"
}

# exec queries
res = {}
for name, query in queries.items():
    res[name] = sparql.sparql_select(bet, dir+query,verbose=True)

# print result
for name, result in res.items():
    print("Result for",name,":")
    for r in result:
        
        print("\t",bet.label(r[0]),"->" , del_prefix(r[1]))

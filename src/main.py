import abox
import sparql

verbose = True
# raisonneur
import os
if verbose:
    print("Executing reasoner")
os.system("java -cp  reasoner/lib/*: reasoner/JenaApi ../ontologies/Bet.owl ../ontologies/data.owl > ../ontologies/infered.owl")

if verbose:
    print("Loading ontologie")
bet = abox.load_graph("../ontologies/infered.owl")

dir = '../ontologies/sparql-construct/'
queries = [
    'winner-looser.sql',
    'winAgainst.sql',
    'drawAgainst.sql',
    'playGameHome.sql',
    'bestRankThan.sql',
    'best10RankThan.sql',
    'betterFormThan.sql'
]

for query in queries:
    file_name = dir+query
    sparql.sparql_construct(bet,file_name,verbose=True)

dir = '../ontologies/sparql-generalization/'
generalization = [
    'c1.sql',
    'c2.sql',
    'c3.sql',
    'c4.sql'
]

for query in generalization:
    file_name = dir+query
    sparql.sparql_construct(bet,file_name,verbose=True)

output = '../ontologies/final.owl'
bet.serialize(destination=output,format="xml")


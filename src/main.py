import abox
import sparql

# raisonneur
import os
os.system("java -cp  reasoner/lib/*: reasoner/JenaApi ../ontologies/Bet.owl ../ontologies/data.owl > ../ontologies/infered.owl")

bet = abox.load_graph("../ontologies/infered.owl")

dir = '../ontologies/sparql-construct/'
queries = [
    'winner-looser.sql',
    'winAgainst.sql',
    'drawAgainst.sql',
    'playGameHome.sql',
    'bestRankThan.sql',
    'best10RankThan.sql',
    'betterFormThan.sql',
    'c1.sql',
    'c2.sql',
    'c3.sql',
    'c4.sql'
    
]

for query in queries:
    file_name = dir+query
    sparql.sparql_construct(bet,file_name,verbose=True)

output = '../ontologies/final.owl'
bet.serialize(destination=output,format="xml")


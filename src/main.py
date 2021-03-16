import abox
import sparql

bet = abox.main()
output = '../ontologies/data.owl'
bet.serialize(destination=output,format="xml")

import sys
sys.exit(0)

# raisonneur

dir = '../ontologies/sparql-construct/'
queries = [
    'winner-looser.sql',
    'winAgainst.sql', 
    'drawAgainst.sql',  
    'generalizaion.sql' 
]

for query in queries:
    file_name = dir+query
    sparql.sparql_construct(bet,file_name,verbose=True)
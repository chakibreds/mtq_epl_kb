import rdflib
from rdflib import Namespace

import readdb as db
from tbox import Team

def main():
    #bet = load_graph()
    bet = rdflib.Graph()
    ns = Namespace("http://www.semanticweb.org/massy/ontologies/2021/2/untitled-ontology-5#")
    bet.bind("bet",ns)
    
    teams, referee, games = db.get_all()

    for team in teams:
        team.to_rdf(bet,ns)

    for r in referee:
        r.to_rdf(bet, ns)

    for game in games:
        game.to_rdf(bet, ns)

    bet.serialize(destination='./bet.ttl',format="n3")

def load_graph(file_name="../ontologies/Bet.owl",format="xml"):
    g = rdflib.Graph()
    g.parse(file_name, format=format)

    return g

main()
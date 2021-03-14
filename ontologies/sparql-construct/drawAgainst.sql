PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bet: <http://www.semanticweb.org/massy/ontologies/2021/2/untitled-ontology-5#>

# This SPARQL query add winner, looser propreties to the KB

CONSTRUCT {
    ?t1 bet:drawAgainst ?t2.
}
WHERE { 
    ?t1 rdf:type bet:Team.
    ?t2 rdf:type bet:Team.
    ?game rdf:type bet:GamePlayed.

    ?game bet:teams ?t1.
    ?game bet:teams ?t2.
    FILTER(?t1 != ?t2)

    ?game bet:fullTimeHomeGoal ?h.
	?game bet:fullTimeAwayGoal ?a.
    FILTER(?h = ?a).
}
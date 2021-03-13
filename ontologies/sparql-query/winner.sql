PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bet: <http://www.semanticweb.org/massy/ontologies/2021/2/untitled-ontology-5#>

# This SPARQL query add winner, looser relation to the KB

CONSTRUCT {
    ?game bet:winner ?winner.
    ?game bet:looser ?looser.
}
WHERE { 
    ?winner rdf:type bet:Team.
	?game rdf:type bet:GamePlayed.
	{
        ?game bet:fullTimeHomeGoal ?h.
	    ?game bet:fullTimeAwayGoal ?a.
        ?game bet:homeTeam ?winner.
        ?game bet:awayTeam ?looser.
		FILTER(?h > ?a).
	}
	UNION
	{
        ?game bet:fullTimeHomeGoal ?h.
	    ?game bet:fullTimeAwayGoal ?a.
		?game bet:awayTeam ?winner.
        ?game bet:homeTeam ?looser.
		FILTER(?h < ?a).
	}
}
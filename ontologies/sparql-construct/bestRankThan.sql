PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bet: <http://www.semanticweb.org/massy/ontologies/2021/2/untitled-ontology-5#>
PREFIX op: <http://marklogic.com/optic> 

CONSTRUCT{
?t1 bet:bestRankThan ?t2.
}
WHERE{
    ?t1 rdf:type bet:Team.
    ?t2 rdf:type bet:Team.
    ?game rdf:type bet:GameUpComing.
    ?t1 bet:rank ?r1.
	?t2 bet:rank ?r2.
    FILTER(?r1< ?r2)
}

CONSTRUCT{
?t1 bet:best10RankThan ?t2.
}
WHERE{
    ?t1 rdf:type bet:Team.
    ?t2 rdf:type bet:Team.
    ?game rdf:type bet:GameUpComing.
    ?t1 bet:rank ?r1.
	?t2 bet:rank ?r2.
    BIND (?r1 + 10 AS ?rank10).
    FILTER(?rank10 < ?r2)
}
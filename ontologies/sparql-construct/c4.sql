PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bet: <http://www.semanticweb.org/massy/ontologies/2021/2/untitled-ontology-5#>

CONSTRUCT {
    ?team bet:c4 ?game.
}
WHERE { 
    ?team rdf:type bet:Team.
    ?t rdf:type bet:Team.
    ?game rdf:type bet:GameUpComing.
    
    ?team bet:betterFormThan ?t.
    
    ?game bet:teams ?t.
    ?game bet:teams ?team.
    FILTER(?t != ?team)
}
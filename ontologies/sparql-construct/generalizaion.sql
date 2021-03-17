PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX bet: <http://www.semanticweb.org/massy/ontologies/2021/2/untitled-ontology-5#>


/* c1 l'equipe joue à domicile */
CONSTRUCT{
    ?team bet:c1 ?game
}
WHERE{
    ?team rdf:type bet:Team.
    ?game rdf:type bet:GameUpComing.
    ?team bet:playGameHome ?game
}
/* c2 l'equipe à un meilleur classement que son adversaire */

CONSTRUCT {
    ?team bet:c2 ?game.
}
WHERE { 
    ?team rdf:type bet:Team.
    ?t rdf:type bet:Team.
    ?game rdf:type bet:GameUpComing.
    
    ?team bet:bestRankThan ?t.
    
    ?game bet:teams ?t.
    ?game bet:teams ?team.
    FILTER(?t != ?team)
}

CONSTRUCT {
    ?team bet:c3 ?game.
}
WHERE { 
    ?team rdf:type bet:Team.
    ?t rdf:type bet:Team.
    ?game rdf:type bet:GameUpComing.
    
    ?team bet:best10RankThan ?t.
    
    ?game bet:teams ?t.
    ?game bet:teams ?team.
    FILTER(?t != ?team)
}



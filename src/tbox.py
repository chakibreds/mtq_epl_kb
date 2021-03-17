from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import XSD

class Team:
    entity_name = ""
    label = ""
    rank = 0
    nWin = 0
    nLoose = 0
    nDraw = 0
    currentForm = None

    def __init__(self, label, rank, nWin, nLoose, nDraw, currentForm):
        self.label = str(label)
        self.entity_name = str(label.replace(" ", ""))
        if (rank < 1 or nWin < 0 or nLoose < 0 or nDraw < 0):
            raise ValueError()
        self.rank = int(rank)
        self.nWin = int(nWin)
        self.nLoose = int(nLoose)
        self.nDraw = int(nDraw)
        self.currentForm = int(currentForm)
        pass

    def get_label(self):
        return self.label

    def get_entity_name(self):
        return self.entity_name

    def to_rdf(self,ontologie, namespace):
        team = URIRef(namespace[self.entity_name])

        ontologie.add((team, RDF.type, namespace.Team))
        ontologie.add((team, RDFS.label, Literal(self.label,datatype=XSD.string)))
        
        ontologie.add((team, namespace.rank, Literal(self.rank,datatype=XSD.int)))
        ontologie.add((team, namespace.nWin, Literal(self.nWin,datatype=XSD.int)))
        ontologie.add((team, namespace.nLoose, Literal(self.nLoose,datatype=XSD.int)))
        ontologie.add((team, namespace.nDraw, Literal(self.nDraw,datatype=XSD.int)))

        if self.currentForm is not None:
            ontologie.add((team, namespace.currentForm, Literal(self.currentForm,datatype=XSD.int)))



    def to_string(self):
        return self.entity_name + " " + \
            self.label + " " + \
            str(self.rank) + " " + \
            str(self.nWin) + " " + \
            str(self.nLoose) + " " + \
            str(self.nDraw) + " " + \
            self.currentForm

class Manager:
    label =  ""
    entity_name = ""
    team = None

    def __init__(self, label, team):
        self.label = label
        self.entity_name = label.replace(" ", "")
        self.team = team

    def get_label(self):
        return self.label

    def to_rdf(self,ontologie, namespace):
        manager = URIRef(namespace[self.entity_name])

        ontologie.add((manager, RDF.type, namespace.Manager))
        ontologie.add((manager, RDFS.label, Literal(self.label,datatype=XSD.string)))

        if self.team is not None:
            ontologie.add((manager, namespace.manage, namespace[self.team.entity_name]))
        
class Referee:
    label = ""
    entity_name = ""
    homeWin = 0
    awayWin = 0
    refereeDraw = 0

    def __init__(self, label, homeWin = 0, awayWin= 0, refereeDraw= 0):
        self.label = label
        self.entity_name = label.replace(" ","")
        self.homeWin = homeWin
        self.awayWin = awayWin
        self.refereeDraw = refereeDraw

    def get_label(self):
        return self.label
    
    def get_entity_name(self):
        return self.entity_name

    def to_rdf(self,ontologie, namespace):
        referee = URIRef(namespace[self.entity_name])

        ontologie.add((referee, RDF.type, namespace.Referee))
        ontologie.add((referee, RDFS.label, Literal(self.label,datatype=XSD.string)))

        if self.homeWin:
            ontologie.add((referee, RDF.homeWin, Literal(self.homeWin,datatype=XSD.int)))
        if self.awayWin:
            ontologie.add((referee, RDF.awayWin, Literal(self.awayWin,datatype=XSD.int)))
        if self.refereeDraw:
            ontologie.add((referee, RDF.refereeDraw, Literal(self.refereeDraw,datatype=XSD.int)))

class Game:
    entity_name = ""
    dateGame = ""
    homeTeam = None
    awayTeam = None
    referee = None

    def __init__(self, dateGame, homeTeam, awayTeam, referee):
        self.dateGame = dateGame
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.referee = referee
        self.entity_name = homeTeam.get_entity_name()+"VS"+awayTeam.get_entity_name()+self.dateGame.replace("/","")

    def get_entity_name(self):
        return self.entity_name
    
    def to_rdf(self,ontologie, namespace):
        game = URIRef(namespace[self.entity_name])

        ontologie.add((game, RDF.type, namespace.Game))
        ontologie.add((game, namespace.dateGame, Literal(self.dateGame,datatype=XSD.string)))
        ontologie.add((game, namespace.homeTeam, namespace[self.homeTeam.entity_name]))
        ontologie.add((game, namespace.awayTeam, namespace[self.awayTeam.entity_name]))
        ontologie.add((game, namespace.refereedBy, namespace[self.referee.entity_name]))
        

    def to_string(self):
        return self.entity_name + " " + \
            self.dateGame + " " + \
            self.homeTeam.get_entity_name() + " " + \
            self.awayTeam.get_entity_name() + " " + \
            self.referee.get_entity_name()

class GamePlayed(Game):
    fthg = 0
    ftag = 0

    def __init__(self,dateGame, homeTeam, awayTeam, referee, fthg, ftag):
        super().__init__(dateGame, homeTeam, awayTeam, referee)
        self.fthg = int(fthg)
        self.ftag = int(ftag)

    def to_rdf(self,ontologie, namespace):
        super().to_rdf(ontologie,namespace)
        game = URIRef(namespace[self.entity_name])
        
        ontologie.add((game, RDF.type, namespace.GamePlayed))
        ontologie.add((game, namespace.fullTimeHomeGoal, Literal(self.fthg,datatype=XSD.int)))
        ontologie.add((game, namespace.fullTimeAwayGoal, Literal(self.ftag,datatype=XSD.int)))

    def to_string(self):
        return super().to_string() + " " + \
            str(self.fthg) + " " + \
            str(self.ftag)

class GameUpComing(Game):
    def to_rdf(self, ontologie, namespace): 
        super().to_rdf(ontologie,namespace)
        game = URIRef(namespace[self.entity_name])
        ontologie.add((game, RDF.type, namespace.GameUpComing))

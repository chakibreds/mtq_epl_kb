# This file define all entities used in the TBOX

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
        self.currentForm = str(currentForm)
        pass

    def get_label(self):
        return self.label

    def get_entity_name(self):
        return self.entity_name

    def to_rdf(self):
        pass

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
        self.entity_name = lable.replace(" ", "")
        self.team = team

    def get_label(self):
        return self.label

    def to_rdf(self):
        pass

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

    def to_rdf(self):
        pass

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
        self.entity_name = homeTeam.get_entity_name()+"VS"+awayTeam.get_entity_name()+self.dateGame

    def get_entity_name(self):
        return self.entity_name
    
    def to_rdf(self):
        pass

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

    def to_rdf(self):
        pass

    def to_string(self):
        return super().to_string() + " " + \
            str(self.fthg) + " " + \
            str(self.ftag)

class GameUpComing(Game):
    def to_rdf(self):
        pass


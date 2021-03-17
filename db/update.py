import pandas as pd

def main():
    url = "https://www.football-data.co.uk/mmz4281/2021/E0.csv"

    scores = pd.read_csv(url)

    scores = scores[["Date","HomeTeam", "AwayTeam", "FTHG", "FTAG","Referee"]]

    scores.to_csv("2020-21.csv")

    url = "https://www.msn.com/en-au/sport/football/epl/ladder"

    ladder = pd.read_html(url)

    ladder = ladder[0][["R", "TEAM.1","P", "W","D","L"]]
    # rename
    ladder.columns = ["rank", "team", "played", "win", "draw", "loose"]

    ladder.to_csv("actual-ranking.csv")

def get_currentForm(teamName, scores):
    scores_teams = scores[
        (scores["HomeTeam"] == teamName) |
        (scores["AwayTeam"] == teamName)
    ].copy()
    i = 0
    for index,score in scores_teams[-5:].iterrows():
        if score["FTHG"] == score["FTAG"]:
            i += 1
        elif (
                score["HomeTeam"]==teamName and 
                (score["FTHG"] > score["FTAG"]) ) or \
            (
                score["AwayTeam"]==teamName and 
                (score["FTAG"] > score["FTHG"]) 
            ):
            i += 3

    return i

#main()         

ladder = pd.read_csv("actual-ranking.csv")
scores = pd.read_csv("2020-21.csv")

form = []
for index, team in ladder.iterrows():
    form.append(get_currentForm(team["team"],scores))

ladder["currentForm"] = form

ladder.to_csv("actual-ranking.csv")
import pandas as pd

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
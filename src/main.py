from tbox import Team, Game, GameUpComing, GamePlayed, Manager, Referee
import pandas as pd
import sys

def main():
    rank_file = "../db/actual-ranking.csv"
    season_files = [
        "../db/2020-21.csv"
    ]

    df_rank = pd.read_csv(rank_file)
    df_seasons = []
    for file in season_files:
        df_seasons.append(pd.read_csv(file))
    
    teams = rank_to_teams(df_rank)

    referee = seasons_to_referee(df_seasons)

    games = seasons_to_gamePlayed(df_seasons, teams, referee)
    return 0

def seasons_to_referee(dfs):
    referee_names = []
    for df in dfs:
        referee_names = list(set(referee_names + list(df["Referee"])))
    
    referee = []
    for ref in referee_names:
        referee.append(Referee(ref))
    return referee

def seasons_to_gamePlayed(dfs, teams, referee):
    games = []
    for df in dfs:
        for index, game in df.iterrows():
            try:
                games.append(GamePlayed(
                    game["Date"],
                    next(t for t in teams if game["HomeTeam"] in t.get_label()),
                    next(t for t in teams if game["AwayTeam"] in t.get_label()),
                    next(r for r in referee if game["Referee"] in r.get_label()),
                    game["FTHG"],
                    game["FTAG"]
                ))
            except StopIteration:
                print("Exception in line", index, file=sys.stderr)
                print(
                    game["HomeTeam"], [t for t in teams if game["HomeTeam"] in t.get_label()], "\n",
                    game["AwayTeam"], [t for t in teams if game["AwayTeam"] in t.get_label()], "\n",
                    game["Referee"], [r for r in referee if game["Referee"] in r.get_label()], "\n",file=sys.stderr
                )
    
    return games

def rank_to_teams(datafram):
    teams = []
    for index, team in datafram.iterrows():
        try :
            teams.append(Team(team["team"], 
                team["rank"],
                team["win"],
                team["loose"],
                team["draw"],
                None
            ))
        except ValueError:
            print("Erreur à la ligne",index)
            continue
    return teams

main()

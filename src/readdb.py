from tbox import Team, Game, GameUpComing, GamePlayed, Manager, Referee
import pandas as pd
import sys

def get_all(rank_file="../db/actual-ranking.csv",season_files = [
        "../db/2020-21.csv"],managers_file ="../db/managers.csv",
        upComingGames_file = "../db/upComingGames.csv"
    ):
    df_rank = pd.read_csv(rank_file)
    df_seasons = []
    for file in season_files:
        df_seasons.append(pd.read_csv(file))
    df_managers = pd.read_csv(managers_file)

    df_upComingGames = pd.read_csv(upComingGames_file)
    
    teams = rank_to_teams(df_rank)

    referee = seasons_to_referee(df_seasons)

    games = seasons_to_gamePlayed(df_seasons, teams, referee)

    managers = managers_to_managers(df_managers, teams)

    upComingGames = upComingGamesF(df_upComingGames, teams, referee)
    
    return teams, referee, games, managers, upComingGames

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

def upComingGamesF(df, teams, referee):
    games = []
    for index, game in df.iterrows():
        try:
            games.append(GameUpComing(
                game["Date"],
                next(t for t in teams if game["HomeTeam"] in t.get_label()),
                next(t for t in teams if game["AwayTeam"] in t.get_label()),
                next(r for r in referee if game["Referee"] in r.get_label())
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

def managers_to_managers(datafram,teams):
    managers = []
    for index, manager in datafram.iterrows():
        try :
            managers.append(Manager(
                manager["manager"],
                next(t for t in teams if manager["team"] == t.get_label())
            ))
        except ValueError:
            print("Erreur à la ligne",index)
            continue
    return managers


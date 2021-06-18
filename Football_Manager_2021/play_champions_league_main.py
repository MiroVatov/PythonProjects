from project.generate_players_and_teams import GeneratePlayersAndTeams
from project.tournaments.champions_league import ChampionsLeague


def main():

    teams_and_players = GeneratePlayersAndTeams()
    cl_teams = teams_and_players.champions_league_teams
    champions_league = ChampionsLeague(cl_teams, trophy_name="UEFA Champions League", prize_money=100_000_000)
    champions_league.draw_teams()

    print(champions_league.print_groups_teams())
    print(champions_league.print_all_team_strengths())
    print(champions_league.play_tournament())


if __name__ == '__main__':
    main()


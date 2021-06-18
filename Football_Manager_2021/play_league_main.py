from project.tournaments.league import League
from project.generate_players_and_teams import GeneratePlayersAndTeams


def main():

    teams_and_players = GeneratePlayersAndTeams()
    teams = teams_and_players.teams
    league = League()
    league.teams_schedule(teams)
    # league.initialize_dict(teams)
    # print(league.print_season_fixtures())
    league.play_league_tournament(league.rounds)
    print(league.print_standings_dict())
    # print(league.print_season_fixtures())


if __name__ == '__main__':
    main()

import unittest

from project.Teams.base_team import BaseTeam
from project.tournaments.champions_league import ChampionsLeague
from project.generate_players_and_teams import GeneratePlayersAndTeams


class ChampionsLeagueTests(unittest.TestCase):

    def setUp(self) -> None:

        self.teams_generator = GeneratePlayersAndTeams
        self.milan = self.teams_generator.milan
        self.real_madrid = self.teams_generator.real_madrid
        self.man_united = self.teams_generator.man_utd
        self.barca = self.teams_generator.barca
        self.tournament = ChampionsLeague([self.milan, self.real_madrid, self.man_united, self.barca], trophy_name="UEFA Champions League", prize_money=25_000_000)
        self.teams = [self.milan, self.man_united, self.real_madrid, self.barca]

    def test__init__(self):
        self.assertEqual(self.teams, [self.milan, self.man_united, self.real_madrid, self.barca])
        self.assertEqual("UEFA Champions League", self.tournament.trophy_name)
        self.assertEqual(25_000_000, self.tournament.prize_money)
        self.assertEqual(2, self.tournament.number_of_groups)
        self.assertEqual(4, self.tournament.maximum_teams_in_group)
        self.assertEqual(2, self.tournament.minimum_tams_in_group)
        self.assertEqual(2, len(self.tournament.groups))
        self.assertEqual("", self.tournament.teams_to_be_drawn)
        self.assertEqual(None, self.tournament.winning_team)
        self.assertEqual(None, self.tournament.losing_team)
        self.assertEqual({}, self.tournament.teams_dict)
        self.assertEqual(None, self.tournament.percent_chance)


if __name__ == "__main__":
    unittest.main()

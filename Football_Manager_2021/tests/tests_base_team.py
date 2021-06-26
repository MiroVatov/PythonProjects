import unittest

from project.Coaches.coach import Coach
from project.Players.defender import Defender
from project.Players.forward import Forward
from project.Players.goalkeeper import Goalkeeper
from project.Players.midfielder import Midfielder
from project.Teams.base_team import BaseTeam


class BaseTeamTest(unittest.TestCase):

    def setUp(self) -> None:
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000, chairman="Liubo Bechev", finances=11_000, nationality="bulgarian")

    def test__init__is_successful(self):
        self.assertEqual("Botev Vratsa", self.team.name)
        self.assertEqual("Vratsa", self.team.city)
        self.assertEqual("Hristo Botev", self.team.stadium)
        self.assertEqual(25_000, self.team.stadium_capacity)
        self.assertEqual("Liubo Bechev", self.team.chairman)
        self.assertEqual(11_000, self.team.finances)
        self.assertEqual("bulgarian", self.team.nationality)
        self.assertEqual([], self.team.players)
        self.assertEqual(100, self.team.team_chemistry)
        self.assertEqual("", self.team.financial_status)
        self.assertEqual(22, self.team.team_capacity_maximum)
        self.assertEqual(11, self.team.team_capacity_minimum)
        self.assertEqual(None, self.team.coach, None)

    def test_name_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.team = BaseTeam(name="", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000, chairman="Liubo Bechev",
                                 finances=11_000, nationality="bulgarian")
        self.assertEqual("Team name cannot be an empty string.", str(err_msg.exception))

    def test_city_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.team = BaseTeam(name="Botev Vratsa", city="", stadium="Hristo Botev", stadium_capacity=25_000, chairman="Liubo Bechev",
                                 finances=11_000, nationality="bulgarian")
        self.assertEqual("City name cannot be an empty string.", str(err_msg.exception))

    def test_stadium_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="", stadium_capacity=25_000, chairman="Liubo Bechev",
                                 finances=11_000, nationality="bulgarian")
        self.assertEqual("Stadium name cannot be an empty string.", str(err_msg.exception))

    def test_chairman_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000, chairman="",
                                 finances=11_000, nationality="bulgarian")
        self.assertEqual("Chairman name cannot be an empty string.", str(err_msg.exception))

    def test_finances_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000, chairman="Liubo Bechev",
                                 finances=9_000, nationality="bulgarian")
        self.assertEqual("Finances must be set to over 10_000", str(err_msg.exception))

    def test_nationality_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000, chairman="Liubo Bechev",
                                 finances=11_000, nationality="")
        expected_result = "Nationality cannot be an empty string."
        self.assertEqual(expected_result, str(err_msg.exception))

    def test_method_check_financial_status_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=11_110_000, nationality="bulgarian")
        expected_result = "Botev Vratsa financial status is Good"
        self.assertEqual(expected_result, self.team.check_financial_status())

    def test_method_check_team_capacity(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=11_110_000, nationality="bulgarian")

        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                              stamina=100, transfer_fee=10_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.player2 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                              stamina=100, transfer_fee=10_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.team.players = [self.player1, self.player2]
        self.assertEqual(True, self.team.check_team_capacity_maximum())

    def test_method_if_transfer_funds_are_enough(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=11_110_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.assertEqual(False, self.team.check_if_transfer_funds_are_enough(self.player1))

    def test_method_add_player_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=11_110_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        expected_result = f"Team Botev Vratsa successfully signed Miro as Free agent"
        self.assertEqual(expected_result, self.team.add_player(self.player1))
        self.assertEqual("Botev Vratsa", self.player1.player_club)
        self.assertEqual([self.player1], self.team.players)

    def test_method_add_player_player_already_in_the_club(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=11_110_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.team.add_player(self.player1)
        expected_result = f"{self.player1.name} already plays for your club {self.team.name}!"
        self.assertEqual(expected_result, self.team.add_player(self.player1))

    def test_method_buy_player_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=50_000_000, nationality="bulgarian")
        self.team2 = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=50_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.team2.add_player(self.player1)
        expected_result = f"{self.player1.name} successfully was signed from {self.team.name} for transfer fee: {self.player1.transfer_fee}"

        self.assertEqual(expected_result, self.team.buy_player(self.player1))
        self.assertEqual("Botev Vratsa", self.player1.player_club)
        self.assertEqual(37_000_000, self.team.finances)

    def test_method_buy_player_check_if_transfer_funds_are_enough(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=10_000_000, nationality="bulgarian")
        self.team2 = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=20_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.team2.buy_player(self.player1)

        expected_result = f"{self.team.name} does not have enough funds to buy {self.player1.name}"
        self.assertEqual(expected_result, self.team.buy_player(self.player1))

    def test_method_sign_player_as_free_agent_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=100_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        expected_result = f"{self.player1.name} has joined {self.team.name} as free agent"
        self.assertEqual(expected_result, self.team.sign_player_as_free_agent(self.player1))

    def test_method_sign_player_as_free_agent_player_already_signed_by_other_club(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=10_000_000, nationality="bulgarian")
        self.team2 = BaseTeam(name="Barcelona", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                              chairman="Liubo Bechev",
                              finances=20_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.team2.sign_player_as_free_agent(self.player1)
        expected_result = f"{self.player1.name} has already signed with {self.player1.player_club}"
        self.assertEqual(expected_result, self.team.sign_player_as_free_agent(self.player1))
        self.assertEqual("Barcelona", self.player1.player_club)

    def test_method_release_player_reached_minimum_players(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=10_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.team.sign_player_as_free_agent(self.player1)
        expected_result = f"{self.team.name} cannot release any more players. Team capacity minimum: {self.team.team_capacity_minimum}"
        self.assertEqual(expected_result, self.team.release_player(self.player1))
        self.assertEqual("Botev Vratsa", self.player1.player_club)

    def test_method_release_player_player_is_a_free_agent(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        expected_result = f"{self.player1.name} is a free agent and not pat of {self.team.name}."
        self.assertEqual(expected_result, self.team.release_player(self.player1))

    def test_method_release_player_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.player2 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.team.sign_player_as_free_agent(self.player1)
        self.team.sign_player_as_free_agent(self.player2)
        expected_result = f"{self.team.name} successfully released {self.player1.name}!"
        self.team.team_capacity_minimum = 0
        self.assertEqual(expected_result, self.team.release_player(self.player2))
        self.assertEqual(None, self.player2.player_club)

    def test_sell_player_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.team2 = BaseTeam(name="Barcelona", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                              chairman="Liubo Bechev",
                              finances=20_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.team.sign_player_as_free_agent(self.player1)
        expected_result = f"{self.team.name} successfully sold {self.player1.name} to {self.team2.name} for transfer amount: {self.player1.transfer_fee}."
        self.assertEqual(expected_result, self.team.sell_player(self.player1, self.team2))
        self.assertEqual(7_000_000, self.team2.finances)

    def test_sell_player_if_player_is_free_agent(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.team2 = BaseTeam(name="Barcelona", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                              chairman="Liubo Bechev",
                              finances=20_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        expected_result = f"{self.player1.name} is a free agent and can be brought without transfer fee."
        self.assertEqual(expected_result, self.team.sell_player(self.player1, self.team2))

    def test_method_sell_player_team_cannot_afford_the_transfer_fee(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.team2 = BaseTeam(name="Barcelona", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                              chairman="Liubo Bechev",
                              finances=10_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.team.sign_player_as_free_agent(self.player1)
        expected_result = f"{self.team2.name} cannot afford the transfer fee for {self.player1.name}"
        self.assertEqual(expected_result, self.team2.sell_player(self.player1, self.team2))

    def test_method_change_player_transfer_fee_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)
        self.team.add_player(self.player1)
        expected_result = f"{self.player1.name} transfer fee is changed to {self.player1.transfer_fee}"
        self.assertEqual(expected_result, self.team.change_player_transfer_fee(self.player1))
        self.assertEqual(13_000_000, self.player1.transfer_fee)

    def test_method_change_player_transfer_fee_player_not_in_team(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        expected_result = f"{self.player1.name} is not in {self.team.name}"
        self.assertEqual(expected_result, self.team.change_player_transfer_fee(self.player1))

    def test_method_change_player_salary_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        self.player1 = Forward(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                               stamina=100, transfer_fee=13_000_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.team.add_player(self.player1)
        expected_result = f"{self.player1.name} has new salary: 111111"  # NOTE input number 111111
        self.assertEqual(expected_result, self.team.change_player_salary(self.player1))

    def test_calculate_team_strength_success(self):

        def add_players_to_club(players_slot, club):
            for player in players_slot:
                club.add_player(player)
            return club

        gk_team4 = Goalkeeper(name="Iker Casillas", height=185, weight=86, salary=7_650_000,
                              contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_000_000, handling=9,
                              jumping=9, reflexes=9)
        df1_team4 = Defender(name="Alvaro Arbeloa", height=185, weight=83, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_000_000, heading=8, pace=9,
                             positioning=8, tackling=9)
        df2_team4 = Defender(name="Marcelo", height=176, weight=73, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=10,
                             pace=9, positioning=9, tackling=9)
        df3_team4 = Defender(name="Sergio Ramos", height=188, weight=87, salary=7_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=10_000_000, heading=9,
                             pace=9, positioning=9, tackling=9)
        df4_team4 = Defender(name="Pepe", height=187, weight=88, salary=5_800_000, contract_expiry_date="20/July/2022",
                             stamina=10, transfer_fee=11_000_000, heading=9, pace=9, positioning=9, tackling=9)
        mf1_team4 = Midfielder(name="Xabi Alonso", height=180, weight=78, salary=10_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000, agression=10,
                               creativity=9, pace=8, passing=9, shooting=9)
        mf2_team4 = Midfielder(name="Sami Khedira", height=188, weight=85, salary=9_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, agression=9,
                               creativity=8, pace=8, passing=8, shooting=8)
        mf3_team4 = Midfielder(name="Mesut Ozil", height=178, weight=75, salary=10_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=11_000_000, agression=10,
                               creativity=10, pace=8, passing=9, shooting=8)
        mf4_team4 = Midfielder(name="Angel DiMaria", height=177, weight=72, salary=12_000_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, agression=8,
                               creativity=9, pace=9, passing=9, shooting=9)
        fw1_team4 = Forward(name="Cristiano Ronaldo", height=186, weight=81, salary=14_800_00,
                            contract_expiry_date="20/July/2022", stamina=10, transfer_fee=97_500_000, speed=10,
                            technique=9, goalscoring=9, heading=9)
        fw2_team4 = Forward(name="Karim Benzema", height=188, weight=81, salary=10_800_00,
                            contract_expiry_date="20/July/2022", stamina=9, transfer_fee=18_500_000, speed=8,
                            technique=9, goalscoring=9, heading=9)

        real_madrid = BaseTeam(name="Real Madrid", city="Madrid", stadium="Santiago Bernabeu", stadium_capacity=78_000,
                               chairman="Florentino Perez", finances=200_000_000, nationality="Spain")
        players_slot_4 = [gk_team4, df1_team4, df2_team4, df3_team4, df4_team4, mf1_team4, mf2_team4, mf3_team4,
                          mf4_team4, fw1_team4, fw2_team4]
        real_madrid = add_players_to_club(players_slot_4, real_madrid)
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")
        real_madrid.sign_coach(jose_mourinho)
        expected_result = 751
        self.assertEqual(expected_result, real_madrid.calculate_team_strength)

    def test_method_sign_coach_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")

        expected_result = f"{jose_mourinho.name} has joined {self.team.name} successfully"
        self.assertEqual(expected_result, self.team.sign_coach(jose_mourinho))
        self.assertEqual(jose_mourinho, self.team.coach)
        self.assertEqual(self.team.name, jose_mourinho.team)
        self.assertEqual(True, jose_mourinho.occupied)
        self.assertEqual(6_000_000, self.team.finances)

    def test_method_sign_coach_team_already_have_coach(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")
        pep_guardiola = Coach(name="Josep Guardiola", nationality="spanish", age=50, salary=10_000_000, experience=7,
                              mentality="attacking", coaching_ability=9, formation="4-3-3")

        self.team.sign_coach(jose_mourinho)
        expected_result = f"{self.team.name} have already a coach {jose_mourinho.name}"
        self.assertEqual(expected_result, self.team.sign_coach(pep_guardiola))

    def test_method_sign_coach_already_signed_with_another_club(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")

        self.team2 = BaseTeam(name="Barcelona", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                              chairman="Liubo Bechev",
                              finances=10_000_000, nationality="bulgarian")
        self.team.sign_coach(jose_mourinho)
        expected_result = f"{jose_mourinho.name} has already signed with {jose_mourinho.team}"
        self.assertEqual(expected_result, self.team2.sign_coach(jose_mourinho))

    def test_method_sign_coach_team_has_no_funds(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=9_000_000, nationality="bulgarian")
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=10_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")
        expected_result = f"{self.team.name} has no financial funds to sign {jose_mourinho.name} with salary {jose_mourinho.salary}"
        self.assertEqual(expected_result, self.team.sign_coach(jose_mourinho))

    def test_method_release_coach_success(self):
        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")

        expected_result = f"{self.team.name} has successfully released {jose_mourinho.name}"

        self.team.sign_coach(jose_mourinho)
        self.assertEqual(expected_result, self.team.release_coach(jose_mourinho))
        self.assertEqual(False, jose_mourinho.occupied)
        self.assertEqual(None, self.team.coach)
        self.assertEqual(None, jose_mourinho.team)

    def test_method_release_coach_the_coach_has_another_team(self):

        self.team = BaseTeam(name="Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                             chairman="Liubo Bechev",
                             finances=15_000_000, nationality="bulgarian")
        jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                              mentality="defensive", coaching_ability=8, formation="4-1-4-1")
        self.team2 = BaseTeam(name="Barcelona", city="Vratsa", stadium="Hristo Botev", stadium_capacity=25_000,
                              chairman="Liubo Bechev",
                              finances=10_000_000, nationality="bulgarian")

        self.team.sign_coach(jose_mourinho)
        expected_result = f"{jose_mourinho.name} is not in your team {self.team2.name}"
        self.assertEqual(expected_result, self.team2.release_coach(jose_mourinho))

    def test_method_show_Squad(self):
        gk_team2 = Goalkeeper(name="Nelson Dida", height=194, weight=95, salary=4_650_000,
                              contract_expiry_date="20/July/2022", stamina=9, transfer_fee=3_000_000, handling=10,
                              jumping=9, reflexes=9)
        df1_team2 = Defender(name="Paolo Maldini", height=186, weight=87, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=9,
                             pace=9, positioning=10, tackling=10)
        df2_team2 = Defender(name="Cafu", height=181, weight=77, salary=4_600_000, contract_expiry_date="20/July/2022",
                             stamina=10, transfer_fee=6_500_000, heading=6, pace=9, positioning=9, tackling=9)
        df3_team2 = Defender(name="Alessandro Nesta", height=185, weight=80, salary=5_200_000,
                             contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_600_00, heading=9, pace=9,
                             positioning=9, tackling=10)
        df4_team2 = Defender(name="Franco Baresi", height=185, weight=80, salary=3_800_000,
                             contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, heading=10,
                             pace=9, positioning=8, tackling=9)
        mf1_team2 = Midfielder(name="Gennaro Gatuso", height=177, weight=80, salary=4_500_000,
                               contract_expiry_date="20/July/2022", stamina=10, transfer_fee=5_000_000, agression=9,
                               creativity=9, pace=10, passing=9, shooting=8)
        mf2_team2 = Midfielder(name="Andrea Pirlo", height=181, weight=82, salary=5_500_000,
                               contract_expiry_date="20/July/2022", stamina=8, transfer_fee=9_500_000, agression=10,
                               creativity=9, pace=8, passing=8, shooting=9)
        mf3_team2 = Midfielder(name="Dejan Savjcevic", height=178, weight=77, salary=7_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=8_000_000, agression=10,
                               creativity=9, pace=9, passing=9, shooting=9)
        mf4_team2 = Midfielder(name="Ricardo Kaka", height=183, weight=82, salary=10_000_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_500_000, agression=10,
                               creativity=9, pace=9, passing=10, shooting=9)
        fw1_team2 = Forward(name="Filippo Inzaghi", height=181, weight=75, salary=6_800_00,
                            contract_expiry_date="20/July/2022", stamina=8, transfer_fee=8_000_000, speed=8,
                            technique=8, goalscoring=9, heading=9)
        fw2_team2 = Forward(name="Andriy Schevchenko", height=186, weight=81, salary=9_800_00,
                            contract_expiry_date="20/July/2022", stamina=8, transfer_fee=10_500_000, speed=9,
                            technique=9, goalscoring=9, heading=9)

        players_slot_2 = [gk_team2, df1_team2, df2_team2, df3_team2, df4_team2, mf1_team2, mf2_team2, mf3_team2,
                          mf4_team2, fw1_team2, fw2_team2]
        milan = BaseTeam(name="AC MILAN", city="Milano", stadium="San Siro", stadium_capacity=85_000,
                         chairman="Silvio Berlusconi", finances=105_000_000, nationality="Italy")

        def add_players_to_club(players_slot, club):
            for player in players_slot:
                club.add_player(player)
            return club
        milan = add_players_to_club(players_slot_2, milan)
        expected_result = "AC MILAN squad, Nelson Dida, Paolo Maldini, Cafu, Alessandro Nesta, Franco Baresi, Gennaro Gatuso, Andrea Pirlo," \
                          " Dejan Savjcevic, Ricardo Kaka, Filippo Inzaghi, Andriy Schevchenko"

        self.assertEqual(expected_result, milan.show_squad())


if __name__ == "__main__":
    unittest.main()


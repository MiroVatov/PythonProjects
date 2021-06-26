import unittest

from project.Players.midfielder import Midfielder


class MidfielderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Midfielder(name="Miro", height=179, weight=81, salary=100000, contract_expiry_date="10-10-2025",
                                 stamina=100, transfer_fee=10_000_000, agression=10, passing=10, creativity=10, pace=10, shooting=10)

    def test__init__method_successful(self):
        self.assertEqual("Miro", self.player.name)
        self.assertEqual(179, self.player.height)
        self.assertEqual(81, self.player.weight)
        self.assertEqual(100000, self.player.salary)
        self.assertEqual("10-10-2025", self.player.contract_expiry_date)
        self.assertEqual(100, self.player.stamina)
        self.assertEqual(10_000_000, self.player.transfer_fee)
        self.assertEqual(10, self.player.agression)
        self.assertEqual(10, self.player.passing)
        self.assertEqual(10, self.player.creativity)
        self.assertEqual(10, self.player.pace)
        self.assertEqual(10, self.player.shooting)
        self.assertEqual(None, self.player.player_club)
        self.assertEqual(False, self.player.injured)

    def test_name_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.player = Midfielder(name="", height=179, weight=81, salary=100000,
                                     contract_expiry_date="10-10-2025",
                                     stamina=100, transfer_fee=10_000_000, agression=10, passing=10, creativity=10,
                                     pace=10, shooting=10)
        self.assertEqual("Player name cannot be an empty string.", str(err_msg.exception))

    def test_height_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.player = Midfielder(name="Miro", height=139, weight=81, salary=100000,
                                     contract_expiry_date="10-10-2025",
                                     stamina=100, transfer_fee=10_000_000, agression=10, passing=10, creativity=10,
                                     pace=10, shooting=10)
        self.assertEqual(f"Player's height can be over {range(150, 230 + 1)} cm", str(err_msg.exception))

    def test_salary_raises_value_error(self):
        with self.assertRaises(ValueError) as err_msg:
            self.player = Midfielder(name="Miro", height=179, weight=81, salary=1000,
                                     contract_expiry_date="10-10-2025",
                                     stamina=100, transfer_fee=10_000_000, agression=10, passing=10, creativity=10,
                                     pace=10, shooting=10)
        self.assertEqual(f"Players salary should be between {range(100_000, 15_000_000 + 1)} US dollars",
                         str(err_msg.exception))

    def test_injury_not_correct(self):
        self.player.injured = True
        self.assertFalse(False, self.player.injured)

    def test_stamina_not_correct(self):
        self.player.stamina = 99
        self.assertIsNot(100, self.player.stamina)

    def test_contract_expiry_data_not_correct(self):
        self.player.contract_expiry_date = "22_22_2022"
        self.assertIsNot("10-10-2025", self.player.contract_expiry_date)


if __name__ == "__main__":
    unittest.main()
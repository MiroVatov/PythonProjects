import argparse

from project.Players.base_player import BasePlayer


class Forward(BasePlayer):
    def __init__(self, name: str, height: int, weight: int, salary: int, contract_expiry_date: str, stamina: int, transfer_fee: int,
                 speed: int, technique: int, goalscoring: int, heading: int):
        super(Forward, self).__init__(name, height, weight, salary, contract_expiry_date, stamina, transfer_fee, health=10)
        self.speed = speed
        self.technique = technique
        self.goalscoring = goalscoring
        self.heading = heading

    @property
    def player_strength(self):
        return self.health + self.stamina + self.heading + self.speed + self.goalscoring + self.technique

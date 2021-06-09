from project.Players.base_player import BasePlayer


class Midfielder(BasePlayer):
    def __init__(self, name: str, height: int, weight: int, salary: int, contract_expiry_date: str, stamina: int, transfer_fee: int,
                 agression, passing, creativity, pace, shooting):
        super(Midfielder, self).__init__(name, height, weight, salary, contract_expiry_date, stamina, transfer_fee, health=100)
        self.agression = agression
        self.passing = passing
        self.creativity = creativity
        self.pace = pace
        self.shooting = shooting

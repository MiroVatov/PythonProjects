from project.Players.base_player import BasePlayer


class Defender(BasePlayer):

    def __init__(self, name: str, height: int, weight: int, salary: int, contract_expiry_date: str, stamina: int, transfer_fee: int,
                 positioning, tackling, heading, pace):
        super(Defender, self).__init__(name, height, weight, salary, contract_expiry_date, stamina, transfer_fee, health=10)
        self.positioning = positioning
        self.tackling = tackling
        self.heading = heading
        self.pace = pace

    @property
    def player_strength(self):
        return self.health + self.stamina + self.heading + self.pace + self.tackling + self.positioning

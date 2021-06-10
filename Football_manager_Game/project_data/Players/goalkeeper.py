from project.Players.base_player import BasePlayer


class Goalkeeper(BasePlayer):

    def __init__(self, name: str, height: int, weight: int, salary: int, contract_expiry_date: str, stamina: int, transfer_fee: int,
                 handling: int, reflexes: int, jumping: int):
        super(Goalkeeper, self).__init__(name, height, weight, salary, contract_expiry_date, stamina, transfer_fee, health=10)
        self.handling = handling
        self.jumping = jumping
        self.reflexes = reflexes

    @property
    def player_strength(self):
        return self.health + self.stamina + self.handling + self.jumping + self.reflexes



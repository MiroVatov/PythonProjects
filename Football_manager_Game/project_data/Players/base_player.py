from abc import ABC, abstractmethod


class BasePlayer(ABC):
    height_restrictions = range(150, 230 + 1)
    salary_restrictions = range(100_000, 15_000_000 + 1)
    qualities_range = range(1, 10 + 1)

    @abstractmethod
    def __init__(self, name: str, height: int, weight: int, salary: int, contract_expiry_date: str, stamina: int, transfer_fee: int, health: int):
        self.name = name
        self.height = height
        self.weight = weight
        self.salary = salary
        self.contract_expiry_date = contract_expiry_date
        self.stamina = stamina
        self.transfer_fee = transfer_fee
        self.health = health
        self.player_club = None
        self.transfer_fee = 0
        self.injured = False

    @property
    def name(self):
        return self.__name

    # method checks if players name is not blank
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Player name cannot be an empty string.")
        self.__name = value

    @property
    def height(self):
        return self.__height

    # method checks if players height is/not in the restrictions
    @height.setter
    def height(self, value):
        if value not in BasePlayer.height_restrictions:
            raise ValueError(f"Player's height can be over {BasePlayer.height_restrictions} cm")
        self.__height = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value not in BasePlayer.salary_restrictions:
            raise ValueError(f"Players salary should be between {BasePlayer.salary_restrictions} US dollars")
        self.__salary = value

    # @property
    # def health(self):
    #     return self.__health
    #
    # @health.setter
    # def health(self, value):
    #     if value <= 0:
    #         self.injured = True
    #     self.__health = value

    # method checks and returns player's position
    def check_player_position(self):
        return self.__class__.__name__

    def injury(self):
        self.health = 0
        self.injured = True

    def heal(self):
        self.health = 100
        self.injured = False

    @abstractmethod
    def player_strength(self):
        pass




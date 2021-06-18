from project.Coaches.coach import Coach
from project.Players.base_player import BasePlayer


class BaseTeam:

    def __init__(self, name: str, city: str, stadium: str, stadium_capacity: int, chairman: str, finances: int, nationality: str):
        self.name = name
        self.city = city
        self.stadium = stadium
        self.stadium_capacity = stadium_capacity
        self.chairman = chairman
        self.finances = finances
        self.nationality = nationality
        self.players = []  # keeps the players(objects), which are into the team
        self.team_chemistry = 100  # create a method to calculate the team chemistry, from the players qualities
        self.financial_status = ""  # "Poor", "Ok", "Good", "Excellent"
        self.team_capacity_maximum = 22
        self.team_capacity_minimum = 11
        self.coach = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Team name cannot be an empty string.")
        self.__name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if value == "":
            raise ValueError("City name cannot be an empty string.")
        self.__city = value

    @property
    def stadium(self):
        return self.__stadium

    @stadium.setter
    def stadium(self, value):
        if value == "":
            raise ValueError("Stadium name cannot be an empty string.")
        self.__stadium = value

    @property
    def chairman(self):
        return self.__chairman

    @chairman.setter
    def chairman(self, value):
        if value == "":
            raise ValueError("Chairman name cannot be an empty string.")
        self.__chairman = value

    @property
    def finances(self):
        return self.__finances

    @finances.setter
    def finances(self, value):
        if value <= 10_000:
            raise ValueError("Finances must be set to over 10_000")
        self.__finances = value

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, value):
        if value == "":
            raise ValueError("Nationality cannot be an empty string.")
        self.__nationality = value

    def check_financial_status(self):
        if self.finances < 0:
            self.financial_status = "Bankrupt"

        elif 0 < self.finances <= 1_000_000:
            self.financial_status = "Poor"

        elif 1_000_000 < self.finances <= 10_000_000:
            self.financial_status = "Ok"

        elif 10_000_000 < self.finances <= 50_000_000:
            self.financial_status = "Good"

        elif self.finances > 50_000_000:
            self.financial_status = "Excellent"

        return f"{self.name} financial status is {self.financial_status}. Remaining Finances: {self.finances}"

    def check_team_capacity_maximum(self):
        if len(self.players) < self.team_capacity_maximum:
            return True
        return False

    def check_team_capacity_minimum(self):
        if len(self.players) - 1 >= self.team_capacity_minimum:
            return True
        return False

    def check_if_transfer_funds_are_enough(self, player: BasePlayer):
        if self.finances - player.transfer_fee > 0:
            return True
        return False

    # def add_player(self, player: BasePlayer):
    #     if player not in self.players:
    #         if not self.check_team_capacity_maximum():
    #             return f"You cannot sign more players for {self.name}. You reached the maximum players limit {self.team_capacity_limit}!"
    #
    #         player.player_club = self.name
    #         self.players.append(player)
    #         return f"Team {self.name} successfully signed {player.name} as Free agent"
    #     return f"{player.name} already plays for your club {self.name}!"

    "------------------BETTER VERSION OF THE METHOD < add_player >--------------------------------------------------------"

    def add_player(self, player: BasePlayer):
        if player in self.players:
            return f"{player.name} already plays for your club {self.name}!"
        if not self.check_team_capacity_maximum():
            return f"You cannot sign more players for {self.name}. You reached the maximum players limit {self.team_capacity_maximum}!"

        player.player_club = self.name
        self.players.append(player)
        return f"Team {self.name} successfully signed {player.name} as Free agent"

    def buy_player(self, player: BasePlayer):
        if not self.check_if_transfer_funds_are_enough(player):
            return f"{self.name} does not have enough funds to buy {player.name}"
        if player.player_club is None:
            return f"{player.name} is a free agent and you should use method sign_player_as_free_agent to sign him for free"
        if not self.check_team_capacity_maximum():
            return f"{player.player_club} cannot buy more players. Maximum number of players is {self.team_capacity_maximum}"

        player.player_club = self.name
        self.players.append(player)
        self.finances -= player.transfer_fee
        return f"{player.name} successfully was signed from {self.name} for transfer fee: {player.transfer_fee}"

    def sign_player_as_free_agent(self, player):
        if player.player_club is None:
            self.add_player(player)
            return f"{player.name} has joined {self.name} as free agent"

        return f"{player.name} has already signed with {player.player_club}"

    def release_player(self, player: BasePlayer):
        if player.player_club is None:
            return f"{player.name} is a free agent and not pat of {self.name}."
        if not self.check_team_capacity_minimum():
            return f"{self.name} cannot release any more players. Team capacity minimum: {self.team_capacity_minimum}"

        self.players.remove(player)
        player.player_club = None
        return f"{self.name} successfully released {player.name}!"

    def sell_player(self, player: BasePlayer, second_team):

        if not second_team.check_team_capacity_maximum():
            return f"{second_team.name} doesnt have more space for new players."
        if not self.check_team_capacity_minimum():
            return f"{player.player_club} cannot sell more players. Minimum number of players is {self.team_capacity_minimum}"
        if player.player_club is None:
            return f"{player.name} is a free agent and can be brought without transfer fee."

        if second_team.check_if_transfer_funds_are_enough(player) and player in self.players:
            second_team.buy_player(player)
            self.players.remove(player)
            self.finances -= player.transfer_fee
            return f"{self.name} successfully sold {player.name} to {second_team.name} for transfer amount: {player.transfer_fee}."

    def change_player_transfer_fee(self, player):
        if player in self.players:
            print(f"Please add new transfer fee for {player.name}: ")
            new_transfer_fee = int(input())
            player.transfer_fee = new_transfer_fee
            return f"{player.name} transfer fee is changed to {player.transfer_fee}"
        return f"{player.name} is not in {self.name}"

    def change_player_salary(self, player):
        if player in self.players:
            print(f"Please add new player salary for {player.name}")
            new_salary = int(input())
            player.salary = new_salary
            return f"{player.name} has new salary: {player.salary}"
        return f"{player.name} is not in {self.name}"

    @property
    def calculate_team_strength(self):
        team_strength = 0
        for player in self.players:
            team_strength += player.player_strength
        if self.coach is not None:
            team_strength += self.coach.calculate_coach_strength + self.team_chemistry
        return team_strength

    @property
    def message_for_team_strength(self):
        team_strength = self.calculate_team_strength
        return f"{self.name} team strength: {team_strength}"

    def sign_coach(self, coach: Coach):
        if self.coach is not None:
            return f"{self.name} have already a coach {self.coach.name}"
        if coach.occupied:
            return f"{coach.name} has already signed with {coach.team}"
        if self.finances - coach.salary <= 0:
            return f"{self.name} has no financial funds to sign {coach.name} with salary {coach.salary}"

        self.coach = coach
        coach.team = self.name
        coach.occupied = True
        self.finances -= coach.salary
        return f"{coach.name} has joined {self.name} successfully"

    def release_coach(self, coach: Coach):
        if coach.team is not None:
            return f"{coach.name} is not in your team {self.name}"
        if not coach.occupied:
            return f"{coach.name} is free agent, but is not on your team {self.name}"

        self.coach = None
        coach.occupied = False
        coach.team = None
        self.finances += coach.salary
        return f"{self.name} has successfully released {coach.name}"

    def show_squad(self):
        data = [f"{self.name} squad"]
        for player in self.players:
            data.append(player.name)
        return ', '.join(data)






import random
import copy
from collections import deque


class ChampionsLeague:
    winning_team_gain_points = 80
    losing_team_losing_points = 50
    tournament_winner = None
    tournament_loser = None
    object = None
    points_for_win = 3
    points_given_by_the_chance = 30

    def __init__(self, teams: list, trophy_name: str, prize_money: int):
        self.teams = teams
        self.trophy_name = trophy_name
        self.prize_money = prize_money
        self.number_of_groups = len(self.teams) // 2
        self.maximum_teams_in_group = 4
        self.minimum_tams_in_group = 2  # random choice
        self.groups = [[] for _ in range(self.number_of_groups)]
        self.teams_to_be_drawn = ""
        self.winning_team = None
        self.losing_team = None
        self.teams_dict = {}
        self.final_round = False
        self.percent_chance = None

    @staticmethod
    def _calculate_percent_chance_random():
        percent = random.choice(range(1, 3))
        return percent

    def fill_the_teams_dict(self, team1, team2):
        if team1.name and team2.name not in self.teams_dict.keys():
            self.teams_dict[team1.name] = [0, 0, 0]
            self.teams_dict[team2.name] = [0, 0, 0]
        return self.teams_dict

    def fill_the_results_in_teams_dict(self, winner_team, losing_team, team1_goals, team2_goals):
        self.teams_dict[winner_team.name][0] += team1_goals
        self.teams_dict[winner_team.name][1] += team2_goals
        self.teams_dict[winner_team.name][2] += ChampionsLeague.points_for_win
        self.teams_dict[losing_team.name][0] += team2_goals
        self.teams_dict[losing_team.name][1] += team1_goals
        return self.teams_dict

    def draw_teams(self):
        self.teams_to_be_drawn = copy.copy(self.teams)
        index = 0
        while index < self.number_of_groups:
            team1 = random.choice(self.teams_to_be_drawn)
            team2 = random.choice(self.teams_to_be_drawn)
            if team1.name != team2.name:
                self.groups[index] = [team1, team2]
                self.teams_dict = self.fill_the_teams_dict(team1, team2)
                self.teams_to_be_drawn.remove(team1)
                self.teams_to_be_drawn.remove(team2)
                index += 1

    @property
    def generate_result_first_team_win(self):
        while True:
            home_goals = random.choice(range(1, 6))
            away_goals = random.choice(range(1, 6))
            if home_goals > away_goals:
                return home_goals, away_goals

    @property
    def generate_result_second_team_win(self):
        while True:
            home_goals = random.choice(range(1, 6))
            away_goals = random.choice(range(1, 6))
            if away_goals > home_goals:
                return away_goals, home_goals

    @staticmethod
    def _check_if_list_is_nested(groups):
        if any(isinstance(i, list) for i in groups):
            return True
        return False

    def play_tournament(self):
        games_number = 0
        while len(self.groups) > 1:
            first_team_power = 0
            second_team_power = 0
            if self._check_if_list_is_nested(self.groups):
                self.groups = deque(self.groups)
                game = self.groups.popleft()
                first_team = game[0]
                second_team = game[1]
            else:
                self.final_round = True
                first_team = self.groups.popleft()
                second_team = self.groups.popleft()

            team_to_benefit_from_the_chance = self._calculate_percent_chance_random()
            if team_to_benefit_from_the_chance == 1:
                first_team_power += ChampionsLeague.points_given_by_the_chance
            else:
                second_team_power += ChampionsLeague.points_given_by_the_chance
            first_team_power += first_team.calculate_team_strength
            second_team_power += second_team.calculate_team_strength
    # TODO if both teams have same team strength -> add a method for penalties or some to decide who is the winner
            if first_team_power > second_team_power:
                first_team_goals, second_team_goals = self.generate_result_first_team_win
                first_team.team_chemistry += ChampionsLeague.winning_team_gain_points
                second_team.team_chemistry -= ChampionsLeague.losing_team_losing_points
                self.teams_dict = self.fill_the_results_in_teams_dict(first_team, second_team, first_team_goals, second_team_goals)
                ChampionsLeague.tournament_winner = first_team
                ChampionsLeague.tournament_loser = second_team
                games_number += 1
                print(f"The winner in game {games_number} is {first_team.name} won the game with result {first_team_goals}:{second_team_goals} and {second_team.name} have to leave the competition!")
            else:
                second_team_goals, first_team_goals = self.generate_result_second_team_win
                self.teams_dict = self.fill_the_results_in_teams_dict(second_team, first_team, second_team_goals, first_team_goals)
                second_team.team_chemistry += ChampionsLeague.winning_team_gain_points
                first_team.team_chemistry -= ChampionsLeague.losing_team_losing_points
                ChampionsLeague.tournament_winner = second_team
                ChampionsLeague.tournament_loser = first_team
                games_number += 1
                print(f"The winner in game {games_number} is {second_team.name} won the game with result {second_team_goals}:{first_team_goals} and {first_team.name} have to leave the competition!")
            self.groups.append(ChampionsLeague.tournament_winner)
        return self.print_final_report

    def print_groups_teams(self):
        data = []
        for group in range(len(self.groups)):
            data.append(f"Group {group + 1} teams: ")
            data_to_add = self.groups[group]
            for index in range(len(data_to_add)):
                data.append(data_to_add[index].name)
        return '\n'.join(data)

    @property
    def print_final_report(self):
        data = ""
        data += f"{ChampionsLeague.tournament_winner.name} is the winner in the {self.trophy_name} competition!" + '\n'
        sorted_teams_dict = dict(sorted(self.teams_dict.items(), key=lambda x: -x[1][2]))
        data += f"Final Standings" + '\n'
        for team, goals_data in sorted_teams_dict.items():
            data += f"{team} with points: {goals_data[2]} and goal difference {goals_data[0]}:{goals_data[1]}" + '\n'
        return data

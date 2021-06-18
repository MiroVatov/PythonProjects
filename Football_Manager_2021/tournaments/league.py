
from project.generate_players_and_teams import GeneratePlayersAndTeams
from collections import deque
from random import choice


class League:

    points_for_win = 3
    points_for_draw = 1
    points_given_by_the_chance = 30
    winning_team_gain_points = 10
    losing_team_losing_points = 0
    final_week = 31

    def __init__(self):
        self.teams = GeneratePlayersAndTeams().teams
        self.coaches = GeneratePlayersAndTeams().coaches
        self.free_agents_pool = GeneratePlayersAndTeams().free_agents_slot
        self.rounds = self.teams_schedule(self.teams)
        self.winning_team = None
        self.losing_team = None
        self.standings_dict = {}
        self.week_number = 0
        self.chosen_team = None
        self.possible_answers = ['add_player', 'buy_player', 'sell_player',
              'release_player', 'sign_player_as_free_agent', 'change_player_transfer_fee', 'sign_coach', 'release_coach', 'show_squad',
              'check_financial_status', 'message_for_team_strength', 'print_all_teams_strengths']

    @staticmethod
    def teams_schedule(teams):
        if len(teams) % 2:
            teams.append('Day off')
        n = len(teams)
        matches = []
        fixtures = []
        return_matches = []
        for fixture in range(1, n):
            for i in range(n // 2):
                matches.append((teams[i], teams[n - 1 - i]))
                return_matches.append((teams[n - 1 - i], teams[i]))

            teams.insert(1, teams.pop())
            fixtures.insert(len(fixtures) // 2, matches)
            fixtures.append(return_matches)
            matches = []
            return_matches = []

        return fixtures

    def initialize_dict(self, teams_list):
        for team in teams_list:
            if team.name not in self.standings_dict.keys():
                self.standings_dict[team.name] = {"games played": 0, "team goals": 0, "goals conceded": 0, "wins": 0, "loses": 0, "draws": 0, "points": 0}
        return self.standings_dict

    def play_league_tournament(self, league_rounds):
        league_rounds = deque(league_rounds)
        self.week_number = 1
        self.standings_dict = self.initialize_dict(self.teams)
        print(self.print_season_fixtures())

        while league_rounds:
            round_teams = league_rounds.popleft()

            self.play_round(round_teams, self.week_number)
            self.week_number += 1
            print("Do yuo want to make some changes to the team Or the Coach? Y or N")
            answer = input()
            if answer == "Y":

                proceed_with_the_changes = True
                while True:
                    if not proceed_with_the_changes:
                        break
                    print(f"Please type a team name in order to make some changes. Choose from {self.print_team_names_in_the_league()}")
                    self.chosen_team = input()
                    self.chosen_team = self.choose_team(self.chosen_team)
                    if self.chosen_team is not None:
                        self.make_team_changes(self.chosen_team)
                        print("Do you want to make more changes ? Y or N")
                        changes = input()
                        if changes != "Y":
                            proceed_with_the_changes = False

            if self.week_number == League.final_week:
                self.print_standings_dict()

    def play_round(self, round_teams, week_number):
        print(self.print_round_fixtures(round_teams, week_number))
        round_results_dict = {}
        for match in round_teams:
            self.play_match(match, round_results_dict, week_number)
        print("Do you want the League stats? Y or N")
        answer = input()
        if answer == "Y":
            print(self.print_standings_dict())
        print(self.print_weekly_round_results(round_results_dict, week_number))

    def play_match(self, pair_teams, round_results_dict, week_number):
        team_one, team_two = pair_teams[0], pair_teams[1]
        team_one_power, team_two_power = team_one.calculate_team_strength, team_two.calculate_team_strength
        team_to_benefit_from_the_chance = self._calculate_percent_chance_random()

        if team_to_benefit_from_the_chance == 1:
            team_one_power += League.points_given_by_the_chance
        else:
            team_two_power += League.points_given_by_the_chance

        if team_one_power > team_two_power:
            team_one_goals, team_two_goals = self.generate_result_first_team_win
            team_one.team_chemistry += League.winning_team_gain_points
            team_two.team_chemistry -= League.losing_team_losing_points
            self.standings_dict = self.fill_in_the_dict_after_match_if_first_team_won(team_one, team_two, team_one_goals, team_two_goals)

        elif team_two_power > team_one_power:
            team_two_goals, team_one_goals = self.generate_result_second_team_win
            team_two.team_chemistry += League.winning_team_gain_points
            team_one.team_chemistry -= League.losing_team_losing_points
            self.standings_dict = self.fill_in_the_dict_after_match_if_second_team_won(team_one, team_two, team_one_goals, team_two_goals)

        elif team_one_power == team_two_power:
            team_two_goals, team_one_goals = self.generate_result_for_draw
            self.standings_dict = self.fill_in_the_dict_after_match_if_match_ended_draw(team_one, team_two, team_one_goals, team_two_goals)
        if team_one not in round_results_dict.keys():
            round_results_dict[team_one.name] = {team_one.name: team_one_goals, team_two.name: team_two_goals}
        round_results_dict[team_one.name].update({team_one.name: team_one_goals, team_two.name: team_two_goals})

    def choose_team(self, team_name):
        for team in self.teams:
            if team_name == team.name:
                return team
        return None

    def get_free_player(self, player_name):
        for player in self.free_agents_pool:
            if player.name == player_name:
                return player
        return None

    def get_buy_player(self, player_name):
        for team in self.teams:
            for player in team.players:
                if player_name == player.name:
                    return player
        return None

    def get_coach(self, coach_name, team):
        if team.coach is None:
            for coach in self.coaches:
                if coach_name == coach.name:
                    return coach
        return None

    def find_club(self, second_club_name):
        for club in self.teams:
            if club.name == second_club_name:
                return club
        return None

    @staticmethod
    def print_weekly_round_results(weekly_results_dict, week_number):
        data = f"{week_number} Week results: " + '\n'
        for week, results in weekly_results_dict.items():
            for team, goals_scored in results.items():
                data += f"{team} - {goals_scored} "
            data += '\n'
        return data

    @staticmethod
    def print_player_to_interact_with_message():
        return "Please choose a player name to interact with" + '\n'

    @staticmethod
    def print_message_the_player_is_not_in_the_league_teams(player_name):
        return f"{player_name} is not in the League current teams lists and maybe he is a free agent" + '\n'

    def show_available_coaches(self):
        data = []
        for coach in self.coaches:
            data.append(coach.name)
        return '\n'.join(data) + '\n'

    def make_team_changes(self, team):
        print(f"What do you want to do with the team? Possible answers : {', '.join(self.possible_answers)}")
        answer = input()

        while answer not in self.possible_answers:
            print(f"Please choose from the possible answer:  {', '.join(self.possible_answers)}")

        if answer == "add_player":
            print(f"Choose from the free agents pool:  {' ,'.join(self.print_free_agents())}")
            print(self.print_player_to_interact_with_message())
            player_name = input()
            player = self.get_free_player(player_name)
            if not player:
                return f"{player_name} you choose is not in the freee agents list and is not created or added to the free agents list."
            print(team.add_player(player))
            self.free_agents_pool.remove(player)

        elif answer == "sign_player_as_free_agent":
            print(f"Choose from the free agents pool:  {' ,'.join(self.print_free_agents())}")
            player_name = input()
            player = self.get_free_player(player_name)
            if player is None:
                print(f"{player_name} you choose is not in the free agents list and is not created or added to the free agents list.")
                return f"{player_name}"

            print(team.sign_player_as_free_agent(player))
            self.free_agents_pool.remove(player)

        elif answer == "buy_player":
            print("Please choose a team from where you want to buy the player")
            print(self.print_team_names_in_the_league())
            team_name = input()
            team_to_sell = self.find_club(team_name)
            if not team:
                return f"{team_name} is not in the league"

            print(self.print_player_to_interact_with_message())
            print(team_to_sell.show_squad())
            player_name = input()
            player = self.get_buy_player(player_name)
            if not player:
                return self.print_message_the_player_is_not_in_the_league_teams(player_name)

            print(team.buy_player(player))
            team_to_sell.players.remove(player)
            team_to_sell.finances += player.transfer_fee

        elif answer == "sell_player":
            print(self.print_player_to_interact_with_message())
            print(self.chosen_team.show_squad())
            player_name = input()
            print("Please select a club where you want to sell the player")
            print(self.print_team_names_in_the_league())
            second_club_name = input()
            club_player_to_be_sold = self.find_club(second_club_name)

            if not club_player_to_be_sold:
                return f"The team you chose is not in the League. Please choose from {self.print_team_names_in_the_league()}"

            player = self.get_buy_player(player_name)
            if not player:
                return self.print_message_the_player_is_not_in_the_league_teams(player_name)
            print(team.sell_player(player, club_player_to_be_sold))
            team.finances += player.transfer_fee

        elif answer == "release_player":
            print(self.print_player_to_interact_with_message())
            print(self.chosen_team.show_squad())
            player_name = input()
            player = self.get_buy_player(player_name)
            if not player:
                return self.print_message_the_player_is_not_in_the_league_teams(player_name)
            print(team.release_player(player))
            if player.player_club is None:
                self.free_agents_pool.append(player)

        elif answer == "change_player_transfer_fee":
            print(self.print_player_to_interact_with_message())
            print(self.chosen_team.show_squad())
            player_name = input()
            player = self.get_buy_player(player_name)
            if not player:
                return self.print_message_the_player_is_not_in_the_league_teams(player_name)
            print(team.change_player_transfer_fee(player))

        elif answer == "change_player_salary":
            print(self.print_player_to_interact_with_message())
            print(self.chosen_team.show_squad())
            player_name = input()
            player = self.get_buy_player(player_name)
            if not player:
                return self.print_message_the_player_is_not_in_the_league_teams(player_name)
            print(team.change_player_salary(player))

        elif "coach" in answer:
            print("Please choose a coach name to interact with")
            print(self.show_available_coaches())
            coach_name = input()
            print(f"Please choose from the possible answer: {', '.join(self.possible_answers)}")
            while answer not in self.possible_answers:
                print(f"Please choose from the possible answer: {', '.join(self.possible_answers)}")

            if answer == "sign_coach":
                coach = self.get_coach(coach_name, team)
                if not coach:
                    return f"{coach_name} you choose is not in the coaches slot. Coach do not exist."
                print(team.sign_coach(coach))

            elif answer == "release_coach":
                coach = self.get_coach(coach_name, team)
                if not coach:
                    return f"{coach_name} you choose is not in the coaches slot. Coach do not exist."
                print(team.release_coach(coach))

        elif "squad" in answer:
            print(team.show_squad())

        elif answer == "check_financial_status":
            print(team.check_financial_status())

        elif answer == "message_for_team_strength":
            print(team.message_for_team_strength)

        elif answer == "print_all_teams_strengths":
            print(self.print_all_teams_strengths())

    @staticmethod
    def print_round_fixtures(weekly_round, week_number):
        data = f"Weekly Fixtures -"
        data += f"Week {week_number} games are as follows: " + '\n' + '\n'
        for team1, team2 in weekly_round:
            data += f"{team1.name} vs {team2.name}" + '\n'
        data += '\n'
        return data

    def print_all_teams_strengths(self):
        data = ""
        sorted_teams = sorted(self.teams, key=lambda x: -x.calculate_team_strength)
        for count, team in enumerate(sorted_teams, 1):
            data += f"{count} -> {team.message_for_team_strength}" + '\n' + '\n'
        return data

    def print_season_fixtures(self):
        data = "Below are all season matches upcoming:" + '\n' + '\n'
        for outer in range(len(self.rounds)):
            data += f"{outer + 1} Round Games: "
            for inner in self.rounds[outer]:
                data += inner[0].name + ' -- '
                data += inner[1].name + ', '
            data += '\n' + '\n'
        return data

    @staticmethod
    def _calculate_percent_chance_random():
        percent = choice(range(1, 3))
        return percent

    @property
    def generate_result_first_team_win(self):
        while True:
            home_goals = choice(range(1, 6))
            away_goals = choice(range(1, 6))
            if home_goals > away_goals:
                return home_goals, away_goals

    @property
    def generate_result_second_team_win(self):
        while True:
            home_goals = choice(range(1, 6))
            away_goals = choice(range(1, 6))
            if away_goals > home_goals:
                return away_goals, home_goals

    @property
    def generate_result_for_draw(self):
        while True:
            home_goals = choice(range(1, 6))
            away_goals = choice(range(1, 6))
            if away_goals == home_goals:
                return away_goals, home_goals

    def fill_in_the_dict_after_match_if_first_team_won(self, team_one, team_two, team_one_goals, team_two_goals):
        self.standings_dict[team_one.name]['games played'] += 1
        self.standings_dict[team_one.name]["team goals"] += team_one_goals
        self.standings_dict[team_one.name]["goals conceded"] += team_two_goals
        self.standings_dict[team_one.name]["wins"] += 1
        self.standings_dict[team_one.name]["loses"] += 0
        self.standings_dict[team_one.name]["draws"] += 0
        self.standings_dict[team_one.name]["points"] += League.points_for_win

        self.standings_dict[team_two.name]['games played'] += 1
        self.standings_dict[team_two.name]["team goals"] += team_two_goals
        self.standings_dict[team_two.name]["goals conceded"] += team_one_goals
        self.standings_dict[team_two.name]["wins"] += 0
        self.standings_dict[team_two.name]["loses"] += 1
        self.standings_dict[team_two.name]["draws"] += 0
        self.standings_dict[team_two.name]["points"] += 0

        return self.standings_dict
        # TODO -> complete the method to enter the goals after every game, depending on the winner

    def fill_in_the_dict_after_match_if_second_team_won(self, team_one, team_two, team_one_goals, team_two_goals):
        self.standings_dict[team_two.name]['games played'] += 1
        self.standings_dict[team_two.name]["team goals"] += team_two_goals
        self.standings_dict[team_two.name]["goals conceded"] += team_one_goals
        self.standings_dict[team_two.name]["wins"] += 1
        self.standings_dict[team_two.name]["loses"] += 0
        self.standings_dict[team_two.name]["draws"] += 0
        self.standings_dict[team_two.name]["points"] += League.points_for_win

        self.standings_dict[team_one.name]['games played'] += 1
        self.standings_dict[team_one.name]["team goals"] += team_one_goals
        self.standings_dict[team_one.name]["goals conceded"] += team_two_goals
        self.standings_dict[team_one.name]["wins"] += 0
        self.standings_dict[team_one.name]["loses"] += 1
        self.standings_dict[team_one.name]["draws"] += 0
        self.standings_dict[team_one.name]["points"] += 0

        return self.standings_dict

    def fill_in_the_dict_after_match_if_match_ended_draw(self,team_one, team_two, team_one_goals, team_two_goals):
        self.standings_dict[team_one.name]['games played'] += 1
        self.standings_dict[team_one.name]["team goals"] += team_one_goals
        self.standings_dict[team_one.name]["goals conceded"] += team_two_goals
        self.standings_dict[team_one.name]["wins"] += 0
        self.standings_dict[team_one.name]["loses"] += 0
        self.standings_dict[team_one.name]["draws"] += 1
        self.standings_dict[team_one.name]["points"] += League.points_for_draw

        self.standings_dict[team_two.name]['games played'] += 1
        self.standings_dict[team_two.name]["team goals"] += team_two_goals
        self.standings_dict[team_two.name]["goals conceded"] += team_one_goals
        self.standings_dict[team_two.name]["wins"] += 0
        self.standings_dict[team_two.name]["loses"] += 0
        self.standings_dict[team_two.name]["draws"] += 1
        self.standings_dict[team_two.name]["points"] += League.points_for_draw

        return self.standings_dict

    # TODO add method if a I want to make a transfers or want to change th coach ot whatever
    def print_free_agents(self):
        data = []
        for player in self.free_agents_pool:
            data.append(player.name)
        data.append('\n')
        return data

    def check_if_team_is_in_the_league(self, team_name):
        for team in self.teams:
            if team_name == team.name:
                return True
        return False

    def print_team_names_in_the_league(self):
        data = "" + '\n'
        for index, team in enumerate(self.teams, 1):
            data += str(index)
            data += ' -> '
            data += team.name + '\n'
        return data + '\n'

    def print_standings_dict(self):
        index = 1
        data = ""
        if self.week_number == League.final_week:
            data += "Final League standings:" + '\n'
        else:
            data += f"Week - {self.week_number} standings as follows: " + '\n'

        for team in sorted(self.standings_dict.items(), key=lambda x: (-x[1]["points"], -x[1]['team goals'])):
            data += f"{index}: {team[0]}: Games played: {team[1]['games played']}, Goals scored: {team[1]['team goals']}, Goals conceded: {team[1]['goals conceded']}," \
                    f" Wins: {team[1]['wins']}, Draws: {team[1]['draws']}, Loses: {team[1]['loses']}, Overall points: {team[1]['points']}" + '\n'
            index += 1
        return data


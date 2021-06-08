from random import choice

CORRECT_CHOICES = ["stone", "scissor", "paper"]


print("Hello to the game: Rock, Paper, Scissors")
print("Player one, please insert your name: ")
player_one_name = input()
print("Player two, please insert your name: ")
player_two_name = input()

end_of_game = False
winner = None

games_played = 0
player_one_wins = 0
player_two_wins = 0
draws = 0


def check_if_weapon_is_valid(weapon):
    if weapon in CORRECT_CHOICES:
        return True
    return False


def player_choice_message(player_one_or_two):
    print(f"{player_one_or_two}, please choose a weapon from stone, scissor or paper!")


def check_if_the_battle_ends_with_draw(player_one_choice, player_two_choice):
    if player_one_choice == player_two_choice:
        return True
    return False


def draw_message():
    print("The battle ended with a draw!")


def check_the_winner(player_one_choice, player_two_choice, battle_winner):
    if player_one_choice == "scissor" and player_two_choice == "paper":
        battle_winner = player_one_name
    elif player_one_choice == "stone" and player_two_choice == "scissor":
        battle_winner = player_one_name
    elif player_one_choice == "paper" and player_two_choice == "stone":
        battle_winner = player_one_name
    else:
        battle_winner = player_two_name
    return battle_winner


def winner_message(player_name):
    print(f"{player_name} wins the battle!")


def message_do_you_want_another_game():
    print("Do yuo want another game? Y or N")


def print_player_two_random_choice(chioce):
    print(chioce)


def end_message(player_one_name, player_two_name, batle_winner):
    print(f"The game between {player_one_name} ad {player_two_name} has ended!")
    print(f"The winner is {batle_winner}!")
    print(f"They played {player_one_wins + player_two_wins + draws} total games" + '\n' 
          f"{player_one_name} won {player_one_wins}, {player_two_name} won {player_two_wins}," f"Draw games are {draws}")


while not end_of_game:
    player_choice_message(player_one_name)
    player_one_choice = input()

    while not check_if_weapon_is_valid(player_one_choice):
        player_choice_message(player_one_name)
        input()

    player_choice_message(player_two_name)
    player_two_choice = choice(CORRECT_CHOICES)
    print_player_two_random_choice(player_two_choice)

    if check_if_the_battle_ends_with_draw(player_one_choice, player_two_choice):
        draws += 1
        draw_message()
        message_do_you_want_another_game()
        Y_or_N = input()

        while Y_or_N not in ["Y", "N"]:
            message_do_you_want_another_game()
            Y_or_N = input()

        if Y_or_N == "N":
            end_of_game = True
            break
        else:
            continue

    winner = check_the_winner(player_one_choice, player_two_choice, winner)
    if winner == player_one_name:
        player_one_wins += 1
        winner_message(player_one_name)
    else:
        player_two_wins += 1
        winner_message(player_two_name)

    message_do_you_want_another_game()
    Y_or_N = input()

    while Y_or_N not in ["Y", "N"]:
        message_do_you_want_another_game()
        Y_or_N = input()

    if Y_or_N == "N":
        end_of_game = True
        break


end_message(player_one_name, player_two_name, winner)

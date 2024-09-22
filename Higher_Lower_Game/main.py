from art import logo, vs
from game_data import data
import random

print(logo)
print("Welcome to the Higher and Lower game! \n")


def choose():
    return random.choice(data)


def compare(select_data, answer):
    a = select_data['A']['follower_count']
    b = select_data['B']['follower_count']
    if a > b and answer == 'A':
        return True
    elif a < b and answer == 'B':
        return True
    else:
        return False


def game():
    com = {
        'A': choose(),
        'B': choose()
    }
    game_on = True
    score = 0

    while game_on:
        print(f"Compare A : {com['A']['name']} is a {com['A']['description']} from {com['A']['country']}.")
        print(vs)
        print(f"Against B : {com['B']['name']} is a {com['B']['description']} from {com['B']['country']}.\n")

        player_answer = input("Who has more followers : A or B : ").upper()

        if compare(com, player_answer):
            score += 1
            print(f"\nYou are right. CURRENT SCORE : {score}\n")
        else:
            print("\nThat's wrong answer. Game over.\n")
            game_on = False

        com['A'] = com['B']
        com['B'] = choose()


game()

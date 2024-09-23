import random

print("Welcome to the Number Guessing game !")


def chose_number():
    number = random.randint(1, 101)
    return number


def difficulty_level():
    attempts_left = 10
    level = input("Choose the difficulty level. 'easy' or 'hard' : ").lower()

    if level == "hard":
        attempts_left = 5

    return attempts_left


# def check_answer(chosen_number, user):
#     if chosen_number < user:
#         return "Too low"
#     elif chosen_number > user:
#         return "Too high"
#     elif chosen_number == user:
#         return "You win"
game_on = True
lives = difficulty_level()
number = chose_number()
while game_on:
    player = int(input(f"You have {lives} attempts left. Guess a number : "))
    # check = check_answer(chose_number(), player)
    if player > number:
        print("Your answer is too high.")
        lives -= 1
    elif player < number:
        print("Your answer is too low.")
        lives -= 1
    elif player == number:
        print("You have won")
        game_on = False

    if lives == 0:
        print(f"The answer is {number}. You lost.")
        game_on = False

print("Goodbye!")

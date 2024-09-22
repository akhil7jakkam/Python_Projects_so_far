import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards_list):
    if sum( cards_list) == 21 and len(cards_list) == 2:
        return 0

    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose"
    elif user_score == 0:
        return "you win"
    elif user_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   your cards :{user_cards}, current score : {user_score}")
        print(f"   computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            if input("Do you want to draw another card ? yes or no : ").lower() == 'yes':
                user_cards.append(deal_card())
            else:
                game_over = True

        computer_score = calculate_score(computer_cards)

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"   your cards :{user_cards}, current score : {user_score}")
        print(f"   computer's cards : {computer_cards}, computer score : {computer_score}")

        print(compare(user_score, computer_score))


play_game()
while input("Do you want to play another game ? yes or no : ").lower() == "yes":
    play_game()

print("Goodbye!")

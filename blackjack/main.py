import random
from art import logo, ace, king, queen, jack, ten, nine, eight, seven, six, five, four, three, two


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def check_cards(card):
    list = [king, queen, jack, ten]
    if card == 11:
        return ace
    elif card == 2:
        return two
    elif card == 3:
        return three
    elif card == 4:
        return four
    elif card == 5:
        return five
    elif card == 6:
        return six
    elif card == 7:
        return seven
    elif card == 8:
        return eight
    elif card == 9:
        return nine
    elif card == 10:
        return random.choice(list)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(" Your cards: ")
        for i in user_cards:
            card = check_cards(i)
            print(f"{card}", sep='')
        print(f"current score: {user_score}")

        for i in computer_cards:
            ai_card = check_cards(i)
        print(f"   Computer's first card: {ai_card}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: ")
    for i in user_cards:
        card = check_cards(i)
        print(f"{card}")
    print(f"final score: {user_score}")
    print(f" Computer's final hand: ")
    for i in computer_cards:
        ai_card = check_cards(i)
        print(ai_card)
    print(f"final score: {computer_score}")
    print(f"Your score : {user_score} VS {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

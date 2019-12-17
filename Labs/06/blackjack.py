import random
import statistics
import itertools

NUM_DECKS = 4
STARTING_MONEY = 0
NUM_HANDS = 1000
BET_SIZE = 1
VERBOSE = 0
DEALER_HITS_BELOW = 17
PLAYER_STRATEGIES = [15, 16, 17, 18, 19]
NUM_PLAYERS = len(PLAYER_STRATEGIES)


def generate_deck():
    """
    generates a deck of cards, as a list of tuples, where each tuple is a card. Each tuple contains three elements:
     01) the card's suit, 02) it's symbol, 03) and it's value. The function also uses the NUM_DECKS constant, stating
     how many 52-card decks are combined.
    :return: the deck, a shuffled list of tuples
    """
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    symbols = ['Ace', 'King', 'Queen', "Jack", '10', '09', '08', '07', '06', '05', '04', '03', '02']
    values = [0, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    deck = []
    for i in range(NUM_DECKS):
        for suit in suits:
            for j in range(len(symbols)):
                deck.append((symbols[j], suit, values[j]))
    random.shuffle(deck)
    return deck


def generate_players():
    """
    generates a list of players. The number of players is determined by the length of the list constant
    PLAYER_STRATEGIES. Each player is a list containing two elements: 01) their starting money (determined
    by the constant STARTING_MONEY), and their strategy (one of the list elements of PLAYER_STRATEGIES. Their strategy
    is just a number specifying the number below which the player is still willing to take a "hit."
    :return: the player list, a list of lists specifying the player's bank and strategy
    """
    player_list = []

    for i in range(NUM_PLAYERS):
        bank = STARTING_MONEY
        strategy = PLAYER_STRATEGIES[i]  # this is the number below which the player is still willing to 'hit'
        player_list.append([bank, strategy])

    return player_list


def calculate_all_hand_values_list(card_list):
    """
    generates a list of the different values of that hand. It must be a list, because aces can be worth either
    01 or 11 points. This means that each hand as 02^n number of different possible values, where n is the number of
    aces in the hand.
    :param card_list: the list of cards in the hand
    :return: the list of values that the hand is worth.
    """
    non_ace_value = 0
    num_aces = 0

    for card in card_list:
        if card[0] == 'Ace':
            num_aces += 1
        else:
            non_ace_value += card[2]

    num_values = 2 ** num_aces
    value_list = []

    for ace_values in itertools.product([1, 11], repeat=num_aces):
        ace_sum = 0
        for ace_value in ace_values:
            ace_sum += ace_value
        value_list.append(ace_sum)

    for i in range(num_values):
        value_list[i] += non_ace_value

    return value_list


def calculate_hand_best_score(card_list):
    """
    calculates a hand's best score. if the hand has aces, it determines the highest non-bust score. If all the scores
    are BUST (over 21), it returns a mean of all of the BUST hands.
    :param card_list: the cards in the hand
    :return: the best score of the hand
    """
    value_list = calculate_all_hand_values_list(card_list)
    final_score = 0
    for score in value_list:
        if score < 22:
            if score > final_score:
                final_score = score
    if final_score == 0:
        final_score = statistics.mean(value_list)
    return final_score


def get_player_result(deck, name, player_cards, player_strategy, dealer_up):
    """
    takes a player's starting two cards, and plays the hand according to their strategy, until they have either elected
    to stay, or have gone bust
    :param deck: the current remaining cards in the shuffled deck
    :param name: the name of the player
    :param player_cards: the cards in the player's hand
    :param player_strategy: the strategy of the player
    :param dealer_up: the card that the dealer has face up
    :return: the remaining cards in the deck, and the final hand of the player
    """
    if VERBOSE:
        print_hand(name, player_cards)

    done = False
    while not done:
        hand_value_list = calculate_all_hand_values_list(player_cards)
        max_value = 0
        for value in hand_value_list:
            if value < 22:
                if value > max_value:
                    max_value = value
        if max_value == 0:
            done = True
            if VERBOSE:
                print("    {} is bust.".format(name))

        elif max_value >= player_strategy:
            done = True
            if VERBOSE:
                print("    {} stays.".format(name))
        else:
            new_card, deck = deal_card(deck)
            player_cards.append(new_card)

            if VERBOSE:
                print("    {} hits. Gets {} of {}".format(name, new_card[0], new_card[1]))
                print_hand(name, player_cards)
    return deck, player_cards


def get_dealer_result(deck, dealer_cards):
    """
    takes the dealer's starting two cards, and plays the hand according to the specified DEALER_HITS_BELOW constant,
    until the dealer has either stayed or gone bust.
    :param deck: the current remaining cards in the shuffled deck
    :param dealer_cards: the cards in the dealer's hand
    :return: the remaining cards in the deck, and the final hand of the dealer
    """
    if VERBOSE:
        print_hand("\n    Dealer", dealer_cards)

    done = False
    while not done:
        hand_value_list = calculate_all_hand_values_list(dealer_cards)
        max_value = 0
        for value in hand_value_list:
            if value < 22:
                if value > max_value:
                    max_value = value
        if max_value == 0:
            done = True
            if VERBOSE:
                print("    Dealer is bust.")

        elif max_value >= DEALER_HITS_BELOW:
            done = True
            if VERBOSE:
                print("    Dealer stays.")
        else:
            new_card, deck = deal_card(deck)
            dealer_cards.append(new_card)

            if VERBOSE:
                print("    Dealer hits. Gets {} of {}".format(new_card[0], new_card[1]))
                print_hand("Dealer", dealer_cards)

    return deck, dealer_cards


def deal_card(deck):
    """
    checks to make sure there are still cards in the deck. If so, deals a new card. if not, gets a new shuffled deck,
    and tehn deals a single card.
    :param deck: the remaining cards in the shuffled deck before the card is dealt
    :return: the dealt card, and the remaining cards in the shuffled deck after the card is dealt
    """
    if len(deck) == 0:
        deck = generate_deck()
    card = deck.pop()
    return card, deck


def determine_winners(dealer_hand, player_list, player_hand_list):
    """
    for each player, calculates who wins the hand (the dealer or the player) according to standard casino rules.
    :param dealer_hand: the cards in the dealer's final hand
    :param player_list: a list of the players, so that we can adjust their money
    :param player_hand_list: a list of lists, where each sublist is the cards in each player's hand
    :return: the list of players, after having adjusted their money
    """

    dealer_score = calculate_hand_best_score(dealer_hand)

    if VERBOSE:
        print("\n    Results:")
        print("        Dealer final score {}\n".format(dealer_score))

    for i in range(NUM_PLAYERS):
        player_hand = player_hand_list[i]
        player_score = calculate_hand_best_score(player_hand)
        if VERBOSE:
            print("        Player {} final score {}".format(str(i+1), player_score))

        if player_score > 21:
            player_list[i][0] -= BET_SIZE
            if VERBOSE:
                print("        Player {} bust. Player -${}".format(str(i + 1), BET_SIZE))
        else:
            if dealer_score > 21:
                player_list[i][0] += BET_SIZE
                if VERBOSE:
                    print("        Dealer bust. Player {} +${}".format(str(i + 1), BET_SIZE))
            else:
                if player_score == 21:
                    if dealer_score < 21:
                        if len(dealer_hand) > 2:
                            player_list[i][0] += BET_SIZE*1.5
                            if VERBOSE:
                                print("        Player {} Blackjack! +${}".format(str(i + 1), BET_SIZE*1.5))
                else:
                    if player_score > dealer_score:
                        player_list[i][0] += BET_SIZE
                        if VERBOSE:
                            print("        Player {} +${}".format(str(i + 1), BET_SIZE))
                    elif player_score < dealer_score:
                        player_list[i][0] -= BET_SIZE
                        if VERBOSE:
                            print("        Player {} -${}".format(str(i + 1), BET_SIZE))
                    elif player_score == dealer_score:
                        if VERBOSE:
                            print("        Player {} Ties.".format(str(i + 1)))
                        else:
                            pass
        if VERBOSE:
            print("")
    return player_list


def print_hand(name, hand):
    """
    prints to the screen the values of a hand, and all the cards in a hand
    :param name: the name of the hand's owner
    :param hand: the list of cards in the hand
    :return: None
    """
    value_list = calculate_all_hand_values_list(hand)
    value_output_string = '/'.join(str(x) for x in value_list)
    hand_output_string = ""
    for card in hand:
        hand_output_string = hand_output_string + card[0] + " of " + card[1] + ", "
    hand_output_string = hand_output_string[:-2]
    print("    {} has {} ({})".format(name, value_output_string, hand_output_string))


def play_hand(deck, player_list):
    """
    plays the hand by first dealing to the dealer, then to each player. Then each player plays their hand, then the
    dealer plays their hand, and then the winners are determined.
    :param deck: the remaining cards in the shuffled deck
    :param player_list: the list of players (containing their money and strategy)
    :return: the remaining cards in the shuffled deck, and the updated player list
    """
    player_hand_list = []

    dealer_up, deck = deal_card(deck)
    dealer_down, deck = deal_card(deck)
    dealer_hand = [dealer_up, dealer_down]

    if VERBOSE:
        symbol = dealer_up[0]
        suit = dealer_up[1]
        print("    Dealer Shows {} of {}\n".format(symbol, suit))

    for i in range(NUM_PLAYERS):
        player_hand = []
        for j in range(2):
            new_card, deck = deal_card(deck)
            player_hand.append(new_card)
        player_hand_list.append(player_hand)

    for i in range(NUM_PLAYERS):
        player_hand = player_hand_list[i]
        player_strategy = player_list[i][1]
        name = "Player " + str(i+1)
        deck, player_hand = get_player_result(deck, name, player_hand, player_strategy, dealer_up)
        player_hand_list[i] = player_hand

    deck, dealer_hand = get_dealer_result(deck, dealer_hand)

    player_list = determine_winners(dealer_hand, player_list, player_hand_list)

    return deck, player_list


def play_session(deck, player_list):
    """
    Plays the number of hands specified in NUM_HANDS. Outputs progress if VERBOSE=01
    :param deck:
    :param player_list:
    :return: the remaining cards in the shuffled deck, and the player_list reflecting updated money
    """
    print("Let's Play Blackjack!")
    for i in range(NUM_HANDS):
        if i % 100 == 0:
            print(" Playing hand {}".format(str(i+1)))

        if VERBOSE:
            print("Hand {}\n".format(i+1))
        deck, player_list = play_hand(deck, player_list)

    return deck, player_list


def output_final_results(player_list):
    """
    print the final results to the screen, showing each player's strategy and how much money they have won or lost
    :param player_list:
    :return:
    """
    print("\nFinal Results After {} Hands:".format(NUM_HANDS))
    for i in range(NUM_PLAYERS):
        strategy = player_list[i][1]
        result = player_list[i][0]
        print("    Player {}:    Strategy: {}    Result: ${}".format(str(i+1), strategy, result))
    print("\n")


def main():
    deck = generate_deck()
    player_list = generate_players()
    deck, player_list = play_session(deck, player_list)
    output_final_results(player_list)


main()

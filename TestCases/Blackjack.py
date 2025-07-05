import random

points = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def hand_score(hand):
    total = sum([points.get(card, card) for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

def shuffle_cards():
    deck = (['J', 'Q', 'K', 'A'] + list(range(2, 11))) * 4
    random.shuffle(deck)
    return iter(deck)

def player_turn(up_cards, cards, strategy, deck):
    if hand_score(cards) <= 21 and strategy(up_cards, cards):
        cards.append(next(deck))

def dealer_turn(cards, deck):
    while hand_score(cards) < 17:
        cards.append(next(deck))

def blackjack(strategy, announce = print):
    deck = shuffle_cards()

    player_cards = [next(deck)]
    up_cards = next(deck)
    player_cards.append(next(deck))
    hole_cards = next(deck)

    player_turn(up_cards=up_cards, cards=player_cards,strategy=strategy, deck=deck)

    if hand_score(player_cards) > 21:
        announce("player goes bust with", player_cards, "against a", up_cards)
        return -1

    dealer_cards = [up_cards, hole_cards]
    dealer_turn(dealer_cards, deck=deck)
    if hand_score(dealer_cards) > 21:
        announce("player goes bust with", dealer_cards)
        return 1
    else:
        announce('Player has', hand_score(player_cards), "and dealer has", hand_score(dealer_cards))
        diff = hand_score(player_cards) - hand_score(dealer_cards)
        return max(-1, min(1, diff))

def basic_strategy(upcards, cards):
    if hand_score(cards) <= 11:
        return True
    if upcards in [2, 3, 4, 5, 6]:
        return False
    return hand_score(cards) < 17

def ssh(*args):
    ... # do something else instead of print

def gamble(strategy, hands = 1000):
    return sum([blackjack(strategy=strategy, announce=ssh) for _ in range(hands)])

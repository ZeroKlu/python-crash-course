"""Blackjack"""

import sys
from random import shuffle

HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
BACKSIDE = "backside"
BANKROLL = 5_000

def show_rules():
    """Display the game rules"""
    print("Blackjack")
    print("Rules:")
    print("  Try to get as close to 21 without going over.")
    print("  Kings, Queens, and Jacks are worth 10 points.")
    print("  Aces are worth 1 or 11 points.")
    print("  Cards 2 through 10 are worth their face value.")
    print("  (H)it to take another card.")
    print("  (S)tand to stop taking cards.")
    print("  On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.")
    print("  In case of a tie, the bet is returned to the player.")
    print("  The dealer stops hitting at 17.")

def place_bet(max_bet):
    """Allow user to place a bet"""
    while True:
        print(f"How much do you want to bet? (1 - {max_bet}, or [q]uit)")
        bet = input("> ")
        if bet == "": continue
        if not bet.isdecimal():
            if bet.lower().startswith("q"): game_over(False)
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet: return bet
        continue

def game_over(lost):
    """Close out the game"""
    if lost: print("You're broke!\nGood thing you weren't playing with real money.")
    print("Thanks for playing!")
    sys.exit()

def get_deck():
    """Generate a 52-card deck"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    shuffle(deck)
    return deck

def hand_value(hand):
    """Return the value of the cards in the hand"""
    value = 0
    aces = 0

    for card in hand:
        rank = card[0]
        if rank == "A": aces += 1
        elif rank in ["K", "Q", "J"]: value += 10
        else: value += int(rank)
    
    value += aces
    for _ in range(aces):
        if value + 10 <= 21: value += 10
    
    return value

def show_cards(hand):
    """Display all cards in the hand"""
    rows = ["", "", "", "", ""]
    for _, card in enumerate(hand):
        rows[0] += " ___  "
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "
    for row in rows: print(row)

def show_hands(player_hand, dealer_hand, show_dealer_hand):
    """Display the current hands"""
    print()
    if show_dealer_hand:
        print("DEALER", hand_value(dealer_hand))
        show_cards(dealer_hand)
    else:
        print("DEALER: ???")
        show_cards([BACKSIDE] + dealer_hand[1:])
    print("PLAYER:", hand_value(player_hand))
    show_cards(player_hand)

def play(money):
    """Play the game"""
    while True:
        if money < 1: game_over(True)

        print(f"You have ${money} remaining...")
        bet = place_bet(money)

        deck = get_deck()

        dealer_hand = []
        player_hand = []
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
            
        print(f"Bet: ${bet}")
        while True:
            show_hands(player_hand, dealer_hand, False)
            print()

            if hand_value(player_hand) > 21: break

            move = play_turn(player_hand, money - bet, bet)

            if move == "D":
                bet += place_bet(min(bet, money - bet))
                print(f"Bet increased to ${bet}")
                print(f"Bet: ${bet}")
            if move in ["H", "D"]:
                player_hand.append(deck.pop())
                rank, suit = player_hand[-1]
                print(f"You drew a {rank} of {suit}.")
                if hand_value(player_hand) > 21: continue
            if move in ["S", "D"]: break

        if hand_value(player_hand) <= 21:
            while hand_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                show_hands(player_hand, dealer_hand, False)
                if hand_value(dealer_hand) > 21: break
            input("Press <ENTER> to continue...")
            print("\n\n")

        show_hands(player_hand, dealer_hand, True)

        player_value = hand_value(player_hand)
        dealer_value = hand_value(dealer_hand)

        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif player_value > 21 or player_value < dealer_value:
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You won ${bet}!")
            money += bet
        else:
            print("It's a tie. Your bet is returned.")
            
        input("Press <ENTER> to continue...")
        print("\n\n")

def play_turn(hand, money, bet):
    """Get player move"""
    while True:
        moves = ["[H]it", "[S]tand"]
        if len(hand) == 2 and money >= bet: moves.append("[D]ouble down")
        move = input(", ".join(moves) + "\n> ").upper()
        if move != "" and (move[0] in ["H", "S"] or (len(moves) > 2 and move[0] == "D")): return move
        print("Invalid entry...")

def main():
    """Main Program"""
    show_rules()
    money = BANKROLL
    play(money)

if __name__ == "__main__":
    """Only run if not imported"""
    main()

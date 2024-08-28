from deck import Deck
from hand import Hand
from ranks import Ranks
from colors import Colors
import sys
from sm_utils import clear_terminal

class Blackjack(object):
    """Models a game of blackjack"""

    INITIAL_BANKROLL = 5_000

    def __init__(self, color: Colors=Colors.WHITE) -> None:
        """Initialize"""
        self.game = "blackjack"
        self.color = color
        self.deck: Deck = None
        self.player_hands: list[Hand] = None
        self.dealer_hand: Hand = None
        self.player_bankroll: int
        self.reset_bankroll()

    def play(self) -> None:
        """Play a game of blackjack"""
        while True:
            if self.player_bankroll < 1:
                self.game_over(True)
            self.play_hand()
            break

    def play_hand(self) -> None:
        """Play one hand of blackjack"""
        bet = self.place_bet()

    def place_bet(self) -> int:
        """Let the player place a bet"""
        while True:
            clear_terminal()
            print(f"You have ${self.player_bankroll:,} remaining...\n")
            print(f"How much do you want to bet? (1 - {self.player_bankroll:,}, or [q]uit)")
            entry = input("> ")
            if entry is None or entry == "":
                continue
            if not entry.isdigit():
                if entry[0].lower() == "q":
                    self.game_over()
                continue
            bet = int(entry)
            if 1 <= bet <= self.player_bankroll:
                return bet

    def deal_hand(self):
        """Deal the initial two cards to the dealer and player"""
        if self.deck is None or len(self.deck.cards) < 10:
            self.deck = Deck(self.game, self.color)
        self.player_hands, self.dealer_hand = [Hand(self.game)], Hand(self.game, cards=[])
        for _ in range(2):
            for hand in [self.player_hands[0], self.dealer_hand]:
                self.deck.deal(hand, 1)
        self.dealer_hand.hidden = [1]

    def reset_bankroll(self):
        """Reset the player's bankroll back to the default value"""
        self.player_bankroll = Blackjack.INITIAL_BANKROLL

    def show_rules(self) -> None:
        """Display the blackjack rules"""
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

    def game_over(self, lost: bool=False) -> None:
        """Close out the game"""
        if lost:
            print("You're broke!\nGood thing you weren't playing with real money.")
        print("Thanks for playing!")
        sys.exit(0)

    def hand_value(self, hand: Hand) -> int:
        """Get the value of the given hand"""
        val = hand.value
        for _ in range(hand.count(Ranks.ACE)):
            if val <= 11:
                val += 10
        return val

    def show_hands(self):
        print(f"Dealer: {self.hand_value(self.dealer_hand)}{' + ??' if self.dealer_hand.hidden else ''}")
        self.dealer_hand.show()
        p_val = self.hand_value(self.player_hand)
        print(f"\nPlayer: {p_val}", end="")
        if p_val > 21:
            print(" (Busted!)")
        elif p_val == 21 and len(self.player_hand.cards) == 2: #TODO
            print(" (Blackjack!)")
        else:
            print()
        self.player_hand.show()
        print()

def main() -> None:
    Blackjack().play()

if __name__ == "__main__":
    main()

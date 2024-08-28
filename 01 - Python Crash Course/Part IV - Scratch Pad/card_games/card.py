from colors import Colors
from suits import Suits
from ranks import Ranks
import json

class Card(object):
    """Models a playing card"""

    def __init__(self, game: str=None, suit: Suits=None, rank: Ranks=None, color: Colors=Colors.WHITE, back: bool=False) -> None:
        """Initialize"""
        self.suit: Suits = Suits.SPADES if back else suit
        self.rank: Ranks = Ranks.BACK if back else rank
        self.color: Colors = color
        self.value: int = self.get_value(game)
        self.glyph: str = Ranks.glyph(self.rank, self.suit)
        self.ascii: list[str] = self.get_ascii()
        self.name: str = self.get_name()

    def __str__(self) -> str:
        """String representation of the card"""
        return "#" if self.rank == Ranks.BACK else f"{Ranks.initial(self.rank)}{Suits.glyph(self.suit, self.color)}"
    
    def __repr__(self) -> str:
        """Return a string for replication of the card"""
        return json.dumps({
            "rank": Ranks.name(self.rank),
            "suit": Suits.name(self.suit)
        }, indent=4)

    def get_name(self):
        """Get the long name for the card"""
        return "Back" if self.rank == Ranks.BACK else f"{Ranks.name(self.rank)} of {Suits.name(self.suit)}"

    def get_value(self, game: str) -> int:
        """Get the value of the card"""
        if game is None or game == "":
            return self.rank.value
        match game.lower():
            # TODO: Add support for more games
            case "blackjack":
                return self.rank.value if self.rank.value < 11 else 10
            case "poker":
                return 14 if self.rank.value == 1 else self.rank.value
            case _:
                return self.rank.value

    def get_ascii(self) -> list[str]:
        """Get list of strings representing rows to draw card as ASCII art"""
        rows = [" ___ "]
        rank = Ranks.initial(self.rank)
        suit = Suits.glyph(self.suit, self.color)
        back = self.rank == Ranks.BACK
        rows.append(f"|{'## ' if back else f'{rank:<2} '}|")
        rows.append(f"|{'###' if back else f' {suit} '}|")
        rows.append(f"|{'_##' if back else f'_{rank:_>2}'}|")
        return rows

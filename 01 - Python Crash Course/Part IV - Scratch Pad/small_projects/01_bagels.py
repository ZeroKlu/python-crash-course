from random import randint

class Bagels(object):
    """The Bagels Game"""

    def __init__(self, num_digits: int=3, num_guesses: int=10, debug: bool=False) -> None:
        """Initialize"""
        self.debug = debug
        self.num_digits = num_digits
        self.num_guesses = num_guesses
        self.first_game = True

    def play(self) -> None:
        """Start a new game"""
        self.secret_number = [randint(0, 9) for _ in range(3)]
        if self.first_game:
            self.print_instructions()
        self.do_game()

    def print_instructions(self) -> None:
        """Display the game instructions"""
        Utilities.clear_terminal()
        print("Welcome to Bagels!")
        print(f"I am thinking of a {self.num_digits}-digit number with no repeated digits.")
        print(f"Try to guess what it is in {self.num_guesses} guesses. Here are some clues:")
        print("When I say:    That means:")
        print("    Pico         One digit is correct but in the wrong position.")
        print("    Fermi        One digit is correct and in the right position.")
        print("    Bagels       No digit is correct.")
        print("---------------------------------------------------------------")
        Utilities.pause()
        self.first_game = False

    def do_game(self) -> None:
        """Play the game"""
        turn = 0
        guess = []
        while turn < self.num_guesses:
            guess = self.get_guess(turn)
            won = self.display_result(guess)
            if won:
                print("You won!")
                break
            Utilities.pause()
            turn += 1
        self.conclude_game(won)

    def conclude_game(self, won: bool) -> None:
        """Finish the game"""
        if not won:
            Utilities.clear_terminal()
            print("Sorry. You lost this time.")
            for i in range(self.num_digits):
                self.secret_number[i] = str(self.secret_number[i])
            print(f"The secret number was {''.join(self.secret_number)}")
        play_again = input("\nWould you like to play again? [Y|N]:\n> ")
        if play_again is not None and len(play_again) > 0 and play_again[0].lower() == "y":
            self.play()
        else:
            Utilities.clear_terminal()
            print("\nThanks for playing! Good bye.\n")

    def get_guess(self, turn: int) -> list[int]:
        """Enter a guess"""
        num = None
        while num is None or not num.isdigit() or len(num) != self.num_digits:
            Utilities.clear_terminal()
            if num is not None:
                print("Invalid entry!")
            if self.debug: print(self.secret_number)
            print(f"Guesses remaining [{self.num_guesses - turn}]")
            num = input(f"Enter a {self.num_digits}-digit number:\n> ")
        return [int(num[i]) for i in range(self.num_digits)]

    def display_result(self, guess: list[int]) -> bool:
        """Show the results of the guess"""
        fermi = self.locate_fermi(guess)
        pico = self.locate_pico(guess, fermi)
        if sum(pico) == -1 * self.num_digits and sum(fermi) == -1 * self.num_digits:
            print("Bagels!")
            return False
        print("Fermi " * (self.num_digits - fermi.count(-1)), end="")
        print("Pico " * (self.num_digits - pico.count(-1)))
        return fermi.count(-1) == 0

    def locate_fermi(self, guess: list[int]) -> list[int]:
        """Find right numbers at right positions"""
        fermi = [-1] * self.num_digits
        for i in range(self.num_digits):
            # A digit in the guess counts as a fermi if and only if
            #    The same digit appears in the same position in the secret number
            if guess[i] == self.secret_number[i]:
                # I am placing the actual number in the list (rather than a bool) to help subsequent pico finds
                fermi[i] = guess[i]
        return fermi

    def locate_pico(self, guess: list[int], fermi: list[int]) -> list[int]:
        """Find right numbers at wrong positions"""
        pico = [-1] * self.num_digits
        for i in range(self.num_digits):
            # A digit in the guess counts as a pico if and only if
            # 1. The digit appears in the secret number
            # 2. That position isn't already a fermi
            # 3. The total number of fermis and picos for the digit is no greater than
            #    the number of times that the digit appears in the secret number
            if guess[i] in self.secret_number \
                and fermi[i] != guess[i] \
                and (fermi + pico).count(guess[i]) < self.secret_number.count(guess[i]):
                pico[i] = guess[i]
        return pico

class Utilities(object):
    """Utility Functions"""

    @staticmethod
    def pause(end: bool = False) -> None:
        """Wait for user input"""
        act = "end program" if end else "continue"
        input(f"Press <ENTER> to {act}...")
        if end: quit()

    @staticmethod
    def clear_terminal(end: str="") -> None:
        """Clear the terminal"""
        print("\033c", end=end)

def main() -> None:
    """Main process"""
    game = Bagels()
    game.play()

if __name__ == "__main__":
    main()

"""Test Rochambeau (Rock, Paper, Scissors) Game"""

from rock_paper_scissors import RockPaperScissors

def main():
    """Start the game"""
    # Check whether to use strategy
    user_options = ["y", "n"]
    user_input = input("Should the computer use a strategy? (Y|N)\n> ")
    if user_input != "":
        user_input = user_input[0].lower()
    use_strategy = None if user_input not in user_options else user_input == "y"

    # Create and start the game
    game = RockPaperScissors(use_strategy)
    game.play()

if __name__ == "__main__":
    main()

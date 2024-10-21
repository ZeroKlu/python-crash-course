"""Rochambeau (Rock, Paper, Scissors) Game"""

from random import getrandbits, choice

class RockPaperScissors:
    """Defines a Rochambeau Game"""

    def __init__(self, use_strategy = None, debug_mode = False):
        """Initialize global variables"""

        # If the calling program did not set a strategy, use the
        # "win-stay, lose-shift" strategy 50% of games
        self.use_strategy = self.coin_flip() if use_strategy is None else use_strategy

        # Game data
        self.available_actions = ["r", "p", "s", "q"]
        self.names = {"r": "rock", "p": "paper", "s": "scissors"}
        self.loses_to = {"r": "s", "p": "r", "s": "p"}
        self.beats = {"r": "p", "p": "s", "s": "r"}
        self.player_action = ""
        self.last_player_action = None
        self.last_computer_action = None
        self.last_result = "ties"

        # Greet the player once
        print("Welcome to Rochambeau (Rock, Paper, Scissors)!")

        if debug_mode:
            mid = "" if self.use_strategy else "not "
            print(f"Computer is {mid}using strategy.\n")

    def coin_flip(self):
        """Return a 50/50 true | false"""
        return bool(getrandbits(1))

    def random_choice(self):
        """Choose an action at random"""
        return choice(self.available_actions[:3])

    def strategic_choice(self):
        """Choose action based on the win-stay, lose-shift strategy"""
        if self.last_result[0] == "w":
            # A player after losing has a higher likelihood of shifting to
            #   the action that would have beaten the computer's last play
            # So the computer's strategic action is to play whatever would
            #   beat whatever would beat the computer's last action
            computer_action = self.beats[self.beats[self.last_computer_action]]
        elif self.last_result[0] == "l":
            # A player after winning has a higher likelihood of staying with
            #   the same action on the next turn
            # So the computer's strategic action is to play whatever would
            #   beat the player's last action
            computer_action = self.beats[self.last_player_action]
        else:
            # On the first play of the game or following a tie, choose an
            #   action at random
            computer_action = self.random_choice()
        return computer_action

    def turn(self, player_action):
        """Play a turn"""
        # Determine the computer's action based on whether or not
        #   strategy is active
        computer_action = self.strategic_choice() if self.use_strategy \
            else self.random_choice()

        # Stash the actions in order to plot the next strategic move
        self.last_player_action = player_action
        self.last_computer_action = computer_action

        # Determine who wins and stash the result
        if computer_action == player_action:
            self.last_result = "ties"
        elif self.loses_to[computer_action] == player_action:
            self.last_result = "wins"
        else:
            self.last_result = "loses"

        # Print the result of the turn
        print(f"Computer chooses {self.names[computer_action]} and {self.last_result}\n")

    def play(self):
        """Play the game"""

        # Continue play until the user quits
        while True:
            # Clear the player action
            player_action = None

            # Obtain an action from the player and verify that it is in
            # the list of available actions
            while player_action not in self.available_actions:
                player_action = \
                    input("Enter your choice: ([r]ock, [p]aper, [s]cissors, [q]uit\n> ")
                if player_action in ("", None):
                    continue
                player_action = player_action[0].lower()

            # If the player's response starts with "q", end the game
            if player_action == "q":
                break

            # Otherwise, play the turn using the player's chosen action
            self.turn(player_action)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()

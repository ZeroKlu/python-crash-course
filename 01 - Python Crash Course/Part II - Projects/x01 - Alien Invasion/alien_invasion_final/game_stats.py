import os
import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        ROOT_DIR = os.path.dirname(__file__)
        file_name = "hi_score.json"
        self.hi_score_file = os.path.join(ROOT_DIR, file_name)

        self.high_score = self.get_high_score()
        
    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self) -> int:
        """Retrieve the high score from JSON file"""
        try:
            with open(self.hi_score_file) as file:
                return int(json.load(file))
        except:
            return 0

    def set_high_score(self) -> None:
        """Write the high score to JSON file"""
        with open(self.hi_score_file, "w") as file:
            json.dump(str(self.high_score), file)
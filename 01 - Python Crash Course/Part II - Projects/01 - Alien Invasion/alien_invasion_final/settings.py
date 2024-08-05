class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (180, 0, 0)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.difficulty_level = 1.0
        self.difficulty_modifier = 0.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, difficulty_level: float=1.0) -> None:
        """Initialize settings that change throughout the game."""
        self.difficulty_level = difficulty_level

        self.ship_speed = 1.0
        if self.difficulty_level < 1:
            self.ship_speed /= self.difficulty_level
        self.bullet_speed = 3.0 / self.difficulty_level
        self.alien_speed = 0.5 * self.difficulty_level

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = int(50 * self.difficulty_level)

    def increase_speed(self) -> None:
        """Increase speed settings."""
        self.bullet_speed *= self.speedup_scale * self.difficulty_level
        self.alien_speed *= self.speedup_scale * self.difficulty_level
        self.alien_points = int(self.alien_points * self.score_scale * self.difficulty_level)

import os

class Settings:
    """ A class to store the Star Field settings """

    def __init__(self):
        """ Initialize all settings """

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Star Settings
        ROOT_DIR = os.path.dirname(__file__)
        file_name = "star.bmp"
        self.star_file_path = os.path.join(ROOT_DIR, "images", file_name)
        print(self.star_file_path)
        self.num_stars = 100

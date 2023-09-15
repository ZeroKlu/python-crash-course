class Settings():
    """ A class to store the Rain Shower settings """

    def __init__(self):
        """ Initialize all settings """

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Raindrop Settings
        self.rain_img_lg = "rain_l.png"
        self.rain_img_med = "rain_m.png"
        self.rain_img_sm = "rain_s.png"
        self.num_raindrops = 200

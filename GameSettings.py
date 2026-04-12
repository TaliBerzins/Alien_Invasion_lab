from pathlib import Path

"""Alien Invasion settings temlpate
Tali Berzins
File defines the settings applied to the Alien Invasion game
Started code is from professor Gabriel Walters tutorials
04/12/2026 """

class Settings:
    """Defines the settings for the game

    Attributes:
    name: Name of the game
    screen_w: screen width
    screen_h: screen height
    FPS : frames per second the game runs on
    bg_file : the background images used for the game
    laser_sound: the laser sound for the game
    ship_w: width of the ship
    ship_h: height of the ship
    ship_file: ship img file used
    bullet_file: bullet image file used
    bullet_w: bullet width
    bullet_h: bullet height
    bullet_amount: bullet amount
    
    """

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd()/'Assets'/'images'/'Starbasesnow.png'
        self.ship_file = Path.cwd()/'Assets'/'images'/'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 80

        self.bullet_file = Path.cwd()/'Assets'/'images'/ 'laserBlast.png'
        self.laser_sound = Path.cwd()/'Assets'/'sound'/ 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5
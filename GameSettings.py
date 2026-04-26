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
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'
        

        self.bullet_file = Path.cwd()/'Assets'/'images'/ 'laserBlast.png'
        self.laser_sound = Path.cwd()/'Assets'/'sound'/ 'laser.mp3'
        self.impact_sound = Path.cwd()/'Assets'/'sound'/ 'impactSound.mp3'



        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
       
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1
      

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        
    def initialize_dyanmic_settings(self):
          self.fleet_sideways_speed = 5
          self.bullet_speed = 10
          self.alien_bullet_speed = 5
          self.starting_ship_count = 1
          self.fleet_speed = 3
          self.fleet_drop_speed = 2
          self.bullet_w = 25
          self.bullet_h = 80
          self.bullet_amount = 20
          self.ship_speed = 3
          self.alien_points = 50


    def increase_difficulty(self):
         self.ship_speed *= self.difficulty_scale
         self.bullet_speed *= self.difficulty_scale
         self.fleet_speed *= self.difficulty_scale

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

"""Alien Invasion Ship file
Tali Berzins
File defines the template for the ships movement.
Started code is from professor Gabriel Walters tutorials
04/12/2026 """

class Ship:
    """Defines the object ship

    Attributes: self.game : 
    self
    self.game : Defines the game that the ship will be used on
        self.settings : Defines the settings for the ships movement
        self.screen : Defines the screen the ship will display on
        self.screen_rect : 
        self.image : Defines the image used for the ship
        self.rect : Defines the rectanlge used to reference its position
        self.rect.midbottom : Defines the starting point of the rectangle
          that will be used to reference its position
        self.moving_right : Defines state of ship moving right to true/false
        self.moving_left : Defines state of ship moving left to true/false
        self.x : Defines the position of the ship
        self.arsenal : Defines the arsenal (bullet type and amount of bullets) for the ship

    """

    #Initalizer Method
    def __init__ (self, game: 'AlienInvasion', arsenal : 'Arsenal'):

        """Sets up the initial values for the attributes of ship class"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
                (self.settings.ship_w,self.settings.ship_h)
                )
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal


    def update(self):
        """Updates the position of the ship and its arsenal"""
        #updating position of the ship
        self.update_ship_movement()
        self.arsenal.update_arsenal()

    def update_ship_movement(self):
        """Updates the ships and its rectangles 
        position according to its speed """
        temp_speed = 5
        if self.moving_right:
            self.x += temp_speed
        if self.moving_left:
            self.x-=temp_speed
        
        self.rect.x = self.x
        
    def draw(self):
        """Draws the ship at the top left corner of the rectangle
        as defined by self.rect"""
        self.arsenal.draw()
        self.screen.blit(self.image,self.rect)

    def fire(self):
        """Fires a bullet when called
        Returns self.arsenal.fire_bullete() which can be true 
        or false depending on if a bullet can be fired or not
        """
        return self.arsenal.fire_bullet()

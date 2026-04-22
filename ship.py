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
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
                (self.settings.ship_w,self.settings.ship_h)
                )
        self.original_image = pygame.image.load(self.settings.ship_file)
        self.original_image = pygame.transform.scale(self.image,
                (self.settings.ship_w,self.settings.ship_h)
                )
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.y_rect = float(self.rect.y)
        self.arsenal = arsenal
        self.ship_location = 0

    def _center_ship(self):
        self.rotate_ship(0)
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
        self.y_rect = float(self.rect.y)


    def update(self):
        """Updates the position of the ship and its arsenal"""
        #updating position of the ship
        self.update_ship_movement()
        self.arsenal.update_arsenal()

    def update_ship_movement(self):
        """Updates the ships and its rectangles 
        position according to its speed """
        temp_speed = 5

        #Conditions for moving right
       
        if self.moving_right and self.x>0 and self.y_rect == 720 and self.x<1160 and self.rect.width != 80:
            self.x+=temp_speed

        if self.moving_right and self.x>=1160 and self.y_rect == 720 and self.rect.width == 40:
            self.rotate_ship(90)
            self.y_rect+= 35
            self.x-= 40
            self.ship_location = 1
        if self.moving_right and self.x == 1120 and self.y_rect!= 0 and self.rect.width == 80:
            self.y_rect-= temp_speed

        if self.moving_right and self.y_rect <= 0 and self.x == 1120 and self.rect.width == 80:
            self.rotate_ship(180)
            self.x += 40
            self.ship_location = 2
        if self.moving_right and self.y_rect == 0 and self.x != 0:
            self.x -= temp_speed

        if self.moving_right and self.x <= 0 and self.y_rect == 0:
            self.rotate_ship(-90)
            self.y_rect += temp_speed
            self.ship_location = 3
        if self.moving_right and self.x == 0 and self.y_rect != 0:
            self.y_rect += temp_speed

        if self.moving_right and self.y_rect >= 760:
            self.rotate_ship(0)
            self.x += temp_speed
            self.y_rect-= 40
            self.ship_location = 0
        

        

        #Conditions for user moving left
        if self.moving_left and 1160>self.x>0 and self.y_rect == 720 and self.rect.width == 40 :
            self.x-=temp_speed
            
        if self.moving_left and self.x<=0 and self.y_rect == 720 and self.rect.width == 40:
            self.rotate_ship(-90)
            self.y_rect+=35
            self.ship_location = 3
        if self.moving_left and self.y_rect<= 760 and self.y_rect != 0 and self.x == 0:
            self.y_rect-= temp_speed

        if self.moving_left and self.y_rect <= 0 and self.x == 0:
            self.rotate_ship(180)
            self.x += temp_speed
            self.ship_location = 2
        if self.moving_left and self.y_rect == 0 and self.x != 0:
            self.x += temp_speed

        if self.moving_left and self.x >= 1160 and self.y_rect == 0:
            self.rotate_ship(90)
            self.y_rect += temp_speed
            self.x -= 40
            self.ship_location = 1
        if self.moving_left and self.x == 1120 and self.y_rect != 0 and self.rect.width ==80:
            self.y_rect += temp_speed

        if self.moving_left and self.y_rect >= 760:
            self.rotate_ship(0)
            self.x += 35
            self.y_rect-= 40
            self.ship_location = 0
            


        self.rect.x = self.x
        self.rect.y = self.y_rect
        
    def draw(self):
        """Draws the ship at the top left corner of the rectangle
        as defined by self.rect as well as its arsenal"""
        self.arsenal.draw()
        self.screen.blit(self.image,self.rect)

    def fire(self):
        """Fires a bullet when called
        Returns self.arsenal.fire_bullete() which can be true 
        or false depending on if a bullet can be fired or not
        """
        return self.arsenal.fire_bullet()
    
    def rotate_ship(self,angle):
        
            self.image = pygame.transform.rotate(self.original_image,angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image,self.rect)

    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
    
    # def ship_play_status(self):
    #     if self.rect.x == 0:
    #         ship_status = left
    #     elif self.rect.x  == 1120 and self.rect.y == 




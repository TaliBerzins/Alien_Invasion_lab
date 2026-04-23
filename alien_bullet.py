import pygame
from pygame.sprite import Sprite
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from alien_invasion import AlienInvasion

"""ship Invasion Bullets template
Tali Berzins
File defines the methods for firing bullets from the ship in
ship Invasion game
Started code is from professor Gabriel Walters tutorials
04/12/2026 """



class AlienBullet(Sprite):
     """Defines the speed and positioning of bullets

     Attributes:
     rect.midtop: The center of the top of the ship
     that is used as the reference for where the bullet will fire from
     rect: the rectangle used to reference the position
     of the bullet
     y: the current position of the bullet
     """
     def __init__(self, game: 'AlienInvasion', x: int , y: int):
          """
          Defines the initial statuso f the bullet class
          including its vertical position and image
          """
          super().__init__()
          self.game = game
          self.screen = game.screen
          self.settings = game.settings

          self.image = pygame.image.load(self.settings.bullet_file)
          self.image = pygame.transform.scale(self.image,
                (self.settings.bullet_w,self.settings.bullet_h)
                )
          self.original_image = pygame.image.load(self.settings.bullet_file)
          self.original_image = pygame.transform.scale(self.image,
                (self.settings.bullet_w,self.settings.bullet_h)
                )
          self.rect = self.image.get_rect()
          self.rect.midtop = x,y
          
          
          self.y = float(self.rect.y)
          self.x = float(self.rect.x)
          self.already_rotated = False
          self.first_shot_instance = 0
          




         

     def draw_bullet(self):
          """Draws the bullet at its respective position"""
          if self.game.ship.rect.y == 720 and self.game.ship.rect.width == 40 and self.already_rotated == False :
               self.rotate_bullet(0)
               self.already_rotated = True
               self.first_shot_instance = 1
          elif self.game.ship.rect.width == 80 and self.game.ship.rect.x == 0 and self.already_rotated == False :
               self.rotate_bullet(-90)
               self.already_rotated = True 
               self.first_shot_instance = 2
          elif self.game.ship.rect.width == 80 and self.game.ship.rect.x == 1120 and self.already_rotated == False :
               self.rotate_bullet(90)
               self.already_rotated = True 
               self.first_shot_instance = 3
               

          elif self.game.ship.rect.width == 40 and self.game.ship.rect.y == 0 and self.already_rotated == False :
               self.rotate_bullet(180)
               self.already_rotated = True 
               self.first_shot_instance = 4
          
          self.screen.blit(self.image,self.rect)

     def update(self):
          """
          Updates the bullets position based on its speed"""
          if self.first_shot_instance == 1:
               self.y += self.settings.bullet_speed
               self.rect.y = self.y
               
          
          elif self.first_shot_instance == 2:
               self.x -= self.settings.bullet_speed
               self.rect.x = self.x
          
          elif self.first_shot_instance == 3:
               self.x += self.settings.bullet_speed
               self.rect.x = self.x

          elif self.first_shot_instance == 4:
               self.y -= self.settings.bullet_speed
               self.rect.y = self.y

     
     def rotate_bullet(self,angle):
        
            self.image = pygame.transform.rotate(self.original_image,angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            
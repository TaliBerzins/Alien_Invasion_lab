import pygame
from alien_bullet import AlienBullet
from typing import TYPE_CHECKING


"""Alien Invasion alien_Arsenal template
Tali Berzins
File defines the methods for defining the number of bullets left with the 
ship in Alien Invasion game
Started code is from professor Gabriel Walters tutorials
04/12/2026 """


if TYPE_CHECKING:
     from alien_invasion import AlienInvasion
     

class AlienArsenal:
     """
     Defines the "alien_arsenal" of screen bullet objects as a group

     Attributes:
     alien_arsenal: the group of bullet objects

     """
     def __init__(self, game: 'AlienInvasion'):
          """Initializes the settings and creates the alien_arsenal
          as a group of sprite objects"""
          self.game = game
          self.settings = game.settings
          self.alien_arsenal = pygame.sprite.Group()

     def update_alien_arsenal(self):
          """updates the alien_arsenal and removes bullets from alien_arsenal
          once they go off screen"""
          self.alien_arsenal.update()
          self._remove_bullets_offscreen()
     
     def _remove_bullets_offscreen(self):
          """Removes each bullet that is off screen from alien_arsenal
          """
          for alien_bullet in self.alien_arsenal.copy():
               if alien_bullet.rect.bottom <=0 or alien_bullet.rect.x >= 1200 or alien_bullet.rect.x <= 0 or alien_bullet.rect.y >= 800:

                    self.alien_arsenal.remove(alien_bullet)
            
               


     def draw(self):
          """Draws each bullet in alien_arsenal at its respective position
          """
          for alien_bullet in self.alien_arsenal:
               alien_bullet.draw_bullet()
     
     def fire_bullet(self, x, y):
          """Creates a new bullet object and adds it to the alien_arsenal
          
          Returns True if there is space in alien_arsenal for new bullet"""
          if len(self.alien_arsenal) < self.settings.bullet_amount:
               new_bullet = AlienBullet(self.game, x, y)
               self.alien_arsenal.add(new_bullet)
               return True
          return False 
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING


"""Alien Invasion Arsenal template
Tali Berzins
File defines the methods for defining the number of bullets left with the 
ship in Alien Invasion game
Started code is from professor Gabriel Walters tutorials
04/12/2026 """


if TYPE_CHECKING:
     from alien_invasion import AlienInvasion
     

class Arsenal:
     """
     Defines the "arsenal" of screen bullet objects as a group

     Attributes:
     arsenal: the group of bullet objects

     """
     def __init__(self, game: 'AlienInvasion'):
          """Initializes the settings and creates the arsenal
          as a group of sprite objects"""
          self.game = game
          self.settings = game.settings
          self.arsenal = pygame.sprite.Group()

     def update_arsenal(self):
          """updates the arsenal and removes bullets from arsenal
          once they go off screen"""
          self.arsenal.update()
          self._remove_bullets_offscreen()
     
     def _remove_bullets_offscreen(self):
          """Removes each bullet that is off screen from arsenal
          """
          for bullet in self.arsenal.copy():
               if bullet.rect.bottom <=0 or bullet.rect.x >= 1200 or bullet.rect.x <= 0 or bullet.rect.y >= 800:

                    self.arsenal.remove(bullet)
            
               


     def draw(self):
          """Draws each bullet in arsenal at its respective position
          """
          for bullet in self.arsenal:
               bullet.draw_bullet()
     
     def fire_bullet(self):
          """Creates a new bullet object and adds it to the arsenal
          
          Returns True if there is space in arsenal for new bullet"""
          if len(self.arsenal) < self.settings.bullet_amount:
               new_bullet = Bullet(self.game)
               self.arsenal.add(new_bullet)
               return True
          return False 
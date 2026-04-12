import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from alien_invasion import AlienInvasion

"""Alien Invasion Bullets template
Tali Berzins
File defines the methods for firing bullets from the ship in
Alien Invasion game
Started code is from professor Gabriel Walters tutorials
04/12/2026 """



class Bullet(Sprite):
     """Defines the speed and positioning of bullets

     Attributes:
     rect.midtop: The center of the top of the ship
     that is used as the reference for where the bullet will fire from
     rect: the rectangle used to reference the position
     of the bullet
     y: the current position of the bullet
     """
     def __init__(self, game: 'AlienInvasion'):
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
          self.rect = self.image.get_rect()
          self.rect.midtop = game.ship.rect.midtop
          self.y = float(self.rect.y)

     def update(self):
          """
          Updates the ibullets position based on its speed"""
          self.y -= self.settings.bullet_speed
          self.rect.y = self.y

     def draw_bullet(self):
          """Draws the bullet at its respective position"""
          self.screen.blit(self.image,self.rect)
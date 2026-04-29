import pygame
import random
from pygame.sprite import Sprite

from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from alien_fleet import AlienFleet


"""Alien template
Tali Berzins
File defines the methods for creating and updating an alien object
Started code is from professor Gabriel Walters tutorials
04/26/2026 """

class Alien(Sprite):
     def __init__(self, fleet: 'AlienFleet', x: float, y: float):
          

          """Initializes the classes attributes and objects
          Parameters:
          fleet: Alien fleet is referenced for the alien instance
          x: Aliens horizontal location
          y: Alien vertical location
          Attributes:
          self.original_image: Image is used as the reference for aliens that will be rotated
          so that new rotations don't lose pixels by rotating based on a previously rotated image
          """
          super().__init__()
          
          self.fleet = fleet
          self.screen = fleet.game.screen
          self.boundaries = fleet.game.screen.get_rect()
          self.settings = fleet.game.settings

          self.image = pygame.image.load(self.settings.alien_file)
          self.image = pygame.transform.scale(self.image,
                (self.settings.alien_w,self.settings.alien_h)
                )
          
          self.original_image = pygame.image.load(self.settings.alien_file)
          self.original_image = pygame.transform.scale(self.image,
                (self.settings.alien_w,self.settings.alien_h)
                )
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
          self.y = float(self.rect.y)
          self.x = float(self.rect.x)
          

     def update(self):
        """Updates aliens position based on the fleets speed
        Attributes:
        temp_speed : The speed at which aliens move when they're rotated so that their fleet
        moves either up or down
        side_ways_temp_speed: The speed at which aliens move when they're rotated so that the fleet
        moves eventually to the left or right."""
        
        temp_speed = self.settings.fleet_speed
        side_ways_temp_speed = self.settings.fleet_sideways_speed 

        if self.fleet.ship.ship_location == 0 :
          self.x+=temp_speed * self.fleet.fleet_direction
        elif self.fleet.ship.ship_location == 2:
              self.x-=temp_speed * self.fleet.fleet_direction * -1
        elif self.fleet.ship.ship_location == 1:
              self.y-=side_ways_temp_speed * self.fleet.fleet_direction * -1
        elif self.fleet.ship.ship_location == 3:
              self.y+=side_ways_temp_speed * self.fleet.fleet_direction * -1
        self.rect.x = self.x
        self.rect.y = self.y
  
             

     def check_edges(self):
          """Checks if fleet has reached the edge for its respective rotation"""
          if self.fleet.ship.ship_location == 0 or self.fleet.ship.ship_location == 2:
           return (self.rect.right >= self.boundaries.right or self.rect.left<= self.boundaries.left)
          elif self.fleet.ship.ship_location == 1 or self.fleet.ship.ship_location == 3:
           return (self.rect.bottom >= self.boundaries.bottom or self.rect.top<= self.boundaries.top)
          
          

     
     


     def draw_alien(self, angle):
            """Draws aliens at the angle called"""
            self.image = pygame.transform.rotate(self.original_image,angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.screen.blit(self.image,self.rect)

          
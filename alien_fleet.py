import pygame
import random 
from alien import Alien


from typing import TYPE_CHECKING


if TYPE_CHECKING:
     from alien_invasion import AlienInvasion
     from alien_arsenal import AlienArsenal
     



"""AlienFleet template
Tali Berzins
File defines the methods for creating and updating alien fleets
Started code is from professor Gabriel Walters tutorials
04/26/2026 """
     
     
     
class AlienFleet:
     """Creates alien fleets, updates and draws them according to ship's position.  Removes
     alien objects that go offscreen and updates the score accordingly
     Attributes:
     fleet_direction: The value that defines what direction the alien fleet moves (positive or negatve)
     fleet_drop_speed: How much the alien fleet moves if it hits an edge
     list_of_removed_aliens: List of aliens that go off screen
     alien_position : Position of an alien 
     """


     
     def __init__ (self, game: 'AlienInvasion',  alien_arsenal : 'AlienArsenal'):
          """Initializes alien fleet objects that are later referenced
          Parameters: 
          game: Type: AlienInvasion.  References the alieninvasion game so attributes such as settings
          and objects such as ship can be accessed
          alien_arsenal: Type: AlienArsenal.  Group of bullets assigned to an alien fleet """
          self.game = game
          self.settings = game.settings
          self.boundaries = game.screen.get_rect()
          self.fleet = pygame.sprite.Group()
          self.fleet_direction = self.settings.fleet_direction
          self.fleet_drop_speed = self.settings.fleet_drop_speed
          self.alien_arsenal = alien_arsenal
          self.list_of_removed_aliens = []
         
          
          


          

    
     def create_fleet_2(self):
         """Creates an alien fleet when the ship is rotated to the left side of the screen
         Attributes:
         fleet_w: How many ships fit in one row of the fleet
         fleet_h: How many ships fit in one column of the fleet
         x_offset: Horiztonal space added before the fleet is drawn
         y_offset: Vertical space added before the fleet is drawn"""
         alien_w = self.settings.alien_w
         alien_h = self.settings.alien_h
         screen_h = self.settings.screen_h
         screen_w = self.settings.screen_w
         

         fleet_w , fleet_h= self.calculate_fleet_size_2(alien_w, screen_w, alien_h, screen_h)

         x_offset, y_offset = self.calculate_offset_2(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         self._create_rectangle_fleet_2(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet_2(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
         """Adds aliens to the fleet by the relative position current_x, current_y
          Attributes:
        current_x: The horizontal position of where the alien will be created
        current_y: The vertical position of where the alien will be created
        ran_1, 2, 3, 4: Random numbers generated to leave out alien generations at these random positions
        If current_x or y divided by ran_1 ,2... gives remainder 0, alien won't be created
              """
         num_of_aliens_gen = random.SystemRandom()
         ran_1 = (num_of_aliens_gen.randint(2,10))
         ran_2 = (num_of_aliens_gen.randint(2,10))
         ran_3 = (num_of_aliens_gen.randint(2,10))
         ran_4 = (num_of_aliens_gen.randint(2,10))
         

         for row in range(0,fleet_h,2):
              for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col% 2 == 0 or col % ran_1 == 0 or col % ran_2 == 0 or col % ran_3 == 0 or col % ran_4 == 0:
                    continue
                

                self._create_alien(current_x, current_y)

              ran_1 = (num_of_aliens_gen.randint(2,10))
              ran_2 = (num_of_aliens_gen.randint(2,10))
              ran_3 = (num_of_aliens_gen.randint(2,10))
              ran_4 = (num_of_aliens_gen.randint(2,10))

     def calculate_offset_2(self, alien_w, alien_h, screen_h, fleet_w, fleet_h):
         """Caculates the offset or amount of space before the alien fleet is created both horizontally
         and vertically
         Attributes:
         fleet_horizontal_space: How much space the fleet takes up horizontally
         fleet_vertical_space: How much space the fleet takes up vertically
         """
         full_screen_h = self.settings.screen_h
         full_screen_w = self.settings.screen_w
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         y_offset = ((full_screen_h - fleet_vertical_space)/2)
         x_offset = ((full_screen_w-fleet_horizontal_space))
         return x_offset,y_offset


     def calculate_fleet_size_2(self, alien_w, screen_w, alien_h, screen_h):
         """Calculates how many aliens will be created in the fleet, with fleet_w being
         the number of aliens in a row, and fleet_h being number of aliens in a column
         Attributes: 
         fleet_w : number of aliens in a row
         fleet_h: Number of aliens in a column
         """
         fleet_w = 4
         fleet_h = (screen_h/alien_h)

         if fleet_w % 2 == 0:
              fleet_w -=2
         else:
              fleet_w -=1

         if fleet_h %2 ==0:
              fleet_h -=2
         else:
              fleet_h -=1
        
         return int(fleet_w), int(fleet_h)
     
     def create_fleet_4(self):
         """Creates an alien fleet when the ship is rotated to the right side of the screen
         Attributes:
         fleet_w: How many ships fit in one row of the fleet
         fleet_h: How many ships fit in one column of the fleet
         x_offset: Horiztonal space added before the fleet is drawn
         y_offset: Vertical space added before the fleet is drawn"""
         alien_w = self.settings.alien_w
         alien_h = self.settings.alien_h
         screen_h = self.settings.screen_h
         screen_w = self.settings.screen_w
      

         fleet_w , fleet_h= self.calculate_fleet_size_4(alien_w, screen_w, alien_h, screen_h)

         x_offset, y_offset = self.calculate_offset_4(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         self._create_rectangle_fleet_4(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet_4(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
         """Adds aliens to the fleet by the relative position current_x, current_y
          Attributes:
         current_x: The horizontal position of where the alien will be created
         current_y: The vertical position of where the alien will be created
         ran_1, 2, 3, 4: Random numbers generated to leave out alien generations at these random positions
         If current_x or y divided by ran_1 ,2... gives remainder 0, alien won't be created"""
         
         num_of_aliens_gen = random.SystemRandom()
         ran_1 = (num_of_aliens_gen.randint(2,10))
         ran_2 = (num_of_aliens_gen.randint(2,10))
         ran_3 = (num_of_aliens_gen.randint(2,10))
         ran_4 = (num_of_aliens_gen.randint(2,10))
         

         for row in range(0,fleet_h,2):
              for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + 40
                if col% 2 == 0 or col % ran_1 == 0 or col % ran_2 == 0 or col % ran_3 == 0 or col % ran_4 == 0:
                    continue
                

                self._create_alien(current_x, current_y)

              ran_1 = (num_of_aliens_gen.randint(2,10))
              ran_2 = (num_of_aliens_gen.randint(2,10))
              ran_3 = (num_of_aliens_gen.randint(2,10))
              ran_4 = (num_of_aliens_gen.randint(2,10))

     def calculate_offset_4(self, alien_w, alien_h, screen_h, fleet_w, fleet_h):
         """Caculates the offset or amount of space before the alien fleet is created both horizontally
         and vertically
         Attributes:
         fleet_horizontal_space: How much space the fleet takes up horizontally
         fleet_vertical_space: How much space the fleet takes up vertically
         """
         full_screen_h = self.settings.screen_h
         full_screen_w = self.settings.screen_w
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         y_offset = ((full_screen_h - fleet_vertical_space)/2)
         x_offset = alien_w/2
         return x_offset,y_offset


     def calculate_fleet_size_4(self, alien_w, screen_w, alien_h, screen_h):
         """Adds aliens to the fleet by the relative position current_x, current_y
          Attributes:
        current_x: The horizontal position of where the alien will be created
        current_y: The vertical position of where the alien will be created
        ran_1, 2, 3, 4: Random numbers generated to leave out alien generations at these random positions
        If current_x or y divided by ran_1 ,2... gives remainder 0, alien won't be created
              """
         fleet_w = 4
         fleet_h = (screen_h/alien_h)

         if fleet_w % 2 == 0:
              fleet_w -=2
         else:
              fleet_w -=1

         if fleet_h %2 ==0:
              fleet_h -=2
         else:
              fleet_h -=1
        
         return int(fleet_w), int(fleet_h)
     

     
     def create_fleet_3(self):
         """Creates an alien fleet when the ship is rotated to the top side of the screen
         Attributes:
         fleet_w: How many ships fit in one row of the fleet
         fleet_h: How many ships fit in one column of the fleet
         x_offset: Horiztonal space added before the fleet is drawn
         y_offset: Vertical space added before the fleet is drawn"""
         alien_w = self.settings.alien_w
         alien_h = self.settings.alien_h
         screen_h = self.settings.screen_h
         screen_w = self.settings.screen_w
         self.alien_position = 3

         fleet_w , fleet_h= self.calculate_fleet_size_3(alien_w, screen_w, alien_h, screen_h)

         x_offset, y_offset = self.calculate_offset_3(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         self._create_rectangle_fleet_3(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet_3(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
         """Adds aliens to the fleet by the relative position current_x, current_y
          Attributes:
        current_x: The horizontal position of where the alien will be created
        current_y: The vertical position of where the alien will be created
        ran_1, 2, 3, 4: Random numbers generated to leave out alien generations at these random positions
        If current_x or y divided by ran_1 ,2... gives remainder 0, alien won't be created"""
         num_of_aliens_gen = random.SystemRandom()
         ran_1 = (num_of_aliens_gen.randint(2,10))
         ran_2 = (num_of_aliens_gen.randint(2,10))
         ran_3 = (num_of_aliens_gen.randint(2,10))
         ran_4 = (num_of_aliens_gen.randint(2,10))
         

         for row in range(0,fleet_h,2):
              for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col% 2 == 0 or col % ran_1 == 0 or col % ran_2 == 0 or col % ran_3 == 0 or col % ran_4 == 0:
                    continue
                

                self._create_alien(current_x, current_y)

              ran_1 = (num_of_aliens_gen.randint(2,10))
              ran_2 = (num_of_aliens_gen.randint(2,10))
              ran_3 = (num_of_aliens_gen.randint(2,10))
              ran_4 = (num_of_aliens_gen.randint(2,10))

     def calculate_offset_3(self, alien_w, alien_h, screen_h, fleet_w, fleet_h):
         """Caculates the offset or amount of space before the alien fleet is created both horizontally
         and vertically
         Attributes:
         fleet_horizontal_space: How much space the fleet takes up horizontally
         fleet_vertical_space: How much space the fleet takes up vertically
         """
         full_screen_h = self.settings.screen_h
         full_screen_w = self.settings.screen_w
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         y_offset = int(full_screen_h - fleet_vertical_space)
         x_offset = int((full_screen_w-fleet_horizontal_space)/2)
         return x_offset,y_offset


     def calculate_fleet_size_3(self, alien_w, screen_w, alien_h, screen_h):
         """Calculates how many aliens will be created in the fleet, with fleet_w being
         the number of aliens in a row, and fleet_h being number of aliens in a column
         Attributes: 
         fleet_w : number of aliens in a row
         fleet_h: Number of aliens in a column
         """        
         fleet_w = (screen_w/alien_w)
         fleet_h = 5

         if fleet_w % 2 == 0:
              fleet_w -=2
         else:
              fleet_w -=1

         if fleet_h %2 ==0:
              fleet_h -=2
         else:
              fleet_h -=1
        
         return int(fleet_w), int(fleet_h)
     


         
     def create_fleet(self):
          """Creates an alien fleet when the ship is at the bottom of the screen
         Attributes:
         fleet_w: How many ships fit in one row of the fleet
         fleet_h: How many ships fit in one column of the fleet
         x_offset: Horiztonal space added before the fleet is drawn
         y_offset: Vertical space added before the fleet is drawn"""
          alien_w = self.settings.alien_w
          alien_h = self.settings.alien_h
          screen_h = self.settings.screen_h
          screen_w = self.settings.screen_w
          self.alien_position = 1

          fleet_w , fleet_h= self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

          x_offset, y_offset = self.calculate_offset(alien_w, alien_h, screen_w, fleet_w, fleet_h)
          self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)


     def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
         """Adds aliens to the fleet by the relative position current_x, current_y
          Attributes:
        current_x: The horizontal position of where the alien will be created
        current_y: The vertical position of where the alien will be created
        ran_1, 2, 3, 4: Random numbers generated to leave out alien generations at these random positions
        If current_x or y divided by ran_1 ,2... gives remainder 0, alien won't be created"""
         num_of_aliens_gen = random.SystemRandom()
         ran_1 = (num_of_aliens_gen.randint(2,10))
         ran_2 = (num_of_aliens_gen.randint(2,10))
         ran_3 = (num_of_aliens_gen.randint(2,10))
         ran_4 = (num_of_aliens_gen.randint(2,10))
         

         for row in range(0,fleet_h,2):
              for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col% 2 == 0 or col % ran_1 == 0 or col % ran_2 == 0 or col % ran_3 == 0 or col % ran_4 == 0:
                    continue
                

                self._create_alien(current_x, current_y)

              ran_1 = (num_of_aliens_gen.randint(2,10))
              ran_2 = (num_of_aliens_gen.randint(2,10))
              ran_3 = (num_of_aliens_gen.randint(2,10))
              ran_4 = (num_of_aliens_gen.randint(2,10))
            
               
               



     def calculate_offset(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
         """Caculates the offset or amount of space before the alien fleet is created both horizontally
         and vertically
         Attributes:
         fleet_horizontal_space: How much space the fleet takes up horizontally
         fleet_vertical_space: How much space the fleet takes up vertically
         """
         half_screen = self.settings.screen_h//2
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         x_offset = int((screen_w-fleet_horizontal_space)//2)
         y_offset = int((half_screen-fleet_vertical_space)//2)
         return x_offset,y_offset


     def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
         """Calculates how many aliens will be created in the fleet, with fleet_w being
         the number of aliens in a row, and fleet_h being number of aliens in a column
         Attributes: 
         fleet_w : number of aliens in a row
         fleet_h: Number of aliens in a column
         """        
         fleet_w = (screen_w//alien_w)
         fleet_h = 10

         if fleet_w % 2 == 0:
              fleet_w -=1
         else:
              fleet_w -=2

         if fleet_h %2 ==0:
              fleet_h -=1
         else:
              fleet_h -=2
        
         return int(fleet_w), int(fleet_h)
     
         
     
     
     def _create_alien(self, current_x: int, current_y:int):
          """Creates an alien and adds it to the fleet
          Parameters:
          current_x:Horizontal Position of creation of alien 
          current_y:Vertical position of alien creation"""
          new_alien = Alien(self, current_x, current_y)

          self.fleet.add(new_alien)



     def _drop_alien_fleet(self):
          """Drops the aliens by
          attribute:
          self.fleet_drop_speed: Drop speed which is defined earlier by settings"""
          for alien in self.fleet:
               alien.y += self.fleet_drop_speed

     def _left_alien_fleet(self):
         """Moves aliens to the left according to drop speed
         """
         for alien in self.fleet:
             alien.x-= self.fleet_drop_speed

     def _ascend_alien_fleet(self):
         """Moves aliens up according to drop speed
         """
         for alien in self.fleet:
             alien.y-= self.fleet_drop_speed

     def _right_alien_fleet(self):
         """Moves aliens to the right according to drop speed
         """
         for alien in self.fleet:
             alien.x+= self.fleet_drop_speed

     def _check_fleet_edges(self):
          """Flips the direction aliens in fleet move if they hit an edge based on
          the ships location"""
          alien : Alien
          for alien in self.fleet:
               if alien.check_edges() == True and self.game.ship.ship_location ==0:
                   self._drop_alien_fleet()
                   self.fleet_direction *=-1
                   break
               elif alien.check_edges() == True and self.game.ship.ship_location ==1:
                   self._left_alien_fleet()
                   self.fleet_direction *=-1
                   break
               elif alien.check_edges() == True and self.game.ship.ship_location ==2:
                   self._ascend_alien_fleet()
                   self.fleet_direction *=-1
                   break
               elif alien.check_edges()== True  and self.game.ship.ship_location ==3:
                   self._right_alien_fleet()
                   self.fleet_direction *=-1
                   break

     def check_if_aliens_can_shoot_bottom(self):
         """Checks if an alien in a fleet that is traveling towards the bottom of the screen
         can shoot which depends on if there is an alien in front of 
         its shooting path relative to its current rotation.  If it can shoot a bullet will fire
         from the alien arsena depending on if its location is equal to one of the random values assigned.
         
         Attributes:
         _list_of_aliens_can_shoot : List full of aliens that can shoot
          _ran_x 1, 2 ,3: random values that represent a location at which an alien will shoot if its location
           is equal to the random location """
         _list_of_aliens_can_shoot = []
         _ran_x = random.randrange(0,1201,3)
         _ran_x_2 = random.randrange(0,1201,3)
         _ran_x_3 = random.randrange(0,1201,3)

         
   
         alien : Alien
         _list_alien: Alien
          
         for alien in self.fleet:
            

               if alien in _list_of_aliens_can_shoot:
                    if alien.x == _ran_x or alien.x == _ran_x_2 or alien.x == _ran_x_3:
                       self.alien_arsenal.fire_bullet(alien.rect.x, alien.rect.y) 
                       continue
                    else:
                        continue
                    
               _list_of_aliens_below = self.get_sprites_below(alien)
   
                
               lowest_alien = alien
               for _list_alien in _list_of_aliens_below:
               # Pygame objects typically use a 'rect' for positioning
                 if  _list_alien.rect.y > lowest_alien.rect.y:
                      lowest_alien = _list_alien


               if lowest_alien not in _list_of_aliens_can_shoot:
                   _list_of_aliens_can_shoot.append(lowest_alien)


               if alien in _list_of_aliens_can_shoot:
                if alien.x == _ran_x or alien.x == _ran_x_2 or alien.x == _ran_x_3:
                   self.alien_arsenal.fire_bullet(alien.x, alien.y)






      

     def check_alien_shoots_left(self):
         """Checks if an alien in a fleet that is traveling to the left of the screen
         can shoot which depends on if there is an alien in front of 
         its shooting path relative to its current rotation.  If it can shoot a bullet will fire
         from the alien arsena depending on if its location is equal to one of the random values assigned.
         
         Attributes:
         _list_of_aliens_can_shoot : List full of aliens that can shoot
          _ran_x 1, 2 ,3: random values that represent a location at which an alien will shoot if its location
           is equal to the random location """
         
         _list_of_aliens_can_shoot = []
         _ran_y = random.randrange(0,701,3)
         _ran_y_2 = random.randrange(0,701,3)
         _ran_y_3 = random.randrange(0,701,3)
         _ran_y_4 = random.randrange(0,701,3)
         _ran_y_5 = random.randrange(0,701,3)
        
         
   
         alien : Alien
         _list_alien_1: Alien
         
         
         for alien in self.fleet:
           if alien in _list_of_aliens_can_shoot:
             if alien.y  == _ran_y or alien.y == _ran_y_2 or alien.y == _ran_y_3 or alien.y == _ran_y_4 or alien.y == _ran_y_5:
                self.alien_arsenal.fire_bullet(alien.rect.x, alien.rect.y)
                
                

                continue
             else:
                 continue
                    
           _list_of_aliens_left = self.get_sprites_beside(alien)
     
         
   
                
           leftest_alien = alien
           for _list_alien_1 in _list_of_aliens_left:
               # Pygame objects typically use a 'rect' for positioning
            if  _list_alien_1.rect.x < leftest_alien.rect.x:
               leftest_alien = _list_alien_1
    


           if leftest_alien not in _list_of_aliens_can_shoot:
                  _list_of_aliens_can_shoot.append(leftest_alien)
                 
                 
                  


           if alien in _list_of_aliens_can_shoot:
              if alien.y  == _ran_y or alien.y == _ran_y_2 or alien.y == _ran_y_3 or alien.y == _ran_y_4 or alien.y == _ran_y_5:
                self.alien_arsenal.fire_bullet(alien.x, alien.y)

     def check_alien_shoots_top(self):
         """Checks if an alien in a fleet that is traveling towards the top of the screen
         can shoot which depends on if there is an alien in front of 
         its shooting path relative to its current rotation.  If it can shoot a bullet will fire
         from the alien arsena depending on if its location is equal to one of the random values assigned.
         
         Attributes:
         _list_of_aliens_can_shoot : List full of aliens that can shoot
          _ran_x 1, 2 ,3: random values that represent a location at which an alien will shoot if its location
           is equal to the random location """        
         _list_of_aliens_can_shoot = []
         _ran_x = random.randrange(0,1201,3)
         _ran_x_2 = random.randrange(0,1201,3)
         _ran__3 = random.randrange(0,1201,3)


         
   
         alien : Alien
         _list_alien_2: Alien

         
         for alien in self.fleet:
           if alien in _list_of_aliens_can_shoot:
             if alien.x  == _ran_x or alien.x == _ran_x_2 or alien.x == _ran__3:
                self.alien_arsenal.fire_bullet(alien.rect.x, alien.rect.y)
                continue
             else:
                 continue
                    
           _list_of_aliens_above = self.get_sprites_below(alien)
   
                
           highest_alien = alien
           for _list_alien_2 in _list_of_aliens_above:
               # Pygame objects typically use a 'rect' for positioning
            if  _list_alien_2.rect.y < highest_alien.rect.y:
               highest_alien = _list_alien_2


            if highest_alien not in _list_of_aliens_can_shoot:
                  _list_of_aliens_can_shoot.append(highest_alien)
                  
                  
                  
                  


            if alien in _list_of_aliens_can_shoot:
              if alien.x  == _ran_x or alien.x == _ran_x_2 or alien.x == _ran__3:
                self.alien_arsenal.fire_bullet(alien.x, alien.y)

     def check_alien_shoots_right(self):
         """Checks if an alien in a fleet that is traveling towards the right of the screen
         can shoot which depends on if there is an alien in front of 
         its shooting path relative to its current rotation.  If it can shoot a bullet will fire
         from the alien arsena depending on if its location is equal to one of the random values assigned.
         
         Attributes:
         _list_of_aliens_can_shoot : List full of aliens that can shoot
          _ran_x 1, 2 ,3: random values that represent a location at which an alien will shoot if its location
           is equal to the random location """
         
         _list_of_aliens_can_shoot = []
         _ran_y = random.randrange(0,701,3)
         _ran_y_2 = random.randrange(0,701,3)
         _ran_y_3 = random.randrange(0,701,3)
         _ran_y_4 = random.randrange(0,701,3)
         _ran_y_5 = random.randrange(0,701,3)
   
         
   
         alien : Alien
         _list_alien_3: Alien
         
         for alien in self.fleet:
           if alien in _list_of_aliens_can_shoot:
             if alien.y  == _ran_y or alien.y == _ran_y_2 or alien.y == _ran_y_3 or alien.y == _ran_y_4 or alien.y == _ran_y_5:
                self.alien_arsenal.fire_bullet(alien.rect.x, alien.rect.y)

                continue
             else:
                 continue
                    
           _list_of_aliens_beside = self.get_sprites_beside(alien)
   
                
           rightest_alien = alien
           for _list_alien_3 in _list_of_aliens_beside:
               # Pygame objects typically use a 'rect' for positioning
              if  _list_alien_3.rect.x > rightest_alien.rect.x:
               rightest_alien = _list_alien_3


           if rightest_alien not in _list_of_aliens_can_shoot:
                  _list_of_aliens_can_shoot.append(rightest_alien)
                 
                  


           if alien in _list_of_aliens_can_shoot:
              if alien.y  == _ran_y or alien.y == _ran_y_2 or alien.y == _ran_y_3 or alien.y == _ran_y_4 or alien.y == _ran_y_5:
                self.alien_arsenal.fire_bullet(alien.x, alien.y)
     
     


     def get_sprites_below (self, target_sprite):
            """Gets all the aliens below the alien imported
            Parameters: target_sprite, should be of type alien
            
            Attributes: _same_horizontal: list of aliens in the same horizontal location
            verticaly_aligned: is true when the two aliens being compared are at the same vertical poistion"""
            
            _same_horizontal = []
            other: Alien
            for other in self.fleet:
                if other == target_sprite:
                    continue
                
                # Check if horizontal spans overlap
                verticaly_aligned = (other.rect.left < target_sprite.rect.right and 
                                        other.rect.right > target_sprite.rect.left)               
                
                if verticaly_aligned:
                    _same_horizontal.append(other)
            return _same_horizontal
     def get_sprites_beside(self,target_sprite):
            """Gets all the aliens below the alien imported
            Parameters: target_sprite, should be of type alien
            
            Attributes: _same_vertical: list of aliens in the same vertical location
            horizontally_aligned: is true when the two aliens being compared are at the same horizontal poistion"""
            same_vertical = []
            other: Alien
            for other in self.fleet:
                if other == target_sprite:
                    continue
                
                # Check if horizontal spans overlap
                horizontally_aligned = (other.rect.y == target_sprite.rect.y)               
                
                if horizontally_aligned:
                    same_vertical.append(other)
            return same_vertical
   

                    

    

     

                        

     def update_fleet(self):
          """Updates the fleet by removing aliens that are offscreen and checking
          if it hits an edge.  Updates arsenal accordingly"""
          self._check_fleet_edges()
          self.remove_aliens_offscreen()
          self.fleet.update()
          
          if self.game.ship.ship_location == 0:
            self.check_if_aliens_can_shoot_bottom()
          elif self.game.ship.ship_location == 1:
              self.check_alien_shoots_left()
          elif self.game.ship.ship_location == 2:
              self.check_alien_shoots_top()
          elif self.game.ship.ship_location == 3:
              self.check_alien_shoots_right()
          self.alien_arsenal.update_alien_arsenal()
      

     def draw(self):
          """Draws aliens at their proper rotation"""
          self.alien_arsenal.draw()
          alien: 'Alien'
          for alien in self.fleet:
               if self.game.ship.ship_location == 0:
                 alien.draw_alien(0)
                 self.location = 0 
               elif self.game.ship.ship_location == 1:
                   alien.draw_alien(-90)
                   self.location = 1
               elif self.game.ship.ship_location == 2:
                   alien.draw_alien(180)
                   self.location = 2
               elif self.game.ship.ship_location == 3:
                   alien.draw_alien(90)
                   self.location = 3

               

     def check_collisions(self, other_group):
          """Checks collisions between the fleet object and other sprite group
          Parameters:
          other_group: The group of sprites to check the collisions with
          """
          return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
     
     def remove_aliens_offscreen(self):
          """Removes each alien that is off screen from alien fleet
          """
          
          for alien in self.fleet:
               if alien.x>self.boundaries.right or alien.x<self.boundaries.left\
               or alien.y<self.boundaries.top or alien.y>self.boundaries.bottom:
                     self.fleet.remove(alien)
                     self.game.game_stats.score -= self.settings.alien_points
                     self.game.HUD.update_scores()
                    
                  
     def check_destroyed_status(self):
          """Checks if alien fleet is destroyed
          Returns true if fleet is empty"""
          return not self.fleet
     
               
     def fire(self):
        """Fires a bullet when called
        Returns self.arsenal.fire_bullete() which can be true 
        or false depending on if a bullet can be fired or not
        """
        return self.alien_arsenal.fire_bullet()
     
     # def rotate_fleet(self, angle):
     #      alien: 'Alien'
     #      for alien in self.fleet:
     #        alien.image = pygame.transform.rotate(alien.original.image,angle)
     #        alien.rect = alien.image.get_rect(center=alien.rect.center)
     #        alien.screen.blit(alien.image,alien.rect)

               

               
        
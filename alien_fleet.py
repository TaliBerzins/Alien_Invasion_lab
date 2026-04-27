import pygame
import random 
from alien import Alien


from typing import TYPE_CHECKING


if TYPE_CHECKING:
     from alien_invasion import AlienInvasion
     from alien_arsenal import AlienArsenal
     from ship import Ship
     
     
class AlienFleet:
     
     def __init__ (self, game: 'AlienInvasion',  alien_arsenal : 'AlienArsenal', ship: 'Ship'):
          
          self.game = game
          self.settings = game.settings
          self.fleet = pygame.sprite.Group()
          self.fleet_direction = self.settings.fleet_direction
          self.fleet_drop_speed = self.settings.fleet_drop_speed
          self.alien_arsenal = alien_arsenal
          self.ship = ship
          self.list_of_removed_aliens = []
          self.alien_position = 0
          


          

    
     def create_fleet_2(self):
         alien_w = self.settings.alien_w
         alien_h = self.settings.alien_h
         screen_h = self.settings.screen_h
         screen_w = self.settings.screen_w
         self.alien_position = 1

         fleet_w , fleet_h= self.calculate_fleet_size_2(alien_w, screen_w, alien_h, screen_h)

         x_offset, y_offset = self.calculate_offset_2(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         self._create_rectangle_fleet_2(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet_2(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
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
         full_screen_h = self.settings.screen_h
         full_screen_w = self.settings.screen_w
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         y_offset = ((full_screen_h - fleet_vertical_space)/2)
         x_offset = ((full_screen_w-fleet_horizontal_space))
         return x_offset,y_offset


     def calculate_fleet_size_2(self, alien_w, screen_w, alien_h, screen_h):
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
         alien_w = self.settings.alien_w
         alien_h = self.settings.alien_h
         screen_h = self.settings.screen_h
         screen_w = self.settings.screen_w
         self.alien_position = 4

         fleet_w , fleet_h= self.calculate_fleet_size_4(alien_w, screen_w, alien_h, screen_h)

         x_offset, y_offset = self.calculate_offset_4(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         self._create_rectangle_fleet_4(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet_4(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
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
         full_screen_h = self.settings.screen_h
         full_screen_w = self.settings.screen_w
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         y_offset = ((full_screen_h - fleet_vertical_space)/2)
         x_offset = alien_w/2
         return x_offset,y_offset


     def calculate_fleet_size_4(self, alien_w, screen_w, alien_h, screen_h):
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
         alien_w = self.settings.alien_w
         alien_h = self.settings.alien_h
         screen_h = self.settings.screen_h
         screen_w = self.settings.screen_w
         self.alien_position = 3

         fleet_w , fleet_h= self.calculate_fleet_size_3(alien_w, screen_w, alien_h, screen_h)

         x_offset, y_offset = self.calculate_offset_3(alien_w, alien_h, screen_w, fleet_w, fleet_h)
         self._create_rectangle_fleet_3(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

     def _create_rectangle_fleet_3(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
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
         full_screen_h = self.settings.screen_h
         full_screen_w = self.settings.screen_w
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         y_offset = int(full_screen_h - fleet_vertical_space)
         x_offset = int((full_screen_w-fleet_horizontal_space)/2)
         return x_offset,y_offset


     def calculate_fleet_size_3(self, alien_w, screen_w, alien_h, screen_h):
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
          alien_w = self.settings.alien_w
          alien_h = self.settings.alien_h
          screen_h = self.settings.screen_h
          screen_w = self.settings.screen_w
          self.alien_position = 1

          fleet_w , fleet_h= self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

          x_offset, y_offset = self.calculate_offset(alien_w, alien_h, screen_w, fleet_w, fleet_h)
          self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)


     def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
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
         half_screen = self.settings.screen_h//2
         fleet_horizontal_space = fleet_w * alien_w
         fleet_vertical_space = fleet_h * alien_h
         x_offset = int((screen_w-fleet_horizontal_space)//2)
         y_offset = int((half_screen-fleet_vertical_space)//2)
         return x_offset,y_offset


     def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
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
          new_alien = Alien(self, current_x, current_y)

          self.fleet.add(new_alien)



     def _drop_alien_fleet(self):
          for alien in self.fleet:
               alien.y += self.fleet_drop_speed

     def _left_alien_fleet(self):
         for alien in self.fleet:
             alien.x-= self.fleet_drop_speed

     def _ascend_alien_fleet(self):
         for alien in self.fleet:
             alien.y-= self.fleet_drop_speed

     def _right_alien_fleet(self):
         for alien in self.fleet:
             alien.x+= self.fleet_drop_speed

     def _check_fleet_edges(self):
          alien : Alien
          for alien in self.fleet:
               if alien.check_edges() == True and self.ship.ship_location ==0:
                   self._drop_alien_fleet()
                   self.fleet_direction *=-1
                   break
               elif alien.check_edges() == True and self.ship.ship_location ==1:
                   self._left_alien_fleet()
                   self.fleet_direction *=-1
                   break
               elif alien.check_edges() == True and self.ship.ship_location ==2:
                   self._ascend_alien_fleet()
                   self.fleet_direction *=-1
                   break
               elif alien.check_edges()== True  and self.ship.ship_location ==3:
                   self._right_alien_fleet()
                   self.fleet_direction *=-1
                   break

     def check_if_aliens_can_shoot_bottom(self):
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
          self._check_fleet_edges()
          self.fleet.update()
          if self.ship.ship_location == 0:
            self.check_if_aliens_can_shoot_bottom()
          elif self.ship.ship_location == 1:
              self.check_alien_shoots_left()
          elif self.ship.ship_location == 2:
              self.check_alien_shoots_top()
          elif self.ship.ship_location == 3:
              self.check_alien_shoots_right()
          self.alien_arsenal.update_alien_arsenal()
      

     def draw(self):
          self.alien_arsenal.draw()
          alien: 'Alien'
          for alien in self.fleet:
               if self.ship.ship_location == 0:
                 alien.draw_alien(0)
                 self.location = 0 
               elif self.ship.ship_location == 1:
                   alien.draw_alien(-90)
                   self.location = 1
               elif self.ship.ship_location == 2:
                   alien.draw_alien(180)
                   self.location = 2
               elif self.ship.ship_location == 3:
                   alien.draw_alien(90)
                   self.location = 3

               

     def check_collisions(self, other_group):
          return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
          
     

     def check_fleet_bottom(self):
          alien: Alien
          for alien in self.fleet:
               if alien.rect.bottom >= self.settings.screen_h:
                 return True
          return False
     
     def remove_aliens_offscreen(self):
          """Removes each bullet that is off screen from arsenal
          """
          alien: Alien
          for alien in self.fleet.copy():
               if self.alien_position == 1 and alien.y>= 800:
                     self.fleet.remove(alien)
                     self.list_of_removed_aliens.append(alien)
               if self.alien_position == 2 and alien.x<=0:
                   self.fleet.remove(alien)
                   self.list_of_removed_aliens.append(alien)
               if self.alien_position == 3 and alien.y<=0:
                   self.fleet.remove(alien)
                   self.list_of_removed_aliens.append(alien)   
               if self.alien_position == 4 and alien.x>=1200:
                   self.fleet.remove(alien)
                   self.list_of_removed_aliens.append(alien) 
          return self.list_of_removed_aliens
                  
     def check_destroyed_status(self):
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

               

               
        
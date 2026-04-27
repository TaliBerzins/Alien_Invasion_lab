import sys
import pygame
from GameSettings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from alien_arsenal import AlienArsenal
from hud import HUD
from button import Button
from time import sleep
"""Alien Invasion main game loop
Tali Berzins
File runs the main game loop for the Alien Invasion game.
Started code is from professor Gabriel Walters tutorials
04/12/2026 """

class AlienInvasion:
    """The main game loop as a class

    clock : clock object to define a timer

    """
    def __init__(self):
        """
        Initailizes game settings, screen, background,
        clock, the laser sound, ship object, and fleet group
        
        """

        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dyanmic_settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
           (self.settings.screen_w,self.settings.screen_h))
        
        self.game_stats = GameStats(self)
        self.HUD = HUD(self)

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self,Arsenal(self))
        self.alien_fleet = AlienFleet(self, AlienArsenal(self))
        self.alien_fleet_2 = AlienFleet(self, AlienArsenal(self))
        self.alien_fleet_3 = AlienFleet(self, AlienArsenal(self))
        self.alien_fleet_4 = AlienFleet(self, AlienArsenal(self))
        self.alien_fleet.create_fleet() 
        self.alien_fleet_2.create_fleet_2()
        self.alien_fleet_3.create_fleet_3()
        self.alien_fleet_4.create_fleet_4()
       

        self.play_button = Button(self, 'Play')
        
        self.game_active = False

    def run_game(self):
        """
        Runs the game for
        each tick of the clock.
        Updates ship, fleet, and checks for collisions
        """
        #Game Loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                if self.ship.has_rotated_left:
                  self.alien_fleet_2.update_fleet()
                if self.ship.has_rotated_top:
                  self.alien_fleet_3.update_fleet()
                if self.ship.has_rotated_right:
                  self.alien_fleet_4.update_fleet() 
                self._check_collisions()
                
                


            self._update_screen()
            self.clock.tick(self.settings.FPS)



    def _check_collisions(self):
        """Checks for collisions between the ship and the alien fleets and their 
        respective arsenals.  Updates ship lives and game status
        by calling check game status method.
        Updates the hud and game scores accordingly"""
        #check collisions for ship
        if  self.ship.check_collisions(self.alien_fleet.fleet) or self.ship.check_collisions(self.alien_fleet.alien_arsenal.alien_arsenal):
            self._check_game_status()
        if self.ship.has_rotated_top: 
             if self.ship.check_collisions(self.alien_fleet_3.fleet):
                 self._check_game_status()
                 if self.ship.check_collisions(self.alien_fleet_3.alien_arsenal.alien_arsenal):
                  self.alien_fleet_3.alien_arsenal.alien_arsenal.empty()  
                  self._check_game_status()
        if self.ship.has_rotated_left:
             if self.ship.check_collisions(self.alien_fleet_2.fleet):
                 self._check_game_status()
             if self.ship.check_collisions(self.alien_fleet_2.alien_arsenal.alien_arsenal):
                 self.alien_fleet_2.alien_arsenal.alien_arsenal.empty()  
                 self._check_game_status()
        if self.ship.has_rotated_right:
             if self.ship.check_collisions(self.alien_fleet_4.fleet):
                 self._check_game_status()
                                    
             if self.ship.check_collisions(self.alien_fleet_4.alien_arsenal.alien_arsenal):
                self.alien_fleet_4.alien_arsenal.alien_arsenal.empty()  
                self._check_game_status()




        
            #the alien fleet to reset
            #ship recenter
            #subtract one life
        #check collisions for aliens and bottom of screen
        
        
        #check collisions for projectiles and aliens
        collisions_2 = False
        collisions_3 = False
        collisions_4 = False
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if self.ship.has_rotated_left:
         collisions_2 = self.alien_fleet_2.check_collisions(self.ship.arsenal.arsenal)
        if self.ship.has_rotated_top:
            collisions_3 = self.alien_fleet_3.check_collisions(self.ship.arsenal.arsenal)
        if self.ship.has_rotated_right:
            collisions_4 = self.alien_fleet_4.check_collisions(self.ship.arsenal.arsenal)
        
        
        if collisions or collisions_2 or collisions_3 or collisions_4:
               self.impact_sound.play()
               self.impact_sound.fadeout(250)
               self.game_stats.update(collisions)
               self.HUD.update_scores()




    
        if self.alien_fleet.check_destroyed_status():
            self.game_stats.update_level()
            self.HUD.update_level()
            self._reset_level()
            self.settings.increase_difficulty()

    # def check_ship_rotation(self):
    #     if self.ship.has_rotated_left == True and self.ship.number_of_rotations == 1:
    #          self.alien_fleet_2.create_fleet_2()
    #     elif self.ship.has_rotated_right == True and self.ship.ship_location == 3:
    #          self.alien_fleet_4.create_fleet_4() 

    
    def _check_game_status(self):
        """Updates number of lives left in the game, resets level if number of lives is more than zero
        stops the game is number of lives is less than 0"""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else: self.game_active = False  



    def _reset_level(self):
        """Empties the sprite groups and recreates them"""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.alien_arsenal.alien_arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        """Restarts the game at its level and updates scores, centers ship
        """
        self.settings.initialize_dyanmic_settings()
        self.game_stats.reset_stats()
      
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """
        Updates the screen by drawing ship, alien fleets, HUD
        """


        self.screen.blit(self.bg,(0,0))

        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
         
        
        if self.ship.has_rotated_right:
            self.alien_fleet_4.draw() 
             
            
        if self.ship.has_rotated_left:
            self.alien_fleet_2.draw()  
        

        if self.ship.has_rotated_top:
            self.alien_fleet_3.draw()    
         
                 
        
         
        
        pygame.display.flip()

    def _check_events(self):

        """
        Checks for events such as keyboard quit
        and updates based on if a key is held down or up
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_click()

    def _check_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
            

    def _check_keyup_events(self, event):
        """
        Defines movement of ship if the key event is
        changed to up (if key is released)
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _check_keydown_events(self, event):
        """
        Defines movement of ship and firing of bullets
        for specific keydown events(when a key is held down)
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
             if self.ship.fire():
               self.laser_sound.play()
               self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()

  




if __name__ == '__main__':
    """
    Creates an instance of the game and runs it
    """
    ai = AlienInvasion()
    ai.run_game()


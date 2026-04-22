import sys
import pygame
from GameSettings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from alien_arsenal import AlienArsenal
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
        clock, the laser sound, and ship object
        
        """

        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
           (self.settings.screen_w,self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self,Arsenal(self))
        self.alien_fleet = AlienFleet(self, AlienArsenal(self), self.ship)
        self.alien_fleet.create_fleet() 
        
        self.game_active = True

    def run_game(self):
        """
        Runs the game for
        each tick of the clock
        """
        #Game Loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()


            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet) or self.alien_fleet.check_fleet_bottom():
            
            self._check_game_status()
            #the alien fleet to reset
            #ship recenter
            #subtract one life
        #check collisions for aliens and bottom of screen
        
        
        #check collisions for projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
               self.impact_sound.play()
               self.impact_sound.fadeout(250)
               self.alien_fleet.check_if_aliens_can_shoot()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()


    
    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else: self.game_active = False  



    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()


    def _update_screen(self):
        """
        Updates the screen
        """

        self.screen.blit(self.bg,(0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self):

        """
        Checks for events such as keyboard quit
        and updates based on if a key is held down or up
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            

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
            pygame.quit()
            sys.exit()

  




if __name__ == '__main__':
    """
    Creates an instance of the game and runs it
    """
    ai = AlienInvasion()
    ai.run_game()


import pygame.font
from typing import TYPE_CHECKING


if TYPE_CHECKING:
     from alien_invasion import AlienInvasion

"""HUD template
Tali Berzins
File defines the methods for creating and updating the HUD
Started code is from professor Gabriel Walters tutorials
04/26/2026 """
class HUD:
 

     def __init__(self,game: 'AlienInvasion'):
          """Initializes HUD's attributes and objects
          Attributes:
          self.padding: Adds space in between containers
          """
          self.game = game
          self.settings = game.settings
          self.screen = game.screen
          self.boundaries = game.screen.get_rect()
          self.game_stats = game.game_stats
          self.font = pygame.font.Font(self.settings.font_file,
          self.settings.HUD_font_size)
          self.padding = 20
          self.update_scores()
          self._setup_life_image()
          self.update_level()

     def _setup_life_image(self):
          """Sets up the lives display to show a ships"""
          self.life_image = pygame.image.load(self.settings.ship_file)
          self.life_image = pygame.transform.scale(self.life_image,(
          self.settings.ship_w, self.settings.ship_h))
          self.life_rect = self.life_image.get_rect()



     def update_scores(self):
           """Updates current score, hi score and max score"""
           self._update_score()
           self._update_hi_score()
           self._update_max_score()

     def _update_score(self):
          """Updates the score_str to the game_stats score.
          Renders the score image and draws it at its rectangle position
          Attributes:
          score_str:  String that displays the game stats score
          self.score_img: Renders an image of the score str at its appropriate settings
          """
          score_str = f'Score: {self.game_stats.score: ,.0f}'
          self.score_image = self.font.render(score_str,True,
                                              self.settings.text_color, None)
          self.score_rect = self.score_image.get_rect()
          self.score_rect.right = self.boundaries.right - self.padding
          self.score_rect.top = self.score_rect.bottom + self.padding

     def _update_max_score(self):
          """Updates the max_score_str to the game_stats score.
          Renders the score image and draws it at its rectangle position
          Attributes:
          max_score_str:  String that displays the game stats score
          self.max_score_img: Renders an image of the score str at its appropriate settings
          """
          max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
          self.max_score_image = self.font.render(max_score_str,True,
                                              self.settings.text_color, None)
          self.max_score_rect = self.max_score_image.get_rect()
          self.max_score_rect.right = self.boundaries.right - self.padding
          self.max_score_rect.top = self.padding


     def _update_hi_score(self):
          """Updates the score_str to the game_stats score.
          Renders the score image and draws it at its rectangle position
          Attributes:
          hi_score_str:  String that displays the game stats score
          self.hi_score_img: Renders an image of the score str at its appropriate settings
          """
          hi_score_str = f'Hi-Score: {self.game_stats.hi_score: ,.0f}'
          self.hi_score_image = self.font.render(hi_score_str,True,
                                              self.settings.text_color, None)
          self.hi_score_rect = self.hi_score_image.get_rect()
          self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)


     def update_level(self):
          """Updates the level_str to the game_stats level.
          Renders the level image and draws it at its rectangle position
          Attributes:
          level_str:  String that displays the game stats score
          self.level_image: Renders an image of the score str at its appropriate settings
          """
          level_str = f'Level: {self.game_stats.level: ,.0f}'
          self.level_image = self.font.render(level_str,True,
                                              self.settings.text_color, None)
          self.level_rect = self.level_image.get_rect()
          self.level_rect.left = self.padding
          self.level_rect.top = self.life_rect.bottom + self.padding


     def _draw_lives(self):
          """Draws the life image for the number of ships left from game stats"""
          current_x = self.padding
          current_y = self.padding
          for _ in range(self.game_stats.ships_left):
               self.screen.blit(self.life_image,(current_x, current_y))
               current_x += self.life_rect.width+self.padding


     def draw(self):
          """Draws the hi score, max score, score, and level images and calles the 
          draw live function"""
          self.screen.blit(self.hi_score_image,self.hi_score_rect)
          self.screen.blit(self.max_score_image,self.max_score_rect)
          self.screen.blit(self.score_image,self.score_rect)
          self.screen.blit(self.level_image,self.level_rect)
          self._draw_lives()
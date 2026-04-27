import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

"""Button template
Tali Berzins
File defines the methods for creating and defining button class attributes 
and functions
Started code is from professor Gabriel Walters tutorials
04/26/2026 """


class Button:
    """Initializes class attributes
    Parameters:
    msg: The message that will be displayed by the button"""
    def __init__(self, game: 'AlienInvasion', msg):
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.font = pygame.font.Font(self.settings.font_file,
                                      self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Prepares the message by rendering message to an image with
        a pre-defined font."""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draws the button according to self.settings.button_color.
        Draws the msg in the msg rectangle"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Checks if mouse clicked on the button"""
        return self.rect.collidepoint(mouse_pos)
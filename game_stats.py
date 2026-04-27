from typing import TYPE_CHECKING
from pathlib import Path
import json


if TYPE_CHECKING:
     from alien_invasion import AlienInvasion
"""Button template
Tali Berzins
File defines the methods for creating and defining game stats attributes 
and functions
Started code is from professor Gabriel Walters tutorials
04/26/2026 """
class GameStats():

    def __init__(self, game: 'AlienInvasion'):
        """Initializes game stats attributes.  Initializes saved scores
        and resets stats to zero"""
        
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Loads the scores contents path as a file, and initializes the hi score
        Creates a dictionary named scores that stores the scores
        Attributes:
        scores: dictionary that stores the scores"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            if not contents:
                print('File empty')
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            #save the file

    def save_scores(self):
        """Updates hi score in dictionary to the current hi score.  Dumps 
        the contents scores dictionary and saves it as a string called contents
        then writes contents into the file
        Attributes:
        Scores: Dictionary that stores the current hi score as a value for the  hi_score key 
        Contents: String of the high scores
        """
        scores = {'hi_score': self.hi_score}
        contents = json.dumps(scores, indent = 4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File not found: {e}')
        

    def reset_stats(self):
        """Resets stats for game instance"""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Updates scores for when collisions happen"""
        self._update_score(collisions)

        self._update_max_score()

        self._update_hi_score()
    def _update_max_score(self):
         """Updates the max score
         Attributes:
         self.max_score:  The highest score of the current game session"""
         if self.score> self.max_score:
            self.max_score = self.score
            #update hi_score

    def _update_hi_score(self):
        """Updates the hi score
        self.hi_score: The highest score out of all game sessions"""
        if self.score > self.hi_score:
            self.hi_score = self.score
        

    def _update_score(self, collisions):
        """Updates the current score for the current game session"""
        for alien in collisions.values():
            self.score += self.settings.alien_points
    
 
    
    def update_level(self):
        """Increases the level by one"""
        self.level += 1
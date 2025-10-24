## @module Player
#  Class for the player character

from enum import Enum

import src.controller.controls as controls
import src.game as game
import src.resources as resources
from src.model.GameObject import GameObject


## Various states for the player character
class PlayerState(Enum):
    IDLE = 1
    WALK = 2
    RUN = 3
    COMBAT = 4
    ATTACK = 5
    DAMAGE = 6
    DEATH = 7


## Class for a player character
class Player(GameObject):
    ## Constructor
    def __init__(self, *args, **kwargs):
        self.velocity_x = 0
        self.velocity_y = 0
        super().__init__(img=resources.player_texture, *args, **kwargs)

    ## Update the character based on
    def update(self, dt):
        # Check for interaction input
        if game.game_input[controls.game["big_menu"][0]]:
            # TODO: Implement pause menu
            game.changeToTitleState()
            return True
        # Check for movement input
        if (
            game.game_input[controls.game["up"][0]]
            or game.game_input[controls.game["up"][1]]
        ):
            self.velocity_y += 500
        elif (
            game.game_input[controls.game["down"][0]]
            or game.game_input[controls.game["down"][1]]
        ):
            self.velocity_y += -500
        elif (
            game.game_input[controls.game["left"][0]]
            or game.game_input[controls.game["left"][1]]
        ):
            self.velocity_x += -500
        elif (
            game.game_input[controls.game["right"][0]]
            or game.game_input[controls.game["right"][1]]
        ):
            self.velocity_x += 500
        # Update position
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        # Reset velocity
        self.velocity_x = 0
        self.velocity_y = 0
        return


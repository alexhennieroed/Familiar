## @module controller
#  Contains the control logic

from enum import Enum

class GameState(Enum):
    TITLE = 1
    GAME = 2
    QUIT = 3
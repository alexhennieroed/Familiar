## @module controls
#  Defines control schemes for various contexts

import pyglet.window.key as key

## Controls for use in menus
menu = {
    "up": [key.UP, key.W, (0,1)],
    "down": [key.DOWN, key.S, (0,-1)],
    "left": [key.LEFT, key.A, (-1, 0)],
    "right": [key.RIGHT, key.D, (1, 0)],
    "accept": [key.ENTER, 'a'],
    "cancel": [key.ESCAPE, 'b']
}

## Controls for use in the game
game = {
    "up": [key.UP, key.W, (0,1)],
    "down": [key.DOWN, key.S, (0,-1)],
    "left": [key.LEFT, key.A, (-1, 0)],
    "right": [key.RIGHT, key.D, (1, 0)],
    "b_face": [key.E, 'a'],
    "r_face": [key.Q, 'b'],
    "l_face": [key.F, 'x'],
    "t_face": [key.R, 'y'],
    "game_menu": [key.TAB, 'back'],
    "big_menu": [key.ESCAPE, 'start']
}
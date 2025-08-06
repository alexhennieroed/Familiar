## The entry-point for the game

import pyglet
import src.game as game

## Redefine the resource path to reference the internal folder
pyglet.resource.path = ['res']
pyglet.resource.reindex()

## Run the game
game.main()
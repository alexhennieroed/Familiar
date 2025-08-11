## The entry-point for the game

import pyglet
import src.game as game

## Run the game
if __name__ == '__main__':
    pyglet.clock.schedule_interval(game.update, 1/120.0)
    pyglet.app.run()
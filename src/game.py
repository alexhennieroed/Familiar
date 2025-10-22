## @module game
#  Module that provides the game logic

import pyglet
from src.controller import *
from src.view import *
import src.resources as resources

## Define the overall game window
display = pyglet.display.get_display()
screen = display.get_default_screen()
win_pos_x = (screen.width - 640) // 2
win_pos_y = (screen.height - 360) // 2
game_window = pyglet.window.Window(640, 360, resizable=False, visible=False)
game_window.set_icon(resources.icon16, resources.icon32)
game_window.set_caption("FAMILIAR")
game_window.set_location(win_pos_x, win_pos_y)
game_window.set_visible()

## Define the game controls
game_input = pyglet.window.key.KeyStateHandler()
game_window.push_handlers(game_input)
game_window.set_exclusive_keyboard
game_window.set_exclusive_mouse
## Prevent ESC from closing the game
@game_window.event
def on_key_press(symbol, modifiers):
    game_input.on_key_press(symbol, modifiers)
    return pyglet.event.EVENT_HANDLED

@game_window.event
def on_key_release(symbol, modifiers):
    game_input.on_key_release(symbol, modifiers)
    return pyglet.event.EVENT_HANDLED

## Define the batch renderer and associated groups
game_batch = pyglet.graphics.Batch()
background = pyglet.graphics.Group(order=0) #background color or visuals
zlayer_0 = pyglet.graphics.Group(order=1) #the ground and objects that go behind the player and collidables
zlayer_1 = pyglet.graphics.Group(order=2) #where the player and collidables exist
zlayer_2 = pyglet.graphics.Group(order=3) #objects that the player and collidables go behind
foreground = pyglet.graphics.Group(order=4) #UI elements and alerts
game_groups = [background, zlayer_0, zlayer_1, zlayer_2, foreground]

## What to draw in the game window
@game_window.event
def on_draw():
    game_window.clear()
    game_batch.draw()

## Changes the game to the Title Screen state
def changeToTitleState():
    global game_state
    global game_screens
    game_state = GameState.GameState.TRANSITION
    for screen in game_screens:
        screen.delete()
        game_screens.remove(screen)
    title_screen = TitleScreen.TitleScreen(game_batch, game_groups)
    game_screens.append(title_screen)
    game_state = GameState.GameState.TITLE
    return

## Changes the game to the Game state //PLACEHOLDER//
def changeToGameState():
    global game_state
    global game_screens
    game_state = GameState.GameState.TRANSITION
    for screen in game_screens:
        screen.delete()
        game_screens.remove(screen)    
    game_screen = GameScreen.GameScreen(game_batch, game_groups)
    game_screens.append(game_screen)
    game_state = GameState.GameState.GAME
    return

## Changes the game to the quit state
def changeToQuitState():
    global game_state
    global game_screens
    for screen in game_screens:
        screen.delete()
        game_screens.remove(screen)
    game_state = GameState.GameState.QUIT
    return

game_state = None
game_screens = []
## Game loop update function
def update(dt):
    match game_state:
        case GameState.GameState.TRANSITION:
            return
        case GameState.GameState.TITLE:
            game_screens[0].update(dt)
            return
        case GameState.GameState.GAME:
            game_screens[0].update(dt)
            return
        case GameState.GameState.QUIT:
            game_window.close()
            return
        case _:
            changeToTitleState()
    return
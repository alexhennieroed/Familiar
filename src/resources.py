## @moduel resources
#  Defines the resource variables for use in the game

import pyglet

## Redefine the resource path to reference the internal folder
pyglet.resource.path = ['res']
pyglet.resource.reindex()

## Window Icons
icon16 = pyglet.resource.image("icon16.png")
icon32 = pyglet.resource.image("icon32.png")

## Backgrounds
title_bg = pyglet.resource.image("title_bg.png")
game_bg = pyglet.resource.image("game_bg.png")

## Title and Word Textures
title_banner = pyglet.resource.image("title_banner.png")
game_placeholder = pyglet.resource.image("game_placeholder.png")

## Button Textures
title_play_unpressed = pyglet.resource.image("title_button_play_unpressed.png")
title_play_pressed = pyglet.resource.image("title_button_play_pressed.png")
title_play_hover = pyglet.resource.image("title_button_play_hover.png")
title_quit_unpressed = pyglet.resource.image("title_button_quit_unpressed.png")
title_quit_pressed = pyglet.resource.image("title_button_quit_pressed.png")
title_quit_hover = pyglet.resource.image("title_button_quit_hover.png")
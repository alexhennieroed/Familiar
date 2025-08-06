## @package src
#  Module that provides the game logic

import pyglet
import src.controller.controller as controller
import src.model.model as model
import src.view.view as view


def main():
    title_screen = view.TitleScreenView(0)
    title_screen.buildWindow()
    pyglet.app.run()
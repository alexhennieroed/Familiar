## @package src
#  Module that provides the game logic

import pyglet
import src.controller.controller as controller
import src.model.model as model
import src.view.view as view


def main():
    view.buildTitleWindow()
    pyglet.app.run()
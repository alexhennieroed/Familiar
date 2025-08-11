## @module GameScreen
#  Defines the game screen

import pyglet
import src.game as game
import src.resources as resources
import src.controller.controls as controls


## Class to represent a game screen
class GameScreen:
    ## Constructor
    def __init__(self, batch, groups):
        self.batch = batch
        self.groups = groups
        self.object_list = []
        self.visible = True
        self.buildGameScreen()

    ## Build the game screen
    def buildGameScreen(self):
        ## Build the UI elements
        game_bg_sprite = pyglet.sprite.Sprite(img=resources.game_bg, batch=self.batch, group=self.groups[0])
        game_placeholder_sprite = pyglet.sprite.Sprite(img=resources.game_placeholder, batch=self.batch, group=self.groups[4])
        ## Add the elements to the object list for tracking
        self.object_list.append(game_bg_sprite)
        self.object_list.append(game_placeholder_sprite)
    
    ## Handle key press
    def on_key_press(self, symbol, modifiers):
        if symbol in controls.game['big_menu']:
            game.changeToTitleState() # TODO: Do the actual thing
            return True
    
    ## Set as visible or invisible
    def setScreenVisible(self, visible):
        if not self.visible == visible:
            for obj in self.object_list:
                obj.visible = visible
            self.visible = visible

    ## Delete the screen
    def delete(self):
        for obj in self.object_list:
            obj.delete()
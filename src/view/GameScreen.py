## @module GameScreen
#  Defines the game screen

import pyglet
import src.game as game
import src.resources as resources
import src.controller.controls as controls
import src.model.Player as player


## Class to represent a game screen
class GameScreen:
    ## Constructor
    def __init__(self, batch, groups):
        self.batch = batch
        self.groups = groups
        self.object_list = []
        self.visible = True
        self.player = player.Player(batch=self.batch, group=self.groups[2])
        self.buildGameScreen()

    ## Build the game screen
    def buildGameScreen(self):
        ## Build the UI elements
        game_bg_sprite = pyglet.sprite.Sprite(img=resources.game_bg, batch=self.batch, group=self.groups[0])
        game_placeholder_sprite = pyglet.sprite.Sprite(img=resources.game_placeholder, batch=self.batch, group=self.groups[4])
        game_player_sprite = self.player
        ## Add the elements to the object list for tracking
        self.object_list.append(game_bg_sprite)
        self.object_list.append(game_placeholder_sprite)
        self.object_list.append(game_player_sprite)
    
    ## Set as visible or invisible
    def setScreenVisible(self, visible):
        if not self.visible == visible:
            for obj in self.object_list:
                obj.visible = visible
            self.visible = visible

    ## Update loop
    def update(self, dt):
        for object in self.object_list:
            object.update(dt)
        return

    ## Delete the screen
    def delete(self):
        for obj in self.object_list:
            obj.delete()
## @module TitleScreen
#  Defines the title screen

import pyglet
import src.game as game
import src.resources as resources
import src.controller.controls as controls
import src.view.view as view

## Action to take when the play button is selected
def on_play_selected():
    game.changeToGameState()
## Action to take when the quit button is selected
def on_quit_selected():
    game.changeToQuitState

## A class to make the Title Screen
class TitleScreen:
    ## Constructor
    def __init__(self, batch, groups):
        self.batch = batch
        self.background = groups[0]
        self.foreground = groups[4]
        self.object_list = []
        self.selectables = []
        self.selected = 0
        self.buildTitleScreen()

    ## Builds and displays the title screen
    def buildTitleScreen(self):
        ## Build the UI elements
        title_bg_sprite = pyglet.sprite.Sprite(img=resources.title_bg, batch=self.batch, group=self.background)
        title_banner_sprite = pyglet.sprite.Sprite(img=resources.title_banner, x=200, y=450,
                                        batch=self.batch, group=self.foreground)
        play_button_sprite = view.MenuButton(unpressed=resources.title_play_unpressed, pressed=resources.title_play_pressed,
                                        hover=resources.title_play_hover, x=300, y=250, on_action=game.changeToGameState,
                                        batch=self.batch, group=self.foreground)
        quit_button_sprite = view.MenuButton(unpressed=resources.title_quit_unpressed, pressed=resources.title_quit_pressed,
                                        hover=resources.title_quit_hover, x=300, y=50, on_action=game.changeToQuitState,
                                        batch=self.batch, group=self.foreground)
        ## Add selectable menu elements to the list for tracking
        self.selectables.append(play_button_sprite)
        self.selectables.append(quit_button_sprite)
        ## Add the elements to the object list for tracking
        self.object_list.append(title_bg_sprite)
        self.object_list.append(title_banner_sprite)
        self.object_list.append(play_button_sprite)
        self.object_list.append(quit_button_sprite)
    
    ## Handle Key Press
    def on_key_press(self, symbol, modifiers):
        if symbol in controls.menu["up"]:
            self.selectables[self.selected].is_now_not_hovered()
            self.selected -= 1
            if self.selected < 0:
                self.selected = len(self.selectables) - 1
            self.selectables[self.selected].is_now_hovered()
        elif symbol in controls.menu["down"]:
            self.selectables[self.selected].is_now_not_hovered()
            self.selected += 1
            if self.selected >= len(self.selectables):
                self.selected = 0
            self.selectables[self.selected].is_now_hovered()
        elif symbol in controls.menu["accept"]:
            self.selectables[self.selected].is_now_pressed()
            self.selectables[self.selected].on_action()
        elif symbol in controls.menu["cancel"]:
            self.selectables[self.selected].is_now_not_hovered()
            self.selected = len(self.selectables) - 1
            self.selectables[self.selected].is_now_hovered()
            return True
        
    ## Delete all objects
    def delete(self):
        for obj in self.object_list:
            obj.delete()
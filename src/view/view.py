## @module view
#  The overall 

import pyglet

## Class for menu buttons 
class MenuButton(pyglet.sprite.Sprite):
    ## Constructor
    def __init__(self, unpressed:pyglet.image.AbstractImage, pressed:pyglet.image.AbstractImage,
            hover:pyglet.image.AbstractImage, on_action, *args, **kwargs):
        super().__init__(img=unpressed, *args, **kwargs)
        self.unpressed = unpressed
        self.pressed = pressed
        self.hover = hover
        self.is_pressed = False
        self.is_hovered = False
        self.on_action = on_action
    ## Change status to hovered
    def is_now_hovered(self):
        if not self.is_hovered and not self.is_pressed:
            self.is_hovered = True
            self.image = self.hover
    ## Change status to not hovered
    def is_now_not_hovered(self):
        if self.is_hovered and not self.is_pressed:
            self.is_hovered = False
            self.image = self.unpressed
    ## Change status to pressed
    def is_now_pressed(self):
        if not self.is_pressed:
            self.is_pressed = True
            self.image = self.pressed
    ## Change status to not pressed
    def is_now_not_pressed(self):
        if self.is_pressed:
            self.is_pressed = False
            self.image = self.unpressed
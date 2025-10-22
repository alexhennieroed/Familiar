## @module GameObject
#  Overarching class for all items that can be rendered

import pyglet

## Class for all game objects
class GameObject(pyglet.sprite.Sprite):
    ## Constructor
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
    
    ## Update the object
    def update(self, dt):
        #TODO: Run a default update
        return 0
    
    ## Deletes the object
    def delete(self):
        super().delete()
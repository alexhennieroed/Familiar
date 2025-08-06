## @module view
#  The overall 

import pyglet

## Overall views that include the game display and collections of UI elements
class ViewObject:
    ## Constructor with a zlayer argument
    #  @param zlayer the layer the object is displayed in the frame. lower numbers are further back in the frame
    def __init__(self, zlayer):
        self.__zlayer = zlayer
        return
    
    ## Builds the object's pyglet window
    def buildWindow(self):
        self.__window = pyglet.window.Window()

        @self.__window.event
        def on_draw():
            self.__window.clear()
        return

    ## Get the zlayer private variable
    def getZlayer(self):
        return self.__zlayer

## Class to create a Title Screen
class TitleScreenView(ViewObject):
    ## Constructor with a zlayer argument
    def __init__(self, zlayer):
        super().__init__(zlayer)
    
    ## Build the title screen window
    def buildWindow(self):
        ## Define the window
        self.__window = pyglet.window.Window(1920, 1080)
        ## Load the icons and assign them to the window
        icon16 = pyglet.resource.image("icon16.png")
        icon32 = pyglet.resource.image("icon32.png")
        self.__window.set_icon(icon16, icon32)
        ## Load the background image and create a sprite from it for use
        bg_image = pyglet.resource.image("title_bg.png")
        bg_sprite = pyglet.sprite.Sprite(img=bg_image)
        ## Create the title label
        label = pyglet.text.Label('FAMILIAR',
                          font_name='Times New Roman',
                          font_size=50,
                          weight='bold',
                          color=(0,0,0,255),
                          x=self.__window.width//2, y=(self.__window.height//6)*5,
                          anchor_x='center', anchor_y='center')
        ## Define the on_draw function to clear the window and draw the sprite and label
        @self.__window.event
        def on_draw():
            self.__window.clear()
            bg_sprite.draw()
            label.draw()
        return

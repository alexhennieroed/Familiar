import pyglet

def buildTitleWindow():
    ## Builds the title screen window
    window = pyglet.window.Window()
    label = pyglet.text.Label('FAMILIAR',
                          font_name='Times New Roman',
                          font_size=36,
                          color=(0,200,255,255),
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        label.draw()
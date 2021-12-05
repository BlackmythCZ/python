import pyglet
window = pyglet.window.Window()
#pyglet.app.run()
#print('Hotovo')

def zpracuj_text(text):
    print(text)

window.push_handlers(on_text=zpracuj_text)

pyglet.app.run()

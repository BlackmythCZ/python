import pyglet
import math
window = pyglet.window.Window()

def tik(t):
#    print(t)
    had.x += t * 20
    had.y = 0 + 20 * math.sin(had.x / 5)
#     had.rotation += t * 5
    print(had.x)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
#    print(text)
    had.x = 150

obrazek = pyglet.image.load('D:\\Git\\python\\Data\\python_snake.png')
had = pyglet.sprite.Sprite(obrazek) # vytvoří speciální objekt Sprite, který určuje, že tento obrázek chceme „posadit“ na určité místo v černém okýnku. Když neuděláme nic dalšího, bude obrázek čekat v levém rohu.

def vykresli(): # se stará o vykreslení okna – výstup našeho programu. Volá se vždycky, když je potřeba okno překreslit – například když okno minimalizuješ a pak vrátíš nebo přesuneš částečně ven z obrazovky a pak dáš zase zpět. A nebo když budeme něco animovat.
    window.clear()
    had.draw()

def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y

window.push_handlers( # registrace funkcí
    on_text = zpracuj_text,
    on_draw = vykresli,
    on_mouse_press = klik # Jakékoli kreslení se musí dělat v rámci kreslící funkce, kterou Pyglet volá z on_draw. Jinde funkce jako clear a draw nebudou fungovat správně.
)

obrazek2 = pyglet.image.load('D:\\Git\\python\\Data\\python_snake_jazyk.png')

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 1) # říká Pygletu, že za jednu vteřinu má zavolat funkci zmen. A funkce změní obrázek – stejně jako se předtím měnily souřadnice.

pyglet.app.run()

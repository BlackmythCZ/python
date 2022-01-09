import pyglet

# Konstanty
WIDTH = 900
HIGHT = 600
ROTATION_SPEED = 4
ACCELERATION = 1

# Globální proměnné
objects = []
spaceship_position = [WIDTH // 2, HIGHT / 2]
spaceship_speed = [0, 0]
pressed_keys = set()
score = 0
batch = pyglet.graphics.Batch()
picture1 = pyglet.image.load('D:\\Git\\python\\Data\\Space_shooter_redux\\PNG\\playerShip1_blue.png')
spaceship = pyglet.sprite.Sprite(picture1, batch = batch)

class Spaceship:
    import pyglet
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    rotation = 0    
    def refresh(dt):
        self.x = self.x + dt * self.x_speed
        self.y = self.y + dt * self.y_speed
        self.rotation = self.rotation + dt * rotation_speed
    


def draw():
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT) # smaž obsah okna (vybarvi na černo)

window = pyglet.window.Window(width = WIDTH, height = HIGHT)
window.push_handlers(
    on_draw = batch.draw()
)
from pyray import *
from random import randint, choice

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

WINDOW_BOX = Rectangle(1, 1, 799, 499)


def particle(count):
    particles = []
    colors = [RED,BLUE,WHITE,BLACK,PURPLE,BROWN,PINK,YELLOW]
    for i in range(0, count):
        particles.append(Vector2(randint(100, 700), randint(100, 400)))
        randcolor = choice(colors)
        draw_circle_v(particles[i], randint(1, 100), randcolor)

set_config_flags(FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_UNDECORATED)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "particles")

set_target_fps(60)

while not window_should_close():

    begin_drawing()
    clear_background(BLANK)

    draw_rectangle_lines_ex(WINDOW_BOX, 1, WHITE)
    particle(100)
    end_drawing()

close_window()

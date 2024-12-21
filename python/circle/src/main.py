from pyray import *
from time import sleep

class player:
    def __init__(self, x):
        self.x = x 
# rectangle boxA = { 10, 400, 200, 100 }
# rectangle boxB = { 10, 10, 200, 100 }
init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    sleep(0.014)
    clear_background(WHITE)
    mx = get_mouse_x()
    my = get_mouse_y()
    draw_circle(mx, my, 50, RED)
    draw_text(f'mx:{mx}, my:{my}', 0, 0, 10, BLACK)
    end_drawing()
close_window()

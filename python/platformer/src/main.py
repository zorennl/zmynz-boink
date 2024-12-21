from pyray import *
from time import sleep

class player:
    def __init__(self, x, y, grav):
        self.x = x 
        self.y = y 
        self.grav = grav

player1 = player(0, 0, 1)

init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    sleep(0.014)
    clear_background(WHITE)
    # right
    if is_key_down(KEY_D): 
        player1.x += 2
    # left
    if is_key_down(KEY_A): 
        player1.x -= 2
    # up
    if is_key_down(KEY_W): 
        player1.y -= 2
    # down
    if is_key_down(KEY_S):
        player1.y += 2     

    draw_rectangle(player1.x, player1.y, 50, 50, RED)
    draw_text("Hello world", 190, 200, 20, BLACK)
    end_drawing()
close_window()

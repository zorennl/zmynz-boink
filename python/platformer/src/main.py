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
    # right
    # if is_key_down(KEY_D): 
        # player1.x += 2
    # left
    # if is_key_down(KEY_A): 
    #     player1.x -= 2
    # # up
    # if is_key_down(KEY_W): 
    #     player1.y -= 10
    # # down
    # if is_key_down(KEY_S):
    #     player1.y += 2     
    # collision = check_collision_recs(boxA, boxB)
    mx = get_mouse_x()
    my = get_mouse_y()
    draw_circle(mx, my, 50, RED)
    draw_text(f'mx:{mx}, my:{my}', 0, 0, 10, BLACK)
    end_drawing()
close_window()

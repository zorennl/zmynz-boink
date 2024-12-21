from pyray import *
x = 0
y = 0

init_window(800, 450, "wasd")
set_target_fps(60)
while not window_should_close():
    begin_drawing()
    # right
    if is_key_down(KEY_D): 
        x += 2
    # left
    if is_key_down(KEY_A): 
        x -= 2
    # up
    if is_key_down(KEY_W): 
        y -= 2
    # down
    if is_key_down(KEY_S):
        y += 2     
    # collision = check_collision_recs(boxA, boxB)

    draw_rectangle(x, y, 10, 10, RED)
     
    end_drawing()
close_window()

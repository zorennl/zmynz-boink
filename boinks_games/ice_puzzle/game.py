from pyray import *


init_window(1200,675,"Ice Game For Plebians Like You!")
set_target_fps(60)


while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    movement = (is_key_pressed(68)-is_key_pressed(65),is_key_pressed(83)-is_key_pressed(87))
    
    end_drawing()
close_window()
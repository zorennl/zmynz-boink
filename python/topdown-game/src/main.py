from pyray import *

dirtraw = 'assets/dirt.png'

init_window(800, 450, "Hello")

# set_config_flags(FLAG_WINDOW_TRANSPARENT)
dirt = load_texture(dirtraw)

while not window_should_close():
    
    mx = get_mouse_x()
    my = get_mouse_y()
    middlex = mx - 8
    middley = my - 8
    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        draw_texture(dirt, middlex, middley, WHITE)
    
    begin_drawing()
    
    # clear_background(BLACK)

    # draw_circle(mx, my, 20, WHITE)
    draw_texture(dirt, 0, 0, WHITE)
    
    end_drawing()
unload_texture(dirt)
close_window()

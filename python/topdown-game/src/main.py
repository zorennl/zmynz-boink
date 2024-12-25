from pyray import *
from sys import platform

if platform == "win32":
    dirtraw = 'python\\topdown-game\\assets\\dirt.png'
else:
    dirtraw = 'assets/dirt.png'

init_window(800, 450, "Hello")

# set_config_flags(FLAG_WINDOW_TRANSPARENT)
dirt = load_texture(dirtraw)

while not window_should_close():
    
    mx = get_mouse_x()
    my = get_mouse_y()
    middlex = mx - 8
    middley = my - 8
    dirtbox = Rectangle(mx, my, 16, 16)
    dirtboxdest = Rectangle(mx, my, 160, 160)
    origin = Vector2(0, 0)
        
    begin_drawing()
    
    clear_background(BLACK)

    # draw_circle(mx, my, 20, WHITE)
    draw_texture(dirt, 0, 0, WHITE)
    draw_texture_pro(dirt, dirtbox, dirtboxdest, origin, 0, WHITE)
    
    end_drawing()
unload_texture(dirt)
close_window()

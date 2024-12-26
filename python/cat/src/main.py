from pyray import *
from sys import platform

WINDOW_WIDTH = 278
WINDOW_HEIGHT = 181

catraw = 'assets/cat.png'

if platform == 'win32':
    catraw = 'python\\cat\\assets\\cat.png'

set_config_flags(FLAG_WINDOW_MOUSE_PASSTHROUGH+FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_UNDECORATED+FLAG_WINDOW_TOPMOST)
init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "pet cat")

current_monitor = get_current_monitor()

windowposx = get_monitor_width(current_monitor) - 278
windowposy = get_monitor_height(current_monitor) - 181

print(windowposx, windowposy)

cat = load_texture(catraw)

set_window_position(windowposx, windowposy)

while not window_should_close():

    begin_drawing()

    clear_background(BLANK)

    draw_texture(cat, 0, 0, WHITE)
    
    end_drawing()

close_window()

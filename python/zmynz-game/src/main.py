from pyray import *
from os.path import join as os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

dirtr = os('assets', 'dirt.png')
playerr = os('assets', 'player.png')

set_config_flags(FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_TOPMOST+FLAG_WINDOW_UNDECORATED)
# set_config_flags(FLAG_)

playerpos = Vector2(400, 450)

dirtdir = Vector2(1, 1)
dirtpos = Vector2(0, 0)
dirtspd = 2


init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "")

set_window_state(1)

set_target_fps(60)

test = False

button = Rectangle(400, 225, 100, 50)

dirt = load_texture(dirtr)
player = load_texture(playerr)

while not window_should_close():

    if dirtpos.y >= WINDOW_HEIGHT - 34:
        dirtdir.y = -1
    if dirtpos.x >= WINDOW_WIDTH - 34:
        dirtdir.x = -1
    if dirtpos.y <= 0:
        dirtdir.y = 1
    if dirtpos.x <= 0:
        dirtdir.x = 1
    
    dirtpos.x += dirtdir.x * dirtspd; dirtpos.y += dirtdir.y * dirtspd
    
    playerpos = get_mouse_position()
    playerpos.x -= 4; playerpos.y -= 4
    begin_drawing()

    hide_cursor()
    if is_key_pressed(KEY_F):
        toggle_fullscreen()
        toggle_borderless_windowed()
        
    clear_background(BLANK)

    # if gui_button(button, "button"):
        # test = not test
    if test == True:
        draw_text("button", 0, 0, 20, WHITE)

    draw_texture_ex(dirt, dirtpos, 0, 2, WHITE)
    draw_text(f'mx:{playerpos.x}, my:{playerpos.y}', 320, 0, 20, WHITE)
    draw_texture_ex(player, playerpos, 0, 1.5, WHITE)
    
    
    end_drawing()
close_window()

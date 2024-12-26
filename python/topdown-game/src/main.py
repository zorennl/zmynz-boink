from pyray import *
from os.path import join as os

dirtr = os('assets', 'dirt.png')
playerr = os('assets', 'player.png')

set_config_flags(FLAG_WINDOW_TRANSPARENT)

playerpos = Vector2(400, 450)

init_window(800, 450, "Hello")

set_target_fps(60)

test = False

button = Rectangle(400, 225, 100, 50)

dirt = load_texture(dirtr)
player = load_texture(playerr)

while not window_should_close():

    playerpos = get_mouse_position()
    playerpos.x -= 40; playerpos.y -= 40
        
    begin_drawing()

    hide_cursor()
        
    clear_background(BLANK)

    if gui_button(button, "button"):
        test = not test
    if test == True:
        draw_text("button", 0, 0, 20, WHITE)
    
    draw_text(f'mx:{playerpos.x}, my:{playerpos.y}', 320, 0, 20, WHITE)
    draw_texture_ex(player, playerpos, 0, 10, WHITE)
    
    
    end_drawing()
close_window()

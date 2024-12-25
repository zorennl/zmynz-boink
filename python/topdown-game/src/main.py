from pyray import *
from os.path import join 

dirtr = join('assets', 'dirt.png')
playerr = join('assets', 'player.png')

set_config_flags(FLAG_WINDOW_TRANSPARENT)

playerpos = Vector2(400, 450)

init_window(800, 450, "Hello")

dirt = load_texture(dirtr)
player = load_texture(playerr)

while not window_should_close():
    
    playerpos = get_mouse_position()
    playerpos.x -= 40; playerpos.y -= 40
    origin = Vector2(0, 0)
        
    begin_drawing()
    
    clear_background(BLANK)

    draw_texture(dirt, 0, 0, WHITE)
    draw_text(f'mx:{playerpos.x}, my:{playerpos.y}', 320, 0, 20, WHITE)
    draw_texture_ex(player, playerpos, 0, 10, WHITE)
    
    end_drawing()
unload_texture(dirt)
close_window()

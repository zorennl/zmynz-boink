from pyray import *
from os.path import join as os
class bullet:
    def __init__(self,shape, velocity, time):
        self.shape = shape
        self.velocity = velocity
        self.time = time
        
    def drawbullet(bullet):
        draw_rectangle_rec(bullet.shape, YELLOW)
dirtr = os('assets', 'dirt.png')
playerr = os('assets', 'player.png')

set_config_flags(FLAG_WINDOW_TRANSPARENT)

playerpos = Vector2(400, 450)

init_window(800, 450, "Hello")

dirt = load_texture(dirtr)
player = load_texture(playerr)

while not window_should_close():

    bulshape = Rectangle(playerpos.x, playerpos.y, 5, 10)
    bul = bullet(bulshape, 2, 999999)
        
    playerpos = get_mouse_position()
    playerpos.x -= 40; playerpos.y -= 40
    origin = Vector2(0, 0)
        
    begin_drawing()

    hide_cursor()
        
    clear_background(BLANK)

    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT): 
        for i in range(1, bul.time):
            bullet.drawbullet(bul)  
            bulshape.y -= bul.velocity
    draw_texture(dirt, 0, 0, WHITE)
    draw_text(f'mx:{playerpos.x}, my:{playerpos.y}', 320, 0, 20, WHITE)
    draw_texture_ex(player, playerpos, 0, 10, WHITE)
    
    
    end_drawing()
unload_texture(dirt)
close_window()

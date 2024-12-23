from pyray import *
from time import sleep
from sys import platform

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

class player:
    def __init__(self,tint,x,y):
        self.tint =tint
        self.x =x
        self.y =y

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "topdown")
png = 'assets/player.png'
zoren = player(WHITE, 0, 0)
spr = load_texture(png)

set_config_flags(FLAG_WINDOW_TRANSPARENT)

set_target_fps(60)

while window_should_close():

    # plyrcollision = Rectangle(zoren.x, zoren.x, 8, 8 )

    begin_drawing()
    clear_background(BLANK)
    
    draw_texture(spr, zoren.x, zoren.y, zoren.tint)
    
    end_drawing()

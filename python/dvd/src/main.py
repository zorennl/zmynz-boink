from pyray import *
from os.path import join as os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

dvdr = os('assets', 'dvd.png')
playerr = os('assets', 'player.png')

set_config_flags(FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_TOPMOST+FLAG_WINDOW_UNDECORATED)

playerpos = Vector2(400, 450)

dvddir = Vector2(1, 1)
dvdpos = Vector2(0, 0)
dvdspd = 2

class color:
     def __init__(self, hue, sat, val):
        self.hue = hue
        self.sat = sat
        self.val = val
     def rgb(self):
         return color_from_hsv(self.hue,self.sat,self.val)

raimbow = color(0, 1, 1)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "")

set_window_state(1)

set_target_fps(60)

test = False

button = Rectangle(400, 225, 100, 50)

dvd = load_texture(dvdr)
player = load_texture(playerr)

while not window_should_close():

    if dvdpos.y >= WINDOW_HEIGHT - 56:
        dvddir.y = -1
    if dvdpos.x >= WINDOW_WIDTH - 107:
        dvddir.x = -1
    if dvdpos.y <= 0:
        dvddir.y = 1
    if dvdpos.x <= 0:
        dvddir.x = 1
    
    dvdpos.x += dvddir.x * dvdspd; dvdpos.y += dvddir.y * dvdspd

    raimbow.hue += 1
    if raimbow.hue == 360:
        raimbow.hue
    raimbowc = color.rgb(raimbow)    
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
    
    draw_texture_ex(dvd, dvdpos, 0, 0.5, raimbowc)
    draw_texture_ex(player, playerpos, 0, 1.5, WHITE)
    draw_rectangle_lines(1, 1, WINDOW_WIDTH - 1 , WINDOW_HEIGHT - 1, WHITE)    
    
    end_drawing()
close_window()

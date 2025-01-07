from pyray import *
from sys import platform
from time import sleep

if platform == "win32":
    spr = 'python\\texture\\assets\\sprite.png'
else:
    spr = 'assets/sprite.png'

class player:
    def __init__(self, x, y, tint):
        self.x = x
        self.y = y
        self.tint = tint

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

zoren = player(0, 0, WHITE)

set_config_flags(FLAG_WINDOW_TRANSPARENT)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "texture")
set_target_fps(60)

spr = load_texture(spr)

box = Rectangle(0, 175,  300, 100)
boxspd = 1

while not window_should_close():
    
    if is_key_down(KEY_W):
        zoren.y -= 2
    if is_key_down(KEY_S):
        zoren.y += 2
    if is_key_down(KEY_D):
        zoren.x += 2
    if is_key_down(KEY_A):
        zoren.x -= 2
    box.x += boxspd
    if box.x + box.width >= get_screen_width() or box.x <= 0: boxspd *= -1
    
    playercollision = Rectangle(zoren.x, zoren.y, 125, 170)
    collision = check_collision_recs(playercollision, box)
           
    begin_drawing()
    
    clear_background(BLANK)

    begin_mode_2d(camera)
    
    draw_text(f"x:{box.x}", 0, 0, 20, WHITE)
    draw_texture(spr, zoren.x, zoren.y, zoren.tint)
    draw_rectangle_rec(box, RED)

    if collision == True:
        zoren.tint = RED
    else:
        zoren.tint = WHITE
        
    end_drawing()

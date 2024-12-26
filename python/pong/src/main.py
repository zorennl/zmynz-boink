from pyray import *
from time import sleep

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

win = 0
lose = 0

set_config_flags(FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_TOPMOST+FLAG_WINDOW_UNDECORATED)

# BALL

balldir = Vector2(1, 1)
ballpos = Vector2(375, 200)
ballspd = 2
ballsize = Vector2(25, 25)

def ballreset():
    ballpos.x = 375
    ballpos.y = 200

# PADLE

padledir = 0
padlepos = Vector2(0, 325)
padlesize = Vector2(50, 100)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "")

set_window_state(1)

set_target_fps(60)

test = False

button = Rectangle(400, 225, 100, 50)

while not window_should_close():

    if ballpos.y >= WINDOW_HEIGHT - 25:
        balldir.y = -1
    if ballpos.x >= WINDOW_WIDTH - 25:
        win = 60
        ballreset()
        ballspd = 0
    if ballpos.y <= 0:
        balldir.y = 1
    if ballpos.x <= 0:
        lose = 60
        ballreset()
        ballspd = 0
    
    ballpos.x += balldir.x * ballspd; ballpos.y += balldir.y * ballspd
    
    begin_drawing()

    hide_cursor()
    clear_background(BLANK)

    # if gui_button(button, "button"):
        # test = not test
    if test == True:
        draw_text("button", 0, 0, 20, WHITE)

    if win > 0:
        lose -=1
        draw_text("SCORE!", 375, 0, 20, WHITE)
    if lose > 0:
        lose -= 1
        draw_text("LOSER", 375, 0, 20, WHITE)
    
    draw_rectangle_v(ballpos, ballsize, WHITE)
    
    
    end_drawing()
close_window()

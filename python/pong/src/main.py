from pyray import *
from time import sleep

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

win = 0
lose = 0

set_config_flags(FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_TOPMOST+FLAG_WINDOW_UNDECORATED)

# BALL

balldir = Vector2(1, 1)
ball = Rectangle(375, 200, 25, 25)
ballspd = 2

def ballreset():
    ball.x = 375
    ball.y = 200

# PADLE

paddledir = 0
paddle1 = Rectangle(0, 225, 20, 50)
paddle2 = Rectangle(780, 225, 20, 50)

# SCORES
bot = 0
player =0

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "")

set_target_fps(60)

while not window_should_close():

    if is_key_down(KEY_W):
        paddle1.y -= 3
    if is_key_down(KEY_S):
        paddle1.y += 3

    if paddle1.y < 0:
        paddle1.y += 3
    if paddle1.y > WINDOW_HEIGHT - 50:
        paddle1.y -= 3
    paddle2.y = ball.y - 25
    
    if ball.y >= WINDOW_HEIGHT - 25:
        balldir.y = -1
    if ball.x >= WINDOW_WIDTH - 25:
        win = 120
        player += 1
        ballreset()
        ballspd = 0
    if ball.y <= 0:
        balldir.y = 1
    if ball.x <= 0:
        lose = 120
        bot += 1
        ballreset()
        ballspd = 0
    
    ball.x += balldir.x * ballspd; ball.y += balldir.y * ballspd
    
    begin_drawing()

    hide_cursor()
    clear_background(BLANK)

    if win > 0:
        lose -=1
        draw_text("SCORE!", 375, 0, 20, WHITE)
    if win or lose == 1:
        ballspd = 1
    if lose > 0:
        lose -= 1
        draw_text("LOSER", 375, 0, 20, WHITE)
    collision1 = check_collision_recs(paddle1, ball)
    collision2 = check_collision_recs(paddle2, ball)
    if collision1 == True:
        balldir.x = 1
    if collision2 == True:
        balldir.x = -1
    draw_rectangle_rec(paddle2,WHITE)
    draw_rectangle_rec(paddle1, WHITE)
    draw_rectangle_rec(ball, WHITE)
    draw_text(f'score:{player, bot}', 360, 0, 20, WHITE)
    draw_rectangle_lines(1, 1, WINDOW_WIDTH - 1, WINDOW_HEIGHT - 1, WHITE)
    
    
    end_drawing()
close_window()

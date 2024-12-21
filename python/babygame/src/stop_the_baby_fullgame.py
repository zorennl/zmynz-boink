from pyray import *
from time import sleep
import math

fire = open('python\\babygame\\assets\\fire', 'r')
fire = fire.read()
screenWidth = 800
screenHeight = 450
rx = screenWidth
ry = 200
bb = "BABY"
push_timer = 0

print(fire)
init_window(screenWidth, screenHeight, "Stop the baby v2")
while not window_should_close():
    sleep(.004)
    begin_drawing()
    clear_background(WHITE)

    if rx < 30: bb = "DEAD BABY"
    else: rx -= .2
    ry = int(200 + 25 * math.sin(rx / 40))
## keyboard
    if is_key_down(KEY_SPACE):
        rx += 10
## timer
    if push_timer > 0:
        push_timer -= 1
## backround
    draw_rectangle(0, 0, screenWidth, screenHeight, DARKGRAY)
    draw_rectangle(0, 150, screenWidth, 150, GRAY)
## fire 🔥
    draw_text(fire, 20, 160, 1, RED)
## baby
    draw_text(bb, int(rx), ry, 50, LIME)
## stats
    press = get_key_pressed()
    print(press)
    draw_text(f'button: {press}', 10, 10, 20, BLACK)
    draw_text(f'x: {rx}, y: {ry}', 10, 40, 20, BLACK)
    draw_text(f'push_timer: {push_timer}', 10, 70, 20, BLACK)
    end_drawing()
close_window()
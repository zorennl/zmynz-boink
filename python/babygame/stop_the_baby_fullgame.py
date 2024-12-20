from pyray import *
from time import sleep
import math


fire = open('assets/fire.txt', 'r')
screenWidth = 800
screenHeight = 450
rx = screenWidth
ry = 200
bb = "BABY"

init_window(screenWidth, screenHeight, "Stop the baby v2")
while not window_should_close():
    sleep(.004)
    begin_drawing()
    clear_background(WHITE)
    if rx < 30: bb = "DEAD BABY"
    else: rx -= .2
    ry = int(200 + 25 * math.sin(rx / 40))
    draw_rectangle(0, 0, screenWidth, screenHeight, DARKGRAY)
    draw_rectangle(0, 150, screenWidth, 150, GRAY)
    draw_text(str(fire), 20, 200, 10, RED)
    end_drawing()
close_window()

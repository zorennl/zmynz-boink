from pyray import *
from time import sleep

screenWidth = 800
screenHeight = 450
rx = screenWidth
ry = 200

init_window(screenWidth, screenHeight, "Hello")
while not window_should_close():
    sleep(.004)
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 20, 20, 10, GRAY)
    rx -= 1
    if rx < -50:
        rx = screenWidth 
    draw_rectangle(rx, ry, 50, 50, RED)
    draw_rectangle(0, 250, screenWidth, 225, GREEN)
    end_drawing()
close_window()


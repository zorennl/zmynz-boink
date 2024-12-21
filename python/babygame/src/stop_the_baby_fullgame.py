from pyray import *
from time import sleep
from pynput import keyboard
import math

press = ""
def on_press(key):
    global press
    try: press = key.char
    except AttributeError: press = key

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

fire = open('python\\babygame\\assets\\fire', 'r')
fire = fire.read()
screenWidth = 800
screenHeight = 450
rx = screenWidth
ry = 200
bb = "BABY"
print(fire)
init_window(screenWidth, screenHeight, "Stop the baby v2")
while not window_should_close():
    sleep(.004)
    begin_drawing()
    clear_background(WHITE)

    if rx < 30: bb = "DEAD BABY"
    else: rx -= .2
    ry = int(200 + 25 * math.sin(rx / 40))

    if press == keyboard.Key.space:
        press = ""
        rx += 10
## backround
    draw_rectangle(0, 0, screenWidth, screenHeight, DARKGRAY)
    draw_rectangle(0, 150, screenWidth, 150, GRAY)
## fire 🔥
    draw_text(fire, 20, 160, 1, RED)
## baby
    draw_text(bb, int(rx), ry, 50, LIME)
## stats
    draw_text(f'button: {press}', 10, 10, 20, BLACK)
    draw_text(f'x: {rx}, y: {ry}', 10, 40, 20, BLACK)
    end_drawing()
close_window()

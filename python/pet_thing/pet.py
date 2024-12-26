from pyray import *
import math
from os.path import join as os



set_config_flags(4120+16384)

mNum = get_current_monitor()



init_window(110,140,"")
set_target_fps(60)

xMax = get_monitor_width(mNum)
yMax = get_monitor_height(mNum) 

x = 20
y = 20
direction = 0
state = {"moveType":0,"timer":0}

dog = load_texture(os("python","pet_thing","assets","dog.png"))
dog2 = load_texture(os("python","pet_thing","assets","dog2.png"))
dog3 = load_texture(os("python","pet_thing","assets","dog3.png"))

newDirection = 0


while not window_should_close():

    begin_drawing()
    clear_background(BLANK)
    draw_texture(dog,0,0,WHITE)
    draw_text(f"{x}",0,0,10,BLACK)
    draw_text(f"{y}",30,0,10,BLACK)
    draw_text(f"{direction}",60,0,10,BLACK)
    draw_text(f"moveType: {state['moveType']}, timer: {state['timer']}",0,20,10,BLACK)

    if state["timer"] == 0:
        if get_random_value(1,2) == 1:
            state["moveType"] = 1
            state["timer"] = get_random_value(60,120)
        else:
            state["moveType"] = 2
            state["timer"] = 80
            newDirection = direction - get_random_value(-60,60)
    elif state["moveType"] == 1:
        x += math.sin(math.radians(direction))*2
        y += math.cos(math.radians(direction))*2
        state["timer"] -= 1
    elif state["moveType"] == 2:
        x += math.sin(math.radians(direction))*1
        y += math.cos(math.radians(direction))*1
        if newDirection > direction:
            direction += 1
        elif newDirection < direction:
            direction -= 1
        else: state["timer"] = 0

    set_window_position(int(x),int(y))

    x += 5*(is_key_down(KEY_D)-is_key_down(KEY_A))
    y += 5*(is_key_down(KEY_S)-is_key_down(KEY_W))

        
    if x > xMax-110: x = xMax-110
    if x < 0: x = 0
    if y > yMax-140: y = yMax-140
    if y < 0: y = 0         

    end_drawing()
close_window()
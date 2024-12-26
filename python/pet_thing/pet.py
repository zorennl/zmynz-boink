from pyray import *
from os.path import join as os



set_config_flags(4120)

mNum = get_current_monitor()



init_window(110,140,"")
set_target_fps(60)

xMax = get_monitor_width(mNum)
yMax = get_monitor_height(mNum) 

x = 20
y = 20

dog = load_texture(os("python","pet_thing","assets","dog.png"))

print(xMax)

while not window_should_close():

    begin_drawing()
    clear_background(BLANK)
    draw_texture(dog,0,0,WHITE)
    draw_text(f"{x}",0,0,10,BLACK)
    draw_text(f"{y}",30,0,10,BLACK)


    set_window_position(int(x),int(y))

    x += 5*(is_key_down(KEY_D)-is_key_down(KEY_A))
    y += 5*(is_key_down(KEY_S)-is_key_down(KEY_W))

        
    if x > xMax-110: x = xMax-110
    if x < 0: x = 0
    if y > yMax-140: y = yMax-140
    if y < 0: y = 0         

    end_drawing()
close_window()
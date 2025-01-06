from pyray import *


init_window(500,500,"123")

set_target_fps(60)
inbox = Rectangle(100,100,200,200)
window = Rectangle(10,10,60,60)
a = -1
text = ""


while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    if a != 1:
        a = gui_text_input_box(inbox,"CAPTCHA","type captcha here:","done",text,50,ffi.new("bool *", True))
    else:
        draw_text(f"{text}",10,10,20,WHITE)

    end_drawing()
close_window()
from pyray import *

test1x = 0
test1y = 0

test2x = 0
test2y = 0

testw = 0
testh = 0

click_count = 0

init_window(800, 500, "test")

set_target_fps(60)

while not window_should_close():
    mousepos = get_mouse_position()

    test = Rectangle(test1x,test1y,testw,testh)
    
    testw = test2x - test1x
    testh = test2y - test1y
    
    begin_drawing()
    clear_background(WHITE)

    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        click_count += 1
        if click_count == 1:
            test1x = mousepos.x
            test1y = mousepos.y
        if click_count == 2:
            test2x = mousepos.x
            test2y = mousepos.y
        if click_count == 2:
            click_count = 0

    draw_rectangle_rec(test, RED)
    end_drawing()

close_window()

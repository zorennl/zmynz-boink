from pyray import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

def dotted_line(start, end, interval):
    windowh = get_screen_width()
    windowh = get_screen_height()

    xdist = start.x - end.x
    abs(xdist)
    dist = xdist*xdist + windowh*windowh

    spacing = dist / interval

    #for i in range(0, spacing):
        #draw_line

start = Vector2(250, 0)
end = Vector2(250, 800)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "dotted line")
while not window_should_close():

    begin_drawing()
    
    
    #dotted_line(start, end, 1)

    draw_line_strip(Vector2(400, 0), 5, WHITE)
    draw_line_bezier(Vector2(0, 0), Vector2(800, 500), 20, BLUE)
        
    end_drawing()

close_window()

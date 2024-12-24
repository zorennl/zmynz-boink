from pyray import *
from time import sleep

WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100

CELL_WIDTH = 50
CELL_HEIGHT = 50

cellsx = []
cellsy = []

x = 0
y = 0

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "test")

while not window_should_close():

    begin_drawing()

    clear_background(BLACK)
    
    for i in range(100):
        if x == 90:
            x = 0
            y += 10
        cellsx.append(x)
        cellsy.append(y)
        draw_rectangle_lines(cellsx[i], cellsy[i], CELL_WIDTH, CELL_HEIGHT, WHITE)
        x += 10
            
    end_drawing()
close_window()

from pyray import *
from draw_grid import *

init_window(100,100,"raylib")
set_target_fps(60)

while not window_should_close():

    begin_drawing()
    clear_background(BLACK)
  
    draw_grid2D(50,50,2,Rectangle(0,0,100,100),GREEN)

    end_drawing()    
close_window()

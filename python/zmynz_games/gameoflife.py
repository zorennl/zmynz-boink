from pyray import *
from math import floor

gridycount = 100
gridxcount = 100

gridy = 1
gridx = 1

cellsize = 10

cells = []

selectedx = 0
selectedy = 0

grid = []

for y in range(gridycount):
    grid.append([])
    for x in range(gridxcount):
        grid[y].append(False)

init_window(102,102,"gol")

set_target_fps(15)

set_exit_key(KEY_Q)

while not window_should_close():

    mpos = get_mouse_position()

    selectedx = min(floor(mpos.x / cellsize), gridxcount - 1)
    selectedy = min(floor(mpos.y / cellsize), gridycount - 1)
   
    begin_drawing()

    draw_rectangle_lines(1,1,100,100,WHITE)
    for y in range(gridycount):
        for x in range(gridxcount):
            celldrawsize = cellsize - 1

            if x == selectedx and y == selectedy:
                cellcolor = PURPLE
            elif grid[y][x] == True:
                cellcolor = YELLOW
            else:
                cellcolor = LIGHTGRAY
            
            draw_rectangle(
                           x*cellsize,
                           y*cellsize,
                           celldrawsize,
                           celldrawsize,
                           cellcolor
                          )
    if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
        grid[selectedy][selectedx] = True
    if is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
        grid[selectedy][selectedx] = False

    if is_key_down(KEY_F):

        nextgrid = []

        for y in range(gridycount):
            nextgrid.append([])
    
            for x in range(gridxcount):

                neighborcount = 0    

                for dy in range(-1,2):
                    for dx in range(-1,2):
                        if (not(dy == 0 and dx == 0)
                           and 0 <= (selectedy + dy) < gridycount
                           and 0 <= (selectedx + dx) < gridxcount
                           and grid[selectedy + dy][selectedx + dx]):
                           neighborcount += 1
                nextgrid[y].append(neighborcount == 3 or (grid[y][x] and neighborcount == 2))
        grid = nextgrid

    end_drawing()

close_window()

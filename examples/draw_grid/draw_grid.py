from pyray import *

def draw_grid2D(xline,yline,spacing,rectangle:Rectangle,color):
    for x in range(xline):
        draw_line(x*spacing,int(rectangle.y),x*spacing,int(rectangle.height),color)
        for y in range(yline):
            draw_line(int(rectangle.x),y*spacing,int(rectangle.width),y*spacing,color)
    draw_rectangle_lines_ex(rectangle,1,color)


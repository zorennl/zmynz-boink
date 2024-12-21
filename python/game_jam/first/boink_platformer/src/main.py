from pyray import *
from time import sleep


class player:
    def __init__(self, x, y, yVel):
        self.x = x
        self.y = y
        self.yVel = yVel
    def setSides(self):
        self.top = (self.x+25,self.y)
        self.bottom = (self.x+25,self.y+50)
        self.left = (self.x,self.y+25)
        self.right = (self.x+50,self.y+25)
    def draw(self):
        draw_rectangle(self.x,self.y,50,50,RED)

class platform:
    def __init__(self, x, y, length, height):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
    def isIn(self,pos):
        if pos[0] > self.x and pos[0] < self.x+self.length:
            if pos[1] > self.y and pos[1] < self.y+self.height:
                return True
            else: return False
        else: return False
    def draw(self):
        draw_rectangle(self.x,self.y,self.length,self.height,GREEN)

def stats():
    mx = get_mouse_x()
    my = get_mouse_y()
    
    draw_text(f'mx: {mx}, my: {my}',10,10,20,BLACK)
    draw_text(f'px: {you.x}, py: {you.y}',10,40,20,BLACK)
    draw_text(f'bottom: {you.bottom}',10,70,20,BLACK)
    draw_text(f'bottom in?: {platform_1.isIn(you.bottom)}',10,100,20,BLACK)

you = player(50,150,0)
platform_1 = platform(0,400,300,100)

init_window(500, 500, "platformer")
while not window_should_close():
    begin_drawing()
    sleep(.005)
    clear_background(WHITE)
#SET SPECIAL STUFF IDK
    you.setSides()

#KEYBOaRD
    you.x += is_key_down(KEY_D)-is_key_down(KEY_A)
    if platform_1.isIn(you.bottom):
        you.yVel = 0
    else: you.yVel += 2
    
    if is_key_pressed(KEY_SPACE):
        you.yVel = -32
    you.y += you.yVel


    stats()
    you.draw()
    platform_1.draw()
    end_drawing()
close_window()
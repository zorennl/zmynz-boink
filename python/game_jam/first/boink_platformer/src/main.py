from pyray import *
from time import sleep


class player:
    def __init__(self, x, y, yVel):
        self.x = x
        self.y = y
        self.yVel = yVel
    def setSides(self,dist):
        self.top = (self.x+25+dist,self.y+dist)
        self.bottom = (self.x+25+dist,self.y+50+dist)
        self.left = (self.x+dist,self.y+25+dist)
        self.right = (self.x+50+dist,self.y+25+dist)
    def draw(self):
        draw_rectangle(int(self.x),int(self.y),50,50,RED)

class platform:
    def __init__(self, x, y, length, height):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
    def isIn(self,pos):
        x = int(pos[0])
        y = int(pos[1])
        if x > self.x and x < self.x+self.length:
            if y > self.y and y < self.y+self.height:
                return True
            else: return False
        else: return False
    def draw(self):
        draw_rectangle(self.x,self.y,self.length,self.height,GREEN)

def stats():
    mx = get_mouse_x()
    my = get_mouse_y()
    
    draw_text(f'mx: {mx}, my: {my}',10,10,20,BLACK)
    draw_text(f'px: {you.x}, py: {you.y}, pyVel: {you.yVel}',10,40,20,BLACK)
    draw_text(f'bottom: {you.bottom}',10,70,20,BLACK)
    draw_text(f'bottom in?: {platform_1.isIn(you.bottom)}',10,100,20,BLACK)

you = player(50,150,0)
platform_1 = platform(0,400,300,100)

init_window(500, 500, "platformer") #? INITIATE
while not window_should_close():
    begin_drawing()
    sleep(.02)
    clear_background(WHITE)


#KEYBOaRD

    you.x += 2*(is_key_down(KEY_D)-is_key_down(KEY_A))
    you.yVel += 2
    if is_key_pressed(KEY_SPACE):
        you.yVel = -24
    you.y += you.yVel
    you.setSides(1)
    if platform_1.isIn(you.bottom) and you.yVel > 0:
        you.y = platform_1.y-50
        you.yVel = 0
        


    stats()
    you.draw()
    platform_1.draw()
    end_drawing()
close_window()
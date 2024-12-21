from pyray import *
from time import sleep


class player:
    def __init__(self, x, y, xVel, yVel):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
    def setSides(self,dist):
        self.top = (self.x+25+dist,self.y+dist)
        self.bottom = (self.x+25+dist,self.y+50+dist)
        self.left = (self.x+dist,self.y+25+dist)
        self.right = (self.x+50+dist,self.y+25+dist)
    def draw(self):
        draw_rectangle(int(self.x),int(self.y),50,50,RED)
    def drawSides(self):
        draw_rectangle(int(self.top[0]),int(self.top[1]-4),4,4,ORANGE)
        draw_rectangle(int(self.bottom[0]),int(self.bottom[1]+4),4,4,ORANGE)
        draw_rectangle(int(self.left[0]-4),int(self.left[1]),4,4,ORANGE)
        draw_rectangle(int(self.right[0]+4),int(self.right[1]),4,4,ORANGE)

class platform:
    def __init__(self, x, y, length, height, color=GREEN):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.color = color
    def isIn(self,pos):
        x = int(pos[0])
        y = int(pos[1])
        if x > self.x and x < self.x+self.length:
            if y > self.y and y < self.y+self.height:
                return True
            else: return False
        else: return False
    def draw(self):
        draw_rectangle(self.x,self.y,self.length,self.height,self.color)

def stats():
    mx = get_mouse_x()
    my = get_mouse_y()
    
    draw_text(f'mx: {mx}, my: {my}',10,10,20,BLACK)
    draw_text(f'px: {round(you.x,3)}, py: {you.y}',10,40,20,BLACK)
    draw_text(f'xVel: {round(you.xVel,3)}, yVel: {you.yVel}', 10, 70, 20, BLACK)

    #you.drawSides()

def movement(acce;):
    you.xVel += 16*(is_key_down(KEY_D)-is_key_down(KEY_A))
    you.yVel += 2
    if is_key_pressed(KEY_SPACE):
        for platf in room_1:
           if platf.isIn(you.bottom):
            you.yVel = -24
    you.xVel -= .8*you.xVel
    you.x += you.xVel
    you.y += you.yVel
    you.setSides(1)
winWidth = 1000
winHeight = 1000

you = player(50,150,0,0)
platform_1 = platform(0,400,350,100)
platform_2 = platform(300,300,200,200,PINK)
platform_3 = platform(400,600,500,200,BLUE)
platform_4 = platform(550,900,450,100,YELLOW)

scrLeft = platform(0,0,5,winHeight,color=BLACK)
scrRight = platform(winWidth-5,0,5,winHeight,color=BLACK)
scrTop = platform(0,0,winWidth,5,color=BLACK)
scrBottom = platform(0,winHeight-5,5,winHeight,color=BLACK)
screenWalls = [scrLeft,scrRight,scrTop,scrBottom]


room_1 = [platform_1,platform_2,platform_3,platform_4] + screenWalls
init_window(winWidth, winHeight, "platformer") #? INITIATE
while not window_should_close():
    begin_drawing()
    sleep(.02)
    clear_background(WHITE)


#KEYBOaRD
    movement()

    if is_key_pressed(KEY_R):
        you.x = 50
        you.y = 150
        you.yVel = 0
##COLISION
    for platf in room_1:
        if platf.isIn(you.bottom) and you.yVel > 0: #floor
            you.y = platf.y-50
            you.yVel = 0
    for platf in room_1:
        if platf.isIn(you.top) and you.yVel < 0: #ceiling
            you.y = platf.y+platf.height
            you.yVel = 0
    for platf in room_1:
        if platf.isIn(you.right) and you.xVel > 0: #right walls
            you.x = platf.x-50
            you.xVel = 0
    for platf in room_1:
        if platf.isIn(you.left) and you.xVel < 0: #left walls
            you.x = platf.x+platf.length
            you.xVel = 0
    for platf in room_1:
        platf.draw()

    you.draw()
    stats()
    end_drawing()
close_window()
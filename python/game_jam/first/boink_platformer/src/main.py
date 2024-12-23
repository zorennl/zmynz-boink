from pyray import *
from time import sleep


class player:
    def __init__(self, x, y, xVel, yVel, color = RED):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.color = color
        self.hitbox = platform(self.x+1,self.y+1,48,48,self.color)

    def setSides(self,dist):
        self.top = (self.x+25+dist,self.y+dist)
        self.bottom = (self.x+25+dist,self.y+50+dist)
        self.left = (self.x+dist,self.y+25+dist)
        self.right = (self.x+50+dist,self.y+25+dist)

    def setHitbox(self):
        self.hitbox.x = int(self.x+1)
        self.hitbox.y = int(self.y+1)

    def draw(self):
        draw_rectangle(int(self.x),int(self.y),50,50,self.color)

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

def movement(player,keys=[KEY_A,KEY_D,KEY_SPACE],accel=16,grav=2,jumpStr=24):
    player.xVel += accel*(is_key_down(keys[1])-is_key_down(keys[0]))
    player.yVel += grav
    if is_key_pressed(keys[2]):
        for platf in room_1:
           if platf.isIn(player.bottom):
            player.yVel = -1*jumpStr
    player.xVel -= .8*player.xVel
    player.x += player.xVel
    player.y += player.yVel
    player.setSides(1)

def collision(player):
    player.setHitbox()
    for platf in room_1:
        if platf.isIn(player.bottom) and player.yVel > 0: #floor
            player.y = platf.y-50
            player.yVel = 0
    for platf in room_1:
        if platf.isIn(player.top) and player.yVel < 0: #ceiling
            player.y = platf.y+platf.height
            player.yVel = 0
    for platf in room_1:
        if platf.isIn(player.right): #right walls
            player.x = platf.x-50
            player.xVel = 0
    for platf in room_1:
        if platf.isIn(player.left): #left walls
            player.x = platf.x+platf.length
            player.xVel = 0


winWidth = 1000
winHeight = 1000

you = player(50,350,0,0)
them = player(150,350,0,0,DARKBLUE)
third = player(250,350,0,0,DARKGREEN)

you.setHitbox()
them.setHitbox()

platform_1 = platform(0,400,350,100)
platform_2 = platform(300,300,200,200,PINK)
platform_3 = platform(400,600,500,200,BLUE)
platform_4 = platform(550,900,450,100,YELLOW)
platform_5 = platform(100,700,300,100,PURPLE)
platform_6 = platform(200,600,120,100,SKYBLUE)

scrLeft = platform(0,0,5,winHeight,color=BLACK)
scrRight = platform(winWidth-5,0,5,winHeight,color=BLACK)
scrTop = platform(0,0,winWidth,5,color=BLACK)
scrBottom = platform(0,winHeight-5,5,winHeight,color=BLACK)
screenWalls = [scrLeft,scrRight,scrTop,scrBottom]


room_1 = [platform_1,platform_2,platform_3,platform_4,platform_5,platform_6] + screenWalls + [you.hitbox,them.hitbox]
init_window(winWidth, winHeight, "platformer") #? INITIATE
while not window_should_close():
    begin_drawing()
    sleep(.02)
    clear_background(WHITE)

    movement(you,keys=[KEY_A,KEY_D,KEY_W])
    movement(them,keys=[KEY_LEFT,KEY_RIGHT,KEY_UP])

    if is_key_pressed(KEY_R):
        you.x = 50
        you.y = 350
        you.yVel = 0
        them.x = 150
        them.y = 350
        them.yVel = 0

#COLLISON
    collision(you)
    collision(them)

    for platf in room_1:
        platf.draw()

    you.draw()
    them.draw()

    stats()
    end_drawing()
close_window()
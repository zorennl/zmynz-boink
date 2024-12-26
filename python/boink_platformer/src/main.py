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
        self.movement = movementSettings()


    def setSides(self,dist):
        self.top = [(self.x+5+dist,self.y+dist),
        (self.x+25+dist,self.y+dist),
        (self.x+45+dist,self.y+dist)]
        self.bottom = [(self.x+5+dist,self.y+50+dist),
        (self.x+25+dist,self.y+50+dist),
        (self.x+45+dist,self.y+50+dist)]
        self.left = (self.x+dist,self.y+25+dist)
        self.right = (self.x+50+dist,self.y+25+dist)

    def setHitbox(self):
        self.hitbox.x = int(self.x+1)
        self.hitbox.y = int(self.y+1)

    def draw(self):
        draw_rectangle(int(self.x),int(self.y),50,50,self.color)

class movementSettings:
        def __init__(self, gravity=2, xAcceleration=16, jumpStrength=24, coyoteTime=5, jumps=1):
            self.gravity = gravity
            self.xAcceleration = xAcceleration
            self.jumpStrength = jumpStrength
            self.coyoteTime = coyoteTime
            self.jumps = jumps
            self.airTime = 0

class platform:
    def __init__(self, x, y, length, height, color=GREEN, tags = {}):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.color = color
        self.tags = tags
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

def movement(player,keys=[KEY_A,KEY_D,KEY_SPACE]):
    player.xVel += player.movement.xAcceleration*(is_key_down(keys[1])-is_key_down(keys[0]))
    player.yVel += player.movement.gravity
    if is_key_pressed(keys[2]):
        if player.movement.airTime <= player.movement.coyoteTime:
            player.yVel = -1*player.movement.jumpStrength
    player.xVel -= .8*player.xVel
    player.x += player.xVel
    player.y += player.yVel
    player.setSides(1)
    player.movement.airTime += 1

def collision(player):
    player.setHitbox()
    for platf in room_1:
#floor
        if platf.isIn(player.bottom[0]) | platf.isIn(player.bottom[1]) | platf.isIn(player.bottom[2]) and player.yVel > 0:
            player.y = platf.y-50
            player.yVel = 0
            player.movement.airTime = 0
#ceiling
        if platf.isIn(player.top[0]) | platf.isIn(player.top[1]) | platf.isIn(player.top[2]) and player.yVel < 0:
            player.y = platf.y+platf.height
            player.yVel = 0
    player.setHitbox()
    player.setSides(1)
    for platf in room_1: 
#right walls
        if platf.isIn(player.right):
            player.x = platf.x-50
            player.xVel = 0
#left walls
        if platf.isIn(player.left):
            player.x = platf.x+platf.length
            player.xVel = 0


winWidth = 1000
winHeight = 1000

you = player(50,350,0,0)
them = player(150,350,0,0,DARKBLUE)
third = player(250,350,0,0,DARKGREEN)

print(you.movement)

you.setHitbox()
them.setHitbox()

platform_1 = platform(0,400,350,100)
platform_2 = platform(300,300,200,200,PINK)
platform_3 = platform(400,600,500,200,BLUE)
platform_4 = platform(550,900,450,100,YELLOW)
platform_5 = platform(100,700,300,100,PURPLE)
platform_6 = platform(200,600,120,100,SKYBLUE)

scrLeft = platform(-45,0,50,winHeight,color=BLACK)
scrRight = platform(winWidth-5,0,50,winHeight,color=BLACK)
scrTop = platform(0,-45,winWidth,50,color=BLACK)
scrBottom = platform(0,winHeight-5,winWidth,50,color=BLACK)
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
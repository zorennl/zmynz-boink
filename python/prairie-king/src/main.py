from pyray import *
from os.path import join as os
import math as m
import random as rd
captcha = []
symbols = "abcdefghijklmnopqrtstuvwxyzABCDEFGHIJKLMNOPQRSTUVYXZ1234567890!@#$%^&*()-=_+"
for i in range(5):
    captcha.append(symbols[rd.randint(0,len(symbols)-1)])
captcha = "".join(captcha)

class player:
    def __init__(self,x,y,texture: str):
        self.x = x
        self.y = y
        self.texture = load_texture(texture)
        self.vx = 0
        self.vy = 0
    def draw(self):
        draw_texture_ex(self.texture,Vector2(self.x,self.y),0,2,WHITE)
    def move(self,vx,vy):
        self.vx, self.vy = vx, vy
        if self.vx != 0:
            vel = m.cos(m.atan(self.vy/self.vx)), m.sin(m.atan(self.vy/self.vx))
        else: vel = [0,self.vy]
        if vx < 0:
            vel = vel[0]*-1, vel[1]*-1
        self.vx, self.vy = vel
        self.x += self.vx
        self.y += self.vy

winWid = 512
winHgt = 512

init_window(winWid,winHgt,"CAPTCHA")
## CAPTCHA
text = ""
inbox = Rectangle(0,0,winWid,winHgt)
## WHY IN THE WORLD IS IT NOT ABLE TO KNOW WHAT VAR vscode IS WHAT
while not window_should_close():
        begin_drawing()
        clear_background(BLACK)
        a = gui_text_input_box(inbox,f"CAPTCHA: {captcha}","type captcha above here:","done",text,50,ffi.new("bool *", True))
        vscode = text
        draw_text(f"{vscode}",10,400,20,BLACK)
        if a == 1:
            vscode = (vscode == captcha)
            break
        end_drawing()

close_window()


init_window(winWid,winHgt,"prarie king python edition")

if vscode:
    print("loaded")
## ASSETS
    # TILES
    desert_tile = load_texture(os("assets","desert","tile.png"))

    # PLAYER
    cowboy = player(winWid/2,winHgt/2,os("assets","player","player.png"))
else:
    print("master boink! is it you?")
    desert_tile = load_texture(os("python\\prairie-king\\assets\\desert\\tile.png"))
    cowboy = player(winWid/2,winHgt/2,"python\\prairie-king\\assets\\player\\player.png")

## VARIABLES
biome = "desert"


set_target_fps(60)

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    ## SET BACKROUND
    for y in range(32):
        for x in range(32):
            draw_texture_ex(eval(f"{biome}_tile"),Vector2(x*16,y*16),0,2,WHITE)

    ## MOVEMENT
    cowboy.move((is_key_down(KEY_RIGHT)-is_key_down(KEY_LEFT)),
                (is_key_down(KEY_DOWN)-is_key_down(KEY_UP)))
    
    ## DEBUG
    draw_text(f"""
pos: {cowboy.x,cowboy.y},
vel: {cowboy.vx, cowboy.vy}
                    """,0,0,20,PURPLE)



    ## DRAW PLAYER
    cowboy.draw()
    








    end_drawing()
close_window()
from pyray import *
import math as m

buls = []

## feel free to replace my arrays with vectors
## pyray is being weird so i cant check how they work :sob:

class Bullet: 
    def __init__(self, pos, theta, speed, btype=None):
        self.pos = pos
        self.theta = theta
        self.speed = speed
        self.btype = btype
    
    def move(this):
        this.pos[0] += m.cos(this.theta) * this.speed
        this.pos[1] += m.sin(this.theta) * this.speed

        if this.btype == 0:
            pass
        elif this.btype == 1:
            pass
        # so on so forth
    
    def attack(this, obj):
        obj.healt -= 1

        if this.btype != 1: # piercing, however we plan on that working
            buls.remove(this)
        # you could also add other effects here

    def draw(this):
        p = Vector2(this.pos[0],this.pos[1])

        draw_rectangle_v(p, Vector2(5, 5), RED) # red cuz why not?

# obv set these to actually thingies
px, py, pd = 250, 250 ,0
ammo = 10000
switch = True
spedd = 1
cooldown = 0
# px, py = player position
# pd = player facing direction
# spedd = bullet speed, could be changed inside the bullet thing absed off of type
# switch, unnecessary, default to true for 8dir

def shoot():
    global ammo, cooldown

    if switch:
        buls.append(Bullet([px, py], 45/180*m.pi * (pd // (45 / 180 * m.pi)), spedd))
    else:
        buls.append(Bullet([px, py], pd, spedd))

    ammo -= 1
    cooldown = 20

#? example code
"""
set_target_fps(60)
init_window(500, 500, "lmao")

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    if is_key_down(KeyboardKey.KEY_Q) & (cooldown <= 0):
        shoot()
    
    if is_key_pressed(KeyboardKey.KEY_E):
        switch = not switch

    pd += (is_key_down(KeyboardKey.KEY_D) - is_key_down(KeyboardKey.KEY_A)) / 180 * m.pi
    
    spedd += (is_key_down(KeyboardKey.KEY_W) - is_key_down(KeyboardKey.KEY_S)) / 5

    cooldown -= 1

    for b in buls:
        b.draw()
        b.move()

    draw_text(f"Direction: {round((pd/m.pi*180) % 360, 3)}", 10, 10, 20, BLACK)
    draw_text(f"Speed: {round(spedd, 2)}", 10, 40, 20, BLACK)
    #draw_text(f"q: {is_key_down(KeyboardKey.KEY_Q)}, cooldown: {cooldown}, both? {is_key_down(KeyboardKey.KEY_Q) & (cooldown == 0)}", 10, 70, 20, BLACK)
    end_drawing()
close_window()
"""

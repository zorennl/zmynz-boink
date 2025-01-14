from pyray import *
from random import randint, choice
from math import pi, cos, sin,floor

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

WINDOW_BOX = Rectangle(1, 1, 799, 499)

class particle:
    def __init__(self, pos: Vector2, radius, angle, speed, life: float, color):
        self.pos = pos
        self.radius = radius
        self.angle = angle
        self.speed = speed
        self.life = life
        self.color = color
        self.radians = self.angle * pi / 180

        self.velocity = Vector2(self.speed * cos(self.radians), -self.speed * sin(self.radians))
        
    def draw(dt, particlelist):
        for i in range(len(particlelist)):
            particlelist[i].life -= 1
            
            particlelist[i].color.a = abs(floor(particlelist[i].life * 0.1))
                                       
            if particlelist[i].life > 0:
                particlelist[i].pos.x += particlelist[i].velocity.x * dt
                particlelist[i].pos.y += particlelist[i].velocity.y * dt
                
                if particlelist[i].pos.y > 500 or particlelist[i].pos.y < 0:
                    particlelist[i].velocity.y *= -1
                
                if particlelist[i].pos.x < 0 or particlelist[i].pos.x > 800:
                    particlelist[i].velocity.x *= -1
                
                draw_circle_v(particlelist[i].pos,particlelist[i].radius,particlelist[i].color)      
                
                if particlelist[i].life == 0:
                    particlelist.pop(i) 

set_config_flags(FLAG_WINDOW_TRANSPARENT+FLAG_WINDOW_UNDECORATED)

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "particles")

set_target_fps(60)

particles = []

while not window_should_close():

    begin_drawing()
    clear_background(BLANK)

    draw_fps(2,2)
    
    if is_mouse_button_down(MOUSE_BUTTON_LEFT):
        for i in range(100):
           particles.append(particle(get_mouse_position(),5,randint(0,360),2,randint(100,400),Color(randint(0,255),randint(0,255),randint(0,255),255)))

    particle.draw(2, particles)

    draw_rectangle_lines_ex(WINDOW_BOX, 1, WHITE)
    end_drawing()

close_window()

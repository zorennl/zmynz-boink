test
from pyray import *
from sys import platform
import math
from os.path import join
import random

debug = False
# Entities
entities = [
    Rectangle(0,0,10,10),
    Rectangle(11,0,10,10),
    Rectangle(21,0,10,10)
]
# General entity class 
class Entity:
    def __init__(self, health, speed=float, sprite=None, source=None, rectangle=Rectangle, rotation=int,color=None, extra=None):
        self.health = health
        self.speed = speed
        self.sprite = sprite
        self.source = source
        self.rectangle = rectangle
        self.rotation = rotation
        self.color = color
        self.extra = extra

# Defining functions for entities
def summon_entity(entity, entity_list: []):
    entity_list.append(entity)   

def draw_entity_sprite(entity):
    draw_texture_pro(entity.sprite,entity.source,entity.rectangle,Vector2(0,0),entity.rotation,WHITE)

def draw_entity_rec(entity):
    draw_rectangle_rec(entity.rectangle,entity.color)

def get_direction(pos1,pos2):
    dx = pos1.x - pos2.x
    dy = pos1.y - pos2.y
    distance = math.sqrt(dx*dx+dy*dy)
    if distance < 10:
        return Vector2(0,0)
    else:
        return Vector2(dx/distance,dy/distance)

init_window(300,300,"raylib bees and hornets")
set_target_fps(60)

if platform == "win32":
    entity_atlas = load_texture('zaboing_games\\bees_and_hornets\\assets\\sprites.png')
else:
    entity_atlas = load_texture('assets/sprites.png')
bees = []
player = Entity(10,2,entity_atlas,entities[0],Rectangle(0,0,25,25),0,WHITE,None)
while not window_should_close():
    bee = Entity(10,random.choice([1.0,1.2,1.1,1.3,1.5,1.4,1.6,1.55]),entity_atlas,entities[1],Rectangle(200,200,15,15),0,WHITE,Vector2(0,0))

    if is_key_down(KEY_W):
        player.rectangle.y -= player.speed
    if is_key_down(KEY_S):
        player.rectangle.y += player.speed
    if is_key_down(KEY_A):
        player.rectangle.x -= player.speed
    if is_key_down(KEY_D):
        player.rectangle.x += player.speed

    if is_key_pressed(KEY_R):
        summon_entity(bee,bees)
    if is_key_pressed(KEY_F3):
        debug = not debug
    begin_drawing()
    clear_background(BLACK)

    draw_entity_sprite(player)
    for i in bees:
        draw_entity_sprite(i)
        i.extra = get_direction(Vector2(player.rectangle.x,player.rectangle.y),Vector2(i.rectangle.x,i.rectangle.y))
        if i.extra.x < 0:
            i.source.width = -10
        else:
            i.source.width = 10
        i.rectangle.x += i.speed * i.extra.x
        i.rectangle.y += i.speed * i.extra.y

    if debug:
        draw_text(f'bees:{len(bees)}',0,0,10,GREEN)
    end_drawing()

close_window()

from pyray import *
from sys import platform
import math
from os.path import join
import random

# Camera
camera = Camera2D()
camera.zoom = 1
camera.rotation = 0

# Rectangles for finding player position
position_rectangles = [
    Rectangle(20,20,10,10),
    Rectangle(270,20,10,10),
    Rectangle(20,270,10,10),
    Rectangle(270,270,10,10)
]

debug = False
# Entities
entities = [
    Rectangle(0,0,10,10),
    Rectangle(11,0,10,10),
    Rectangle(22,0,10,10)
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
    draw_texture_pro(entity.sprite,entity.source,entity.rectangle,Vector2(0,0),entity.rotation,entity.color)

def draw_entity_rec(entity):
    draw_rectangle_rec(entity.rectangle,entity.color)

def get_distance(pos1,pos2):
    dx = pos1.x - pos2.x
    dy = pos1.y - pos2.y
    distance = math.sqrt(dx*dx+dy*dy)
    return int(distance)

def get_direction(pos1,pos2):
    dx = pos1.x - pos2.x
    dy = pos1.y - pos2.y
    distance = math.sqrt(dx*dx+dy*dy)
    if distance < 10:
        return Vector2(0,0)
    else:        return Vector2(dx/distance,dy/distance)

init_window(300,300,"raylib bees and hornets")
set_target_fps(60)

if platform == "win32":
    entity_atlas = load_texture('zaboing_games\\bees_and_hornets\\assets\\sprites.png')
else:
    entity_atlas = load_texture('assets/sprites.png')
bees = []
beedest = Vector2(0,0)
minerals = []
# Player
player = Entity(10,2,entity_atlas,entities[0],Rectangle(138,138,25,25),0,WHITE,None)
mineral_counter = 0
while not window_should_close():
    camera.target = Vector2(player.rectangle.x-138,player.rectangle.y-138)

    bee = Entity(10,random.randint(10,15)/10,entity_atlas,entities[1],Rectangle(200,200,15,15),0,WHITE,Vector2(0,0))
    mineral = Entity(5,0,entity_atlas,entities[2],Rectangle(random.randint(-1000,1000),random.randint(-1000,1000),10,10),0,WHITE,Vector2(0,0))

    if is_key_down(KEY_W) and player.rectangle.y > -1000:
        player.rectangle.y -= player.speed
    if is_key_down(KEY_S) and player.rectangle.y < 1000:
        player.rectangle.y += player.speed
    if is_key_down(KEY_A) and player.rectangle.x > -1000:
        player.rectangle.x -= player.speed
    if is_key_down(KEY_D) and player.rectangle.x < 1000:
        player.rectangle.x += player.speed
    
    if is_mouse_button_down(MOUSE_BUTTON_LEFT):
        beedest = get_mouse_position()       

    if is_key_pressed(KEY_R):
        summon_entity(bee,bees)
    if is_key_down(KEY_F):
        summon_entity(mineral,minerals)
    if is_key_pressed(KEY_F3):
        debug = not debug
    begin_drawing()
    clear_background(BLACK)

    begin_mode_2d(camera)
    for i in minerals:
        draw_entity_sprite(i)
        if i.health == 1:
            i.color = RED
        if check_collision_recs(player.rectangle,i.rectangle) and i.health == 1:
            mineral_counter += 1
            i.health = 0
            del minerals[minerals.index(i)]
        for x in bees:
            if get_distance(i.rectangle,x.rectangle) < 50 and i.health > 1:
                # x.health -=1
                # if x.health == 0:
                #     x.health = 100
                i.health-=1
  
    draw_entity_sprite(player)

    for i in bees:
        draw_entity_sprite(i)
        i.extra = get_direction(Vector2(beedest.x+camera.target.x,beedest.y+camera.target.y),Vector2(i.rectangle.x,i.rectangle.y))
        if i.extra.x < 0:
            i.source.width = -10
        else:
            i.source.width = 10
        i.rectangle.x += i.speed * i.extra.x
        i.rectangle.y += i.speed * i.extra.y

    for i in position_rectangles:
        draw_rectangle_rec(i,WHITE)

    end_mode_2d()

    if debug:
        draw_text(f'x:{player.rectangle.x} y:{player.rectangle.y}\nbees:{len(bees)}\nminerals:{mineral_counter}',0,0,10,GREEN)
    end_drawing()

close_window()

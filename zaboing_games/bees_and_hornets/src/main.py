from pyray import *
from os.path import join

# Entities
entities = [
    Rectangle(0,0,10,10),
    Rectangle(11,0,10,10),
    Rectangle(21,0,10,10)
]
# General entity class 
class Entity:
    def __init__(self, health, sprite=None, source=None, rectangle=Rectangle, color=None, extra=None):
        self.health = health
        self.sprite = sprite
        self.source = source
        self.rectangle = rectangle
        self.color = color
        self.extra = extra

# Defining functions for entities
def summon_entity(entity, entity_list: []):
    entity_list.append(entity)   

def draw_entity_sprite(entity):
    draw_texture_pro(entity.sprite,entity.source,entity.rectangle,Vector2(entity.rectangle.x/2,entity.rectangle.y/2),0,WHITE)

def draw_entity_rec(entity):
    draw_rectangle_rec(entity.rectangle,entity.color)

init_window(300,300,"raylib bees and hornets")
set_target_fps(60)

entity_atlas = load_texture(join('assets','sprites.png'))
bee = Entity(10,entity_atlas,entities[1],Rectangle(200,200,10,10),WHITE,None)
player = Entity(10,entity_atlas,entities[0],Rectangle(100,100,20,20),WHITE,None)
while not window_should_close():
    if is_key_down(KEY_W):
        player.rectangle.y -= 1
    if is_key_down(KEY_S):
        player.rectangle.y += 1
    if is_key_down(KEY_A):
        player.rectangle.x -= 1
    if is_key_down(KEY_D):
        player.rectangle.x += 1

    begin_drawing()
    clear_background(BLACK)

    draw_entity_sprite(bee)
    draw_entity_sprite(player)

    end_drawing()

close_window()

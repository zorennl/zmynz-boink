from pyray import *

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
    draw_texture_pro(entity.sprite,entity.source,entity.rectangle,Vector2(entity.rectangle.x,entity.rectangle.y),0,WHITE)

def draw_entity_rec(entity):
    draw_rectangle_rec(entity.rectangle,entity.color)

init_window(300,300,"raylib bees and hornets")
set_target_fps(60)

while not window_should_close():

    begin_drawing()
    clear_background(BLACK)



    end_drawing()

close_window()

from pyray import *


class Entity:
    def __init__(
        self, traits=[], direction=None, speed=float, rectangle=Rectangle, color=Color
    ):
        self.traits = traits
        self.direction = direction
        self.speed = speed
        self.rectangle = rectangle
        self.color = color

    def draw(self):
        draw_rectangle_rec(self.rectangle, self.color)

    def control(
        self, up=KeyboardKey, down=KeyboardKey, left=KeyboardKey, right=KeyboardKey
    ):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        if is_key_down(up):
            self.direction.y = -1
        elif is_key_down(down):
            self.direction.y = 1
        else:
            self.direction.y = 0
        if is_key_down(left):
            self.direction.x = -1
        elif is_key_down(right):
            self.direction.x = 1
        else:
            self.direction.x = 0

        self.rectangle.x += self.direction.x * self.speed
        self.rectangle.y += self.direction.y * self.speed


init_window(100, 100, "trees and traits")
set_target_fps(60)

tree = Entity([], Vector2(0, 0), 0, Rectangle(45, 45, 10, 10), GREEN)
player = Entity([], Vector2(0, 0), 2, Rectangle(5, 5, 5, 5), WHITE)

while not window_should_close():
    # player.x += player_direction.x * player_speed
    # player.y += player_direction.y * player_speed

    # if is_key_down(KEY_W):
    #     player_direction.y = -1
    # if is_key_down(KEY_S):
    #     player_direction.y = 1
    # else:
    #     player_direction.y = 0

    player.control(KEY_W, KEY_S, KEY_A, KEY_D)

    begin_drawing()
    clear_background(BLACK)

    tree.draw()
    player.draw()

    end_drawing()
close_window()

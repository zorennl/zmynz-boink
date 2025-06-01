from pyray import *


class Tree:
    def __init__(self, rectangle: Rectangle, color: Color):
        self.rectangle = rectangle
        self.color = color

    def draw(self):
        draw_rectangle_rec(self.rectangle, self.color)


init_window(100, 100, "game")
set_target_fps(60)

tree = Tree(Rectangle(45, 45, 10, 10), GREEN)

player = Rectangle(10, 10, 5, 5)
player_direction = Vector2(0, 0)
player_speed = 2

while not window_should_close():
    player.x += player_direction.x * player_speed
    player.y += player_direction.y * player_speed

    if is_key_down(KEY_W):
        player_direction.y = -1
    if is_key_down(KEY_S):
        player_direction.y = 1
    else:
        player_direction.y = 0

    begin_drawing()
    clear_background(BLACK)

    tree.draw()
    draw_rectangle_rec(player, WHITE)

    end_drawing()
close_window()

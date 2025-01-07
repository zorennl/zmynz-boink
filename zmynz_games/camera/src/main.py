from pyray import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

player = Rectangle(0, 0, 100, 100)
obstacle = Rectangle(50, 50, 100, 100)

camera = Camera2D()
# camera.offset = Vector2(350, 200)
camera.rotation = 0
camera.zoom = 1

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "camera")

set_target_fps(60)

while not window_should_close():
    if is_key_down(KEY_W):
        player.y -= 2
    if is_key_down(KEY_S):
        player.y += 2
    if is_key_down(KEY_D):
        player.x += 2
    if is_key_down(KEY_A):
        player.x -= 2
    
    camera.target = Vector2(player.x - 350, player.y - 200)
    
    begin_drawing()
    clear_background(BLACK)
    
    begin_mode_2d(camera)

    draw_rectangle_rec(player, RED)
    draw_rectangle_rec(obstacle, WHITE)
    draw_rectangle_rec(get_collision_rec(player, obstacle), GREEN)
    
    end_mode_2d()
    
    end_drawing()

close_window()

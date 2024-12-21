from pyray import *

init_window(800, 450, "texture")
set_target_fps(60)
texture = load_texture("/home/zmynz/vss/git-repo/zmynz-boink/python/texture/assets/sprite.png")
while not window_should_close():
    begin_drawing()
    draw_texture(texture, 50, 50, WHITE)
    end_drawing()

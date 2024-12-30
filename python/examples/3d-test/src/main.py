from pyray import *

init_window(800, 500, "3D")

camera = Camera3D(Vector3(1000, 1000, 1000), Vector3(0, 0, 0), Vector3(0, 1, 0), 90, CAMERA_PERSPECTIVE)
cubepos = Vector3(0,0,0)
set_target_fps(60)

while not window_should_close():
    begin_mode_3d(camera)
    begin_drawing()
    clear_background(WHITE)

    draw_cube(cubepos, 100, 100, 100, BLACK)

    if is_key_down(KEY_A):
        cubepos.x -= 2
    if is_key_down(KEY_D):
        cubepos.x += 2
    if is_key_down(KEY_W):
        cubepos.y -= 2
    if is_key_down(KEY_S):
        cubepos.y += 2
    if is_key_down(KEY_Q):
        cubepos.z -= 2
    if is_key_down(KEY_E):
        cubepos.z += 2
    
    end_drawing()
    end_mode_3d()
close_window()

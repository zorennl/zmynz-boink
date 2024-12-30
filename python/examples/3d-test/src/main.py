from pyray import *

init_window(800, 500, "3D")

camerapos = Vector3(1000.0, 1000.0, 1000.0)

camera = Camera3D(Vector3(0, 0, 0), camerapos, Vector3(0, 45, 0), 90, CAMERA_ORTHOGRAPHIC)
cubepos = Vector3(0,0,0)
set_target_fps(60)

while not window_should_close():
    begin_mode_3d(camera)
    begin_drawing()
    clear_background(WHITE)
    draw_cube(cubepos, 100, 100, 100, BLACK)
    draw_cube_wires(cubepos, 100, 100, 100,RED)

    if is_key_down(KEY_A):
        cubepos.x -= 2
    if is_key_down(KEY_D):
        cubepos.x += 2
    if is_key_down(KEY_W):
        cubepos.y += 2
    if is_key_down(KEY_S):
        cubepos.y -= 2
    if is_key_down(KEY_Q):
        cubepos.z -= 2
    if is_key_down(KEY_E):
        cubepos.z += 2

    if is_key_down(KEY_G):
        camerapos.x -= 2
    if is_key_down(KEY_J):
        camerapos.x += 2
    if is_key_down(KEY_Y):
        camerapos.y -= 2
    if is_key_down(KEY_H):
        camerapos.y += 2
    if is_key_down(KEY_U):
        camerapos.z -= 2
    if is_key_down(KEY_I):
        camerapos.z += 2
    end_mode_3d()
    draw_grid(10, 1)    
    end_drawing()
close_window()

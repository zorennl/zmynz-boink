from pyray import *
import math as m


class player:
    def __init__(self,pos,target,rot=[0,90]):
        self.pos = pos
        self.target = target
        self.rot = rot
        self.camera = Camera3D(
            Vector3(self.pos[0], self.pos[1], self.pos[2]),
            Vector3(self.target[0], self.target[1], self.target[2]),
            Vector3(0,1,0), #up
            90, #fov
            CameraProjection.CAMERA_PERSPECTIVE)
    def move(self):

        you.pos[0] += is_key_down(KEY_W)-is_key_down(KEY_S)
        you.pos[1] += is_key_down(KEY_Q)-is_key_down(KEY_E)
        you.pos[2] += is_key_down(KEY_D)-is_key_down(KEY_A)

        update_camera_pro(self.camera,
                          Vector3(self.pos[0], self.pos[1], self.pos[2]),
                          Vector3(0,0,0),
                          0)
    def __str__(self):
        return f"pos: {self.pos}, rot: {self.rot}"


you = player([0,0,0],[10,0,0])

init_window(1600,900,"a")

while not window_should_close():
    
    begin_drawing()
    begin_mode_3d(you.camera)
    clear_background(WHITE)

    you.move()
    draw_cube(Vector3(0,0,0),10,10,10,RED)

    


    

    end_mode_3d()

    draw_text(f"you: {you}",0,0,20,PURPLE)
    end_drawing()
    
close_window()
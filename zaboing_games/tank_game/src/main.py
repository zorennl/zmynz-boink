from pyray import *

class Tank:
    def __init__(self,sprite=Texture2D,position=Vector2,size=float,speed=float,controls=[],color=Color):
        self.sprite = sprite
        self.position = position
        self.size = size
        self.speed = speed
        self.controls = controls
        self.color = color
        self.mv_direction = 0
        self.direction = 0

    def move(self):
        mv_directions = [
            Vector2(0, 1),    # top
            Vector2(-1, 1),   # top-left
            Vector2(-1, 0),   # left
            Vector2(-1, -1),  # bottom-left
            Vector2(0, -1),   # bottom
            Vector2(1, -1),   # bottom-right
            Vector2(1, 0),    # right
            Vector2(1, 1)     # top-right
        ]

        if is_key_pressed(self.controls[1]) and self.mv_direction == 0:
            self.mv_direction = 7
        elif is_key_pressed(self.controls[3]) and self.mv_direction == 7:
            self.mv_direction = 0
        elif is_key_pressed(self.controls[1]):
            self.mv_direction -= 1
        elif is_key_pressed(self.controls[3]):
            self.mv_direction += 1

        if is_key_down(self.controls[2]):
            self.position.x += mv_directions[self.mv_direction].x*self.speed
            self.position.y += mv_directions[self.mv_direction].y*self.speed
        if is_key_down(self.controls[0]):
            self.position.x -= mv_directions[self.mv_direction].x*self.speed
            self.position.y -= mv_directions[self.mv_direction].y*self.speed

          
    def draw(self):
        directions = [0, 45, 90, 135, 180, 225, 270, 315, 360]
      
        if is_key_pressed(self.controls[1]) and self.direction == 0:
            self.direction = 7
        elif is_key_pressed(self.controls[3]) and self.direction == 7:
            self.direction = 0
        elif is_key_pressed(self.controls[1]):
            self.direction -= 1
        elif is_key_pressed(self.controls[3]):
            self.direction += 1

        draw_texture_pro(self.sprite,Rectangle(0,0,100,100),Rectangle(self.position.x,self.position.y,10,10),Vector2(5,5),directions[self.direction],self.color)

init_window(500,500,"tank game")
set_target_fps(60)

tank_texture = load_texture("assets/tank_texture.png")

player = Tank(tank_texture,Vector2(250,250),.1,2,[KEY_W,KEY_A,KEY_S,KEY_D],WHITE)
while not window_should_close():
    begin_drawing()
    clear_background(BLANK)

    player.draw()
    player.move()

    end_drawing()
close_window()

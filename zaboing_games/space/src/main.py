import pyray as r

scale = 1

class Planet:
    def __init__(self, position=r.Vector2, radius=float, color=r.Color, mass=float):
        self.position = position
        self.radius = radius
        self.color = color
        self.mass = mass

    def draw(self):
        r.draw_circle_v(r.vector2_multiply(self.position, (scale, scale)), (self.radius * scale), self.color)


sun = Planet(r.Vector2(500, 500), 100, r.YELLOW, 100)

mercury = Planet(r.Vector2(500 + 150, 500), 0.35 * 2, r.GRAY, 10)
venus = Planet(r.Vector2(500 + 200, 500), 0.87 * 2, r.ORANGE, 20)
earth = Planet(r.Vector2(500 + 250, 500), 0.92 * 2, r.BLUE, 30)
mars = Planet(r.Vector2(500 + 300, 500), 0.49 * 2, r.RED, 40)
jupiter = Planet(r.Vector2(500 + 400, 500), 10.05 * 2, r.BROWN, 50)
saturn = Planet(r.Vector2(500 + 500, 500), 8.37 * 2, r.LIGHTGRAY, 60)
uranus = Planet(
    r.Vector2(500 + 600, 500), 3.65 * 2, r.Color(0, 255, 255, 255), 70
)  # Using custom cyan
neptune = Planet(r.Vector2(500 + 700, 500), 3.54 * 2, r.DARKBLUE, 80)

player_pos = r.Vector2(1000*scale, 1000*scale)
player_color = r.WHITE
player_size = 10*scale
player_speed = 1*scale
player_direction = r.Vector2(1, -1)
player_velocity = r.Vector2(0.0, 0.0)

cursor_size = 5*scale
cursor_color = r.Color(255, 255, 255, 50)

r.init_window(int(2000/(scale**-1)), int(2000/(scale**-1)), "space")
r.disable_cursor()
r.set_target_fps(60)

while not r.window_should_close():
    cursor_pos = r.get_mouse_position()

    if r.is_key_down(r.KEY_SPACE):
        player_velocity.x += player_speed * player_direction.x
        player_velocity.y += player_speed * player_direction.y

    player_pos.x += player_velocity.x
    player_pos.y += player_velocity.y

    r.begin_drawing()
    r.clear_background(r.BLACK)

    sun.draw()

    mercury.draw()
    venus.draw()
    earth.draw()
    mars.draw()
    jupiter.draw()
    saturn.draw()
    uranus.draw()
    neptune.draw()

    r.draw_circle_v(player_pos, player_size, player_color)
    r.draw_circle_v(cursor_pos, cursor_size, cursor_color)

    r.end_drawing()
r.close_window()

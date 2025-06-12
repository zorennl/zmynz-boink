import pyray as r
import math

scale = 0.5


class Planet:
    def __init__(
        self, name, position=r.Vector2, radius=float, color=r.Color, mass=float
    ):
        self.name = name
        self.position = position
        self.radius = radius
        self.color = color
        self.mass = mass

    def draw(self):
        r.draw_circle_v(
            r.vector2_multiply(self.position, (scale, scale)),
            (self.radius * scale),
            self.color,
        )


def get_direction(origin=r.Vector2, target=r.Vector2):
    direction = r.Vector2(target.x - origin.x, target.y - origin.y)
    return direction


def get_distance(origin=r.Vector2, target=r.Vector2):
    dx = origin.x * origin.x + target.x * target.x
    dy = origin.y * origin.y + target.y * target.y
    distance = (dx + dy) ** (1 / 2)
    return distance


planets = [
    Planet("sun", r.Vector2(500, 500), 100, r.YELLOW, 100),
    Planet("mercury", r.Vector2(500 + 150, 500), 0.35 * 2, r.GRAY, 10),
    Planet("venus", r.Vector2(500 + 200, 500), 0.87 * 2, r.ORANGE, 20),
    Planet("earth", r.Vector2(500 + 250, 500), 0.92 * 2, r.BLUE, 30),
    Planet("mars", r.Vector2(500 + 300, 500), 0.49 * 2, r.RED, 40),
    Planet("jupiter", r.Vector2(500 + 400, 500), 10.05 * 2, r.BROWN, 50),
    Planet("saturn", r.Vector2(500 + 500, 500), 8.37 * 2, r.LIGHTGRAY, 60),
    Planet(
        "uranus", r.Vector2(500 + 600, 500), 3.65 * 2, r.Color(0, 255, 255, 255), 70
    ),
    Planet("neptune", r.Vector2(500 + 700, 500), 3.54 * 2, r.DARKBLUE, 80),
]

player_pos = r.Vector2(1000 * scale, 1000 * scale)
player_color = r.WHITE
player_size = 10 * scale
player_speed = 70
player_direction = 0
player_velocity = r.Vector2(0.0, 0.0)
player_throttle = 0
player_turn_speed = 0.01

cursor_size = 5 * scale
cursor_color = r.Color(255, 255, 255, 50)

WIDTH = int(2000 / (scale**-1))
HEIGHT = int(2000 / (scale**-1))

r.init_window(WIDTH, HEIGHT, "space")
r.disable_cursor()
r.set_target_fps(60)

while not r.window_should_close():
    cursor_pos = r.get_mouse_position()

    # player_direction = get_direction(cursor_pos, player_pos)
    # player_speed = get_distance(cursor_pos, player_pos)

    if r.is_key_down(r.KEY_LEFT_SHIFT) and player_throttle < 100:
        player_throttle += 1
    if r.is_key_down(r.KEY_LEFT_CONTROL) and player_throttle > 0:
        player_throttle -= 1

    if r.is_key_down(r.KEY_Q):
        player_direction += player_turn_speed
    if r.is_key_down(r.KEY_E):
        player_direction -= player_turn_speed

    if r.is_key_down(r.KEY_SPACE):
        player_velocity.x -= math.sin(player_direction) * player_throttle / player_speed
        player_velocity.y -= math.cos(player_direction) * player_throttle / player_speed

    if player_pos.x > WIDTH or player_pos.x < 0:
        player_velocity.x *= -1
    if player_pos.y > HEIGHT or player_pos.y < 0:
        player_velocity.y *= -1

    player_pos.x += player_velocity.x
    player_pos.y += player_velocity.y

    r.begin_drawing()
    r.clear_background(r.BLACK)

    for i in planets:
        i.draw()
        if r.check_collision_circles(i.position, i.radius, player_pos, player_size):
            player_direction += 180
    r.draw_circle_v(player_pos, player_size, player_color)
    r.draw_circle_v(
        r.vector2_subtract(
            player_pos,
            (10 * math.sin(player_direction), 10 * math.cos(player_direction)),
        ),
        player_size // 5,
        player_color,
    )
    r.draw_circle_v(cursor_pos, cursor_size, cursor_color)

    r.draw_rectangle_rec(
        r.Rectangle(10, (HEIGHT - 10) - player_throttle, 10, player_throttle), r.GREEN
    )
    r.draw_text(f"Throttle:{player_throttle}%", 25, HEIGHT - 20, 10, r.GREEN)

    r.end_drawing()
r.close_window()

import pyray as r

WINDOW_WIDHT = 500
WINDOW_HEIGHT = 500


class Particle:
    def __init__(self, pos, radius, color, velocity, direction):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.velocity = velocity
        self.direction = direction


def draw(particlelist):
    for i in particlelist:
        r.draw_circle_v(i.pos, i.radius, i.color)
        i.pos.y += i.velocity
        if not r.check_collision_circle_rec(
            i.pos, i.radius, r.Rectangle(0, 0, WINDOW_WIDHT, WINDOW_HEIGHT)
        ):
            particlelist.pop(particlelist.index(i))
        if i.pos.y > WINDOW_HEIGHT - i.radius:
            i.velocity = 0


particle_list = []

r.init_window(WINDOW_WIDHT, WINDOW_HEIGHT, "particle-sys v2")
r.set_target_fps(1000)

while not r.window_should_close():
    mouse_pos = r.get_mouse_position()
    if r.is_key_down(r.KEY_R):
        particle_list.append(Particle(mouse_pos, 10, r.WHITE, 1, r.Vector2(0, 0)))

    draw(particle_list)
    r.draw_text(f"particles:{len(particle_list)}", 0, 0, 10, r.GREEN)
    r.draw_fps(20,10,10)

    r.begin_drawing()
    r.clear_background(r.BLACK)

    r.end_drawing()
r.close_window()

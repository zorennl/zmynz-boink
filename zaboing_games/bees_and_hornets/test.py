from pyray import *

# Initialize the window
init_window(800, 600, "2D Mouse Position Relative to Camera")

# Camera setup (2D camera)
camera = Camera2D()
camera.target = Vector2(0, 0)  # Camera target (center of the screen)
camera.offset = Vector2(400, 300)  # Camera offset (screen center)
camera.zoom = 1.0

# Game world variables
world_width = 2000
world_height = 2000
player_position = Vector2(0, 0)  # Player's position in the world
camera_speed = 2

while not window_should_close():
    # Update
    if is_key_down(KEY_W):
        player_position.y -= camera_speed
    if is_key_down(KEY_S):
        player_position.y += camera_speed
    if is_key_down(KEY_A):
        player_position.x -= camera_speed
    if is_key_down(KEY_D):
        player_position.x += camera_speed

    # Update camera to follow the player
    camera.target = player_position
    camera.offset = Vector2(get_screen_width() / 2, get_screen_height() / 2)

    # Get mouse position
    mouse_x = get_mouse_x()
    mouse_y = get_mouse_y()

    # Calculate mouse position relative to camera
    mouse_world_x = mouse_x + camera.target.x - camera.offset.x
    mouse_world_y = mouse_y + camera.target.y - camera.offset.y

    # Draw
    begin_drawing()
    clear_background(SKYBLUE)

    # Begin the camera mode
    begin_mode_2d(camera)

    # Draw the player
    draw_circle_v(player_position, 20, RED)

    # Draw a rectangle at the mouse world position
    draw_rectangle(int(mouse_world_x) - 10, int(mouse_world_y) - 10, 20, 20, GREEN)

    # End the camera mode
    end_mode_2d()

    # Draw some text to display the mouse world position
    draw_text(f"Mouse World Position: ({mouse_world_x:.2f}, {mouse_world_y:.2f})", 10, 10, 20, BLACK)

    end_drawing()

close_window()


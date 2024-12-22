from pynput import *

mouse = Controller()

print('The current pointer position is {0}'.format(
    mouse.position))

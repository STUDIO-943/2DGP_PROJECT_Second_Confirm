import game_framework
from pico2d import *
import title_state


running = True
image = None
logo_time = 0.0
def enter():
    global image
    image = load_image('1.png')
    pass

def exit():
    global image
    del image
    pass


def update():
    global logo_time
    # global running
    if logo_time > 1.0:
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    clear_canvas()
    image.draw(800, 600)
    update_canvas()


def handle_events():
    events = get_events()






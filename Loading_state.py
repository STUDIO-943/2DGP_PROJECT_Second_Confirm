import game_framework
from pico2d import *
import title_state
import logo_state
import Select_state



running = True
image = None
logo_time = 0.0
def enter():
    global image
    image = load_image('L.png')
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
        game_framework.change_state(Select_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    clear_canvas()
    image.draw(800, 600)
    update_canvas()


def handle_events():
    events = get_events()






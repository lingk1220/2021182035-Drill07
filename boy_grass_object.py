from random import randint

from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = randint(50, 700), 90
        self.frame = randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = randint(50, 750), 599
        self.ballsize = randint(0, 1)
        self.speed = randint(20, 100) / 10
        if self.ballsize == 0:
            self.ballsize = 21
            self.image = load_image('ball21x21.png')
        else:
            self.ballsize =41
            self.image = load_image('ball41x41.png')
    def update(self):
        self.y -= self.speed
        if self.y - (self.ballsize / 2) > 30 + 20:
            pass
        else:
            self.y = 30 + 20 + (self.ballsize / 2)
    def draw(self):
        self.image.clip_draw(0, 0, self.ballsize, self.ballsize, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    balls = [Ball() for i in range(20)]
    world += balls

def update_world():
    grass.update() #객체 상태 시뮬레이션
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()

    update_canvas()
    pass
running = True

open_canvas()

# initialization code
reset_world()


# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code


close_canvas()

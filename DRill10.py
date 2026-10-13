from pico2d import *
import random
import os
# Game object class here


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        if self.x > 800:
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball21:
    def __init__(self):
        self.x = random.randint(0,700)
        self.y = 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.y -= 5
        if self.y < 60:
            self.y = 60
    def draw(self):
            self.image.clip_draw(self.frame * 100, 0, 21, 21, self.x, self.y)



def reset_world():
    global running
    running = True
    
    global grass
    global team
    global world
    global ball

    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for _ in range(11)]
    # world.extend(team)
    # ball21 = [Ball21() for _ in range(10)]
    world.append(ball21)
    # ball41 = [Ball41() for _ in range(10)]
    # world.append(ball41)
    


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
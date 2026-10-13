from pico2d import *
import random
import os
# Game object class here

ASSET_DIR = os.path.dirname(os.path.abspath(__file__))

class Grass:
    def __init__(self):
        self.image = load_image(os.path.join(ASSET_DIR, 'grass.png'))

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = 0
        self.image = load_image(os.path.join(ASSET_DIR, 'run_animation.png'))

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        if self.x > 800:
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image(os.path.join(ASSET_DIR, 'zombie_run_animation.png'))

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                            self.x, self.y, frame_width // 2, frame_height // 2)



def reset_world():
    global running
    running = True
    
    global grass
    global team
    global world

    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for _ in range(11)]
    world.extend(team)
    zombie = Zombie()
    world.append(zombie)


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
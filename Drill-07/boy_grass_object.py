from pico2d import *
from random import *

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.frame = randint(0, 7)
        self.x, self.y = randint(100, 700), 90
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Big_ball:
    def __init__(self):
        self.frame = randint(0, 7)
        self.x, self.y = randint(1, 799), 599
        self.falling_rate = randint(1, 20)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 50:
            self.y -= self.falling_rate
        else:
            self.y = self.y

    def draw(self):
        self.image.draw(self.x, self.y)


class Small_ball:
    def __init__(self):
        self.frame = randint(0, 7)
        self.x, self.y = randint(1, 799), 599
        self.falling_rate = randint(10, 20)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 50:
            self.y -= self.falling_rate
        else:
            self.y = self.y

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
small_ball_count = randint(1, 20)
big_ball_count = 20 - small_ball_count
boy = Boy()
grass = Grass()
running = True
team = [Boy() for i in range(11)]
big_ball = [Big_ball() for i in range(big_ball_count)]
small_ball = [Small_ball() for i in range(small_ball_count)]

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in big_ball:
        ball.update()
    for ball in small_ball:
        ball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in big_ball:
        ball.draw()
    for ball in small_ball:
        ball.draw()
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()
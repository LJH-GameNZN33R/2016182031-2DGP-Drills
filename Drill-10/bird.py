import game_framework
from pico2d import *
import game_world

# 10 pixel = 25 cm
# bird size : 2.0m -> 80 pixel
# bird velocity : 30km/h

PIXEL_PER_METER = (10.0 / 0.25)
FLY_SPEED_KMPH = 20.0  # km/h
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

BIRD_SIZE_M = 2
BIRD_SIZE_PIXEL = BIRD_SIZE_M * PIXEL_PER_METER

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    def __init__(self):
        self.x, self.y = 15, 400
        self.image = load_image('bird_animation.png')
        self.velocity = FLY_SPEED_PPS
        self.frame = 0

    def update(self):
        self.frame = (self. frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(100, self.x, 1600 - 100)
        if self.x == 1600 - 100:
            self.velocity = -FLY_SPEED_PPS
        if self.x == 100:
            self.velocity = FLY_SPEED_PPS


    def draw(self):
        if self.velocity > 0:
            self.image.clip_draw((int(self.frame) % 5) * 183, (2 - (int(self.frame) // 5)) * 167, 183, 167,
                                 self.x, self.y, BIRD_SIZE_PIXEL, BIRD_SIZE_PIXEL)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 183, (2 - (int(self.frame) // 5)) * 167, 183, 167,
                                           0, 'h', self.x, self.y, BIRD_SIZE_PIXEL, BIRD_SIZE_PIXEL)
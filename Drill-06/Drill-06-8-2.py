from pico2d import *
from random import *
ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

x = [random.randint(0, 1280) for n in range(10)]
y = [random.randint(0, 1024) for n in range(10)]
open_canvas(KPU_WIDTH, KPU_HEIGHT)
frame = 0
running = True
character_direction = 1
sheet_cut = 1
character_x, character_y = 0, 0

while running:
    for i in range(0, 50):
        while count < 10:
            t = i / 100
            character_x = (2 * t ** 2 - 3 * t + 1) * x[count] + (-4 * t ** 2 + 4 * t) * x[count+1] + (2 * t ** 2 - t) * x[count+2]
            character_y = (2 * t ** 2 - 3 * t + 1) * y[count] + (-4 * t ** 2 + 4 * t) * y[count+1] + (2 * t ** 2 - t) * y[xount+2]
        ground.draw(640, 512)
    x, y = ((randint(1280, 1024)), (randint(1280, 1024)))

    while True:
        move_round_curve(p1, p2, p3, p4)
        character.clip_draw(frame*100, 100*sheet_cut, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.04)
    get_events()

close_canvas()


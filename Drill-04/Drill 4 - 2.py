from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dir_lr
    global dir_ud
    global character_direction

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                character_direction = 1
                dir_lr += 1
            elif event.key == SDLK_LEFT:
                character_direction = 0
                dir_lr -= 1
            elif event.key == SDLK_UP:
                dir_ud += 1
            elif event.key == SDLK_DOWN:
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
               running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_lr -= 1
            elif event.key == SDLK_LEFT:
                dir_lr += 1
            elif event.key == SDLK_UP:
                dir_ud -= 1
            elif event.key == SDLK_DOWN:
                dir_ud += 1


x = 400
y = 90
frame = 0
running = True
dir_lr = 0
dir_ud = 0
character_direction = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100, character_direction*100, 100, 100, x, y)
    update_canvas()
    handle_events()
    x += dir_lr*5
    y += dir_ud*5
    frame = (frame + 1) % 8
    if x >= 800:
        x = 800
        character_direction = 0
    elif x <= 0:
        x = 0
        character_direction = 1
    if y >= 600:
        y = 600
    elif y <= 90:
        y = 90
    delay(0.01)
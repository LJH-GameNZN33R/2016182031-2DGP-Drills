from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dir
    global character_direction

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                character_direction = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                character_direction = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
               running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


x = 400
frame = 0
running = True
dir = 0
character_direction = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100, character_direction*100, 100, 100, x, 90)
    update_canvas()
    handle_events()
    x += dir*4
    frame = (frame + 1) % 8
    if x >= 800:
        x = 800
        character_direction = 0
    elif x <= 0:
        x = 0
        character_direction = 1
    delay(0.01)



from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global character_x
    global character_y
    global character_direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            clear_canvas()
            curser.draw(x, y)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if not running:
                running = True
            x, y = event.x, KPU_HEIGHT - 1 - event.y

            x, y = event.x - 20, KPU_HEIGHT - 1 - event.y + 20
            if x < character_x:
                character_direction = 0
            elif x > character_x:
                character_direction = 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
curser = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
x, y = 0, 0
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_direction = 1
frame = 0
show_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    curser.clip_draw(0, 0, 50, 52, x+20, y-20)
    if x:
        if x == character_x and y == character_y:
            x = 0
            y = 0
        elif character_x <= x:
            character_direction = 1
        elif character_x >= x:
            character_direction = 0
        character_x += (x - character_x) / 100
        character_y += (y - character_y) / 100

    character.clip_draw(frame * 100, character_direction * 100, 100, 100, character_x, character_y)

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()

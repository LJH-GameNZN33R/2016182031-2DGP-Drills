from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 400
frame = 0
running = True
character_direction = 1
sheet_cut = 1

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100, 100*sheet_cut, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += character_direction*5
    if x >= 800:
        character_direction = -1
        sheet_cut = 0
    elif x <= 0:
        character_direction = 1
        sheet_cut = 1
    delay(0.03)
    get_events()

close_canvas()


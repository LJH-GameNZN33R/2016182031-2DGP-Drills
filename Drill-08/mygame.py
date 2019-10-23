import game_framework
import pico2d

import start_state
import title_state
import main_state

pico2d.open_canvas()
game_framework.run(start_state)
game_framework.run(title_state)
# game_framework.run(main_state)
pico2d.close_canvas()

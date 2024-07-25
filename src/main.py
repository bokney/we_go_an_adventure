from game_state import GameState, GameStateDirector
from game_states.sand_pit import init_sand_pit, loop_sand_pit, exit_sand_pit

sand_pit = GameState(init_sand_pit, loop_sand_pit, exit_sand_pit)
director = GameStateDirector(sand_pit)

while True:
    director.run()
    
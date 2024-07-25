from src.game_state import GameState, GameStateDirector
import pytest

ts_01_counter = 0
def ts_01_init():
    global ts_01_counter
    ts_01_counter = 999
def ts_01_loop():
    global ts_01_counter
    ts_01_counter += 1
    if ts_01_counter > 1000:
        return 1
    return 0
def ts_01_exit():
    return ts_02
ts_01 = GameState(ts_01_init, ts_01_loop, ts_01_exit)

ts_02_counter = 0
def ts_02_init():
    global ts_02_counter
    ts_02_counter = 999
def ts_02_loop():
    global ts_02_counter
    ts_02_counter += 1
    if ts_02_counter > 1000:
        return 1
    return 0
def ts_02_exit():
    pass
ts_02 = GameState(ts_02_init, ts_02_loop, ts_02_exit)

def test_director_cycles_correctly():
    director = GameStateDirector(ts_01)
    assert director.current_state is ts_01
    assert director.state_counter == 0
    assert director.state_step == 0
    director.run()
    assert director.current_state is ts_01
    assert director.state_counter == 1
    assert director.state_step == 1
    director.run()
    assert director.current_state is ts_02
    assert director.state_counter == 0
    assert director.state_step == 0
    director.run()
    assert director.current_state is ts_02
    assert director.state_counter == 1
    assert director.state_step == 1
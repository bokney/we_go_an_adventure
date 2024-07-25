"""
¿¿ Iterating Context Manager State Machine ??

2 classes
GameState
GameStateDirector

  -  One instance of GameStateDirector manages the sequential running 
of any number of instances of GameState
  -  Each instance of GameState determines which state the GameStateDirector
will run next

# # # # # # # #
# GameState   #
# # # # # # # #
# - init_func #
# - loop_func #
# - exit_func #
# # # # # # # # 

  -  init_func is only ever run once per GameState
  -  init_func is only ever run before loop_func
  -  loop_func is ran repeatedly until it returns something other than None
  -  exit_func is only run after init_func and loop_func
  -  exit_func is only ever run once per GameState
  -  exit_func returns a reference to the next GameState to be run
  -  if exit_func returns None the program will terminate

# # # # # # #       # # # # # # #       # # # # # # #       # # # # # # #
# GameState #   |--># GameState #   |--># GameState #   |--># GameState #
# # # # # # #   |   # # # # # # #   |   # # # # # # #   |   # # # # # # #
# init_func #   |   # init_func #   |   # init_func #   |   # init_func # 
# loop_func #   |   # loop_func #   |   # loop_func #   |   # loop_func # 
# exit_func #---|   # exit_func #---|   # exit_func #---|   # exit_func #
# # # # # # #       # # # # # # #       # # # # # # #       # # # # # # #

  -  state_counter is incremented after each invocation of loop_func
  -  state_counter is not incremented on invocation of init_func or exit_func
  -  state_step determines which func to incovate
         0: init_func
         1: loop_func
         2: exit_func
  -  current_state holds reference to state currently being handled
  -  initial current_state is passed as sole argument upon instance definition

# # # # # # # # # # #
# GameStateDirector #
# # # # # # # # # # #
# - state_counter   #  -  increments after each invocation of loop_func
# - state_step      #  -  determines init, loop or exit
# - current_state   #  -  reference to state currently being run
# # # # # # # # # # #
# + run()           #  -  each invocation advances state_counter by 1
# # # # # # # # # # #

  -  each of the three properties are non-public and have a getter
  -  on first run(), init_func is called as is loop_func
  -  exit_func is called during the same run invocation as the last loop_func

"""

from types import FunctionType

class GameState:

    def __init__(self,
                 init_func: FunctionType | None = None,
                 loop_func: FunctionType | None = None,
                 exit_func: FunctionType | None = None
                 ) -> None:
        self._init_func = init_func
        self._loop_func = loop_func
        self._exit_func = exit_func
    

class GameStateDirector:

    def __init__(self, initial_state: GameState) -> None:  
        self._state_step = 0
        self._state_counter = 0
        self._current_state = initial_state

    @property
    def current_state(self) -> GameState:
        return self._current_state

    @property
    def state_step(self) -> int:
        return self._state_step
    
    @property
    def state_counter(self) -> int:
        return self._state_counter

    def run(self) -> None:
        if self._state_step == 0:
            if self._current_state._init_func != None:
                    self._current_state._init_func()
                    self._state_step += 1
        if self._current_state._loop_func != None:
                    move_ahead = self._current_state._loop_func()
                    if (move_ahead != 0):
                        self._state_step += 1
        if self._state_step == 2:
             if self._current_state._exit_func != None:
                    next_state = self._current_state._exit_func()
                    if (next_state == None):
                        quit()
                    self._current_state = next_state
                    self._state_step = 0
                    self._state_counter = 0
        else:
             self._state_counter += 1


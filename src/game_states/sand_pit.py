from sprint import sprint, wait, clear


class Actor:

    def __init__(self,
                 name: str,
                 char: str = 'ö',
                 x: int = 0,
                 y: int = 0
                 ) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.char = char
        self._visible = True
        # self._
        
    def place(self, x: int, y: int):
        self.x = x
        self.y = y


class Canvas:

    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._store = []
        self._actors = []
        self._populate()

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def _populate(self):
        self._store.clear()
        for y in range(self._height):
            self._store.append([])
            for x in range(self._width):
                # self._store[y].append("-")
                if y == 0 or y == self._height - 1 or x == 0 or x == self._width - 1:
                    self._store[y].append('#')
                else:
                    self._store[y].append(' ')
        for a in self._actors:
            self._store[a.y][a.x] = a.char

    def draw(self):
        self._populate()
        for y in range(self._height):
            print("".join(self._store[y]))


# # # # # # # # # # # # # # # # # # # # # # # # 

def obj_place():
    # for y in range(obj_y, obj_y + obj_height):
    #     for x in range(obj_x, obj_x + obj_width):
    #         sand_pit[y % sand_pit_width][x % sand_pit_height] = 'O'
    pass

# # # # # # # # # # # # # # # # # # # # # # # # 

canvas = Canvas(32, 24)

def init_sand_pit():
    canvas.add_actor(Actor("actor_01", "P", 4, 4))
    clear()
    canvas.draw()


def loop_sand_pit():
    result = input(">")
    canvas.add_actor(Actor("000", result, 8, 8))
    clear()
    canvas.draw()
    return 0

def exit_sand_pit():
    print('Goodbye')
    pass

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

class Fruit(Item):
    def __init__(self, name, value=20, symbol="?"):
        super().__init__(name, value, symbol)

class Trap(Item):
    def __init__(self, name, value=-10, symbol="*"):
        super().__init__(name, value, symbol)

class Shovel(Item):
    def __init__(self, name, value=0, symbol="#"):
        super().__init__(name, value, symbol)

class Key(Item):
    def __init__(self, name, value=0, symbol="p"):
        super().__init__(name, value, symbol)

class Chest(Item):
    def __init__(self, name, value=100, symbol="O"):
        super().__init__(name, value, symbol)

class Exit(Item):
    def __init__(self, name, value=0, symbol="E"):
        super().__init__(name, value, symbol)

pickups = [Fruit("carrot"), Fruit("apple"), Fruit("strawberry"), Fruit("cherry"), Fruit("watermelon"), Item("radish"), Fruit("cucumber"), Item("meatball")]


def randomize(grid, scale, item=None):
    for i in scale:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item if item else i)
                break

def randomize_one_item(grid):
    for item in pickups:
        # slumpa en position tills vi hittar en som är ledig
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, item)
            break



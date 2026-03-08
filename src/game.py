from copy import deepcopy

from . import pickups
from .grid import Grid
from .pickups import Chest
from .player import Player
from .helper import print_status

player = Player(3, 1)
score = 0
shovel = 0
inventory = []
move_count= 0
original_items = deepcopy(pickups.pickups)

grid = Grid()
grid.set_player(player)
grid.make_walls()
pickups.randomize(grid)
pickups.randomize_traps(grid)
pickups.randomize_shovels(grid)
pickups.randomize_keys(grid)
pickups.randomize_chest(grid)
grid.add_interior_walls()



def is_original_item(maybe_item):
    return maybe_item in original_items


def handle_move(command, player, grid, inventory):
    """Hanterar spelarens kommandot och plockning av varor."""
    global original_items

    directions = {
        "d": (1, 0),
        "a": (-1, 0),
        "w": (0, -1),
        "s": (0, 1)
    }

    if command == "i":
        print("Inventory:")
        for item in inventory:
            print(f"- {item.name} ({item.value} points)")
        return 0, False

    if command not in directions:
        print("Invalid move/command, try again.")
        return 0, False

    dx, dy = directions[command]

    if not player.can_move(dx, dy, grid, inventory):
        print("It is a wall, change direction.")
        return 0, False

    maybe_item = grid.get(player.pos_x + dx, player.pos_y + dy)
    player.move(dx, dy)

    if isinstance(maybe_item, pickups.Trap):
        print(f"You stepped on a {maybe_item.name}! -10 points.")
        return -10, True

    if isinstance(maybe_item, pickups.Item):
        # we found something
        if isinstance(maybe_item, Chest):
            print("You opened a chest!")
        else:
            if is_original_item(maybe_item):
                original_items.remove(maybe_item)
                print(f"{len(original_items)} of original item(s) left to exit the game.")
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        grid.clear(player.pos_x, player.pos_y)
        inventory.append(maybe_item)
        return maybe_item.value, True

    print("You lost one point for at step on floor.")
    return -1, True

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(grid, score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    score_change, move_made = handle_move(command, player, grid, inventory)
    score += score_change

    if move_made:
        move_count += 1
        print("Move count:", move_count)
        if move_count % 25 == 0:
            pickups.randomize_one_item(grid)
            print("A new fruit/vegetable added on the map!")
        if len(original_items) ==  0:
            print("You have collected all original items and you can reach to E on the map to exit the game!")
            pickups.randomize_exit(grid)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

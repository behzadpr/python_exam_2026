from .grid import Grid
from .player import Player
from . import pickups



player = Player(3, 1)
score = 0
inventory = []

grid = Grid()
grid.set_player(player)
grid.make_walls()
pickups.randomize(grid)
grid.add_interior_walls()


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

def handle_move(command, player, grid, inventory):
    """Hanterar spelarens kommandot och plockning av varor."""

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
        return 0

    if command not in directions:
        print("Invalid move/command, try again.")
        return 0

    dx, dy = directions[command]

    if not player.can_move(dx, dy, grid):
        print("It is a wall, change direction.")
        return 0

    maybe_item = grid.get(player.pos_x + dx, player.pos_y + dy)
    player.move(dx, dy)

    if isinstance(maybe_item, pickups.Item):
        # we found something
        print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        grid.clear(player.pos_x, player.pos_y)
        inventory.append(maybe_item)
        return maybe_item.value

    print("You lost one point for at  step on floor.")
    return -1

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(grid)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    score += handle_move(command, player, grid, inventory)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

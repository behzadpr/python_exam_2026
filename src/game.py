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


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(grid)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d" and player.can_move(1, 0, grid):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        maybe_item = grid.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            grid.clear(player.pos_x, player.pos_y)

        elif maybe_item == grid.wall:
            print("You hit a wall, Ouch!")
            player.move(-1, 0)

    elif command == "a" and player.can_move(-1, 0, grid):  # move left
        maybe_item = grid.get(player.pos_x - 1, player.pos_y)
        player.move(-1, 0)

        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            grid.clear(player.pos_x, player.pos_y)

    elif command == "w" and player.can_move(0, -1, grid):  # move up
        maybe_item = grid.get(player.pos_x, player.pos_y - 1)
        player.move(0, -1)

        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            grid.clear(player.pos_x, player.pos_y)

    elif command == "s" and player.can_move(0, 1, grid):  # move down
        maybe_item = grid.get(player.pos_x, player.pos_y + 1)
        player.move(0, 1)

        if isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            grid.clear(player.pos_x, player.pos_y)

    else:
        print("Invalid command, try again.")
        print_status(grid)



# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

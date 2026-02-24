from src.pickups import pickups, Shovel


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid, inventory):
        if not grid.is_surrounding_wall(self.pos_x + x, self.pos_y + y):
            if grid.is_wall(self.pos_x + x, self.pos_y + y):
                if Shovel in [type(item) for item in inventory]:
                    # Remove the first Shovel found
                    for item in inventory:
                        if isinstance(item, Shovel):
                            inventory.remove(item)
                            print("One shovel used to clear the wall.")
                            return True
                else:
                    print("Cannot move through the wall. You need a shovel to clear it.")
                return False
            else:
                return True
        else:
            return False





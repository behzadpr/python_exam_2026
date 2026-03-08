import unittest
from src.grid import Grid
from src.player import Player
from src.pickups import Shovel


class TestShovel(unittest.TestCase):

    def setUp(self):
        """Creates a game grid with a player."""
        self.grid = Grid()
        self.player = Player(5, 5)
        self.grid.set_player(self.player)
        self.inventory = []

    def test_player_blocked_by_wall_without_shovel(self):
        self.grid.set(6, 5, Grid.wall)

        can_move = self.player.can_move(1, 0, self.grid, self.inventory)

        self.assertFalse(can_move)

    def test_player_can_move_through_wall_with_shovel(self):
        self.grid.set(6, 5, Grid.wall)
        self.inventory.append(Shovel("shovel"))

        can_move = self.player.can_move(1, 0, self.grid, self.inventory)

        self.assertTrue(can_move)
        # shovel should be consumed and inventory should be empty after use
        self.assertTrue(len(self.inventory) == 0)


if __name__ == "__main__":
    unittest.main()


import unittest
from src.grid import Grid
from src.player import Player
from src.pickups import Trap


class TestTraps(unittest.TestCase):

    def setUp(self):
        """Creates a game grid with a player and a trap next to the player."""
        self.grid = Grid()
        self.player = Player(3, 1)
        self.grid.set_player(self.player)
        self.trap = Trap("trap")
        self.grid.set(4, 1, self.trap)

    def assert_trap_on_grid(self):
        item_on_grid = self.grid.get(4, 1)
        self.assertTrue(isinstance(item_on_grid, Trap))


    def test_trap_can_hit_multiple_times(self):
        score = 0
        # player moves to trap
        self.player.move(1, 0)
        score -= 10

        # asserts that the player has lost 10 points
        self.assertEqual(score, -10)

        # moves away from the trap
        self.player.move(-1, 0)

        # check if trap stayed at its original position
        self.assert_trap_on_grid()

        # moves onto the trap again
        self.player.move(1, 0)
        score -= 10

        # asserts that the player has lost 20 points
        self.assertEqual(score, -20)

        # check if trap stayed at its original position
        self.assert_trap_on_grid()


if __name__ == "__main__":
    unittest.main()


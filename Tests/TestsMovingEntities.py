import unittest
import curses

from PythonProject.Module_PacDuel.MovingEntities import Pacman, Ghost
from PythonProject.Module_PacDuel.MappingGen import Map
from PythonProject.Module_PacDuel.ScoreCount import ScoreCount


class TestsMovingEntities(unittest.TestCase):
    """
    author: Andreas Bombaert
    description: classe de tests pour MovingEntities
    """
    def tests_pacman_init(self):
        pacman = Pacman(3)
        self.assertEqual(pacman.lives, 3)
        self.assertEqual(pacman.pos, [0, 0])

    def test_pacman_setpos(self):
        pacman = Pacman(3)
        pacman.setpos(4, 9)
        self.assertEqual(pacman.pos, [4, 9])

    def test_pacman_death(self):
        pacman = Pacman(3)
        pacman.death()
        self.assertEqual(pacman.lives, 2)
        pacman.death()
        self.assertEqual(pacman.lives, 1)

    def test_pacman_on_ghost(self):
        pacman = Pacman(3)
        pacman.setpos(4, 9)

        """
        The ghost being a child of the MovingEntities class, a second pacman called 'ghost'
        is more convenient for the tests and work the same way    
        """
        ghost = Pacman(3)
        ghost.setpos(4, 9)
        ghost2 = Pacman(3)
        ghost2.setpos(3, 2)
        ghosts = [ghost]
        ghosts2 = [ghost2]
        self.assertTrue(pacman.on_ghost(ghosts))
        self.assertFalse(pacman.on_ghost(ghosts2))

    def test_pacman_moves(self):
        pacman = Pacman(3)
        pacman.setpos(4, 9)
        game_map = Map("../data/map.txt", pacman.pos[0], pacman.pos[1])
        game_map.gen_map()
        map_ar = game_map.map_ar
        score = ScoreCount()

        pacman.moves(ord('z'), map_ar, score, game_map.collectibles)
        self.assertEqual(pacman.pos, [3, 9])
        pacman.moves(ord('s'), map_ar, score, game_map.collectibles)
        self.assertEqual(pacman.pos, [4, 9])
        pacman.moves(ord('q'), map_ar, score, game_map.collectibles)
        self.assertEqual(pacman.pos, [4, 8])
        pacman.moves(ord('d'), map_ar, score, game_map.collectibles)
        self.assertEqual(pacman.pos, [4, 9])

    def test_ghost_init(self):
        ghost = Ghost("yellow")
        self.assertEqual(ghost.color, "yellow")

    def test_ghost_set_init_pos(self):
        pacman = Pacman(3)
        pacman.setpos(4, 9)

        ghost = Ghost("yellow")
        self.assertEqual(ghost.color, "yellow")

        game_map = Map("../data/map.txt", pacman.pos[0], pacman.pos[1])
        game_map.gen_map()
        map_ar = game_map.map_ar
        pacman.set_eaten(map_ar)

        ghost.set_init_pos(map_ar, pacman)
        self.assertNotEqual(ghost.pos, pacman.pos)
        ghost.set_init_pos(map_ar, pacman)
        self.assertNotEqual(ghost.pos, pacman.pos)
        ghost.set_init_pos(map_ar, pacman)
        self.assertNotEqual(ghost.pos, pacman.pos)
        ghost.set_init_pos(map_ar, pacman)

    def test_ghost_moves(self):
        pacman = Pacman(3)
        pacman.setpos(4, 9)
        game_map = Map("../data/map.txt", pacman.pos[0], pacman.pos[1])
        game_map.gen_map()
        map_ar = game_map.map_ar
        pacman.set_eaten(map_ar)
        ghost = Ghost("yellow")
        ghost.setpos(4, 9)

        ghost.moves(map_ar, 1, 1, pacman)
        self.assertEqual(ghost.pos, [3, 9])
        ghost.moves(map_ar, 3, 1, pacman)
        self.assertEqual(ghost.pos, [4, 9])
        ghost.moves(map_ar, 2, 1, pacman)
        self.assertEqual(ghost.pos, [4, 8])
        ghost.moves(map_ar, 4, 1, pacman)
        self.assertEqual(ghost.pos, [4, 9])


if __name__ == "__main__":
    unittest.main()

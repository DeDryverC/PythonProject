import unittest

from Projet.PythonProject.Module_PacDuel.MovingEntities import Pacman, Ghost
from Projet.PythonProject.Module_PacDuel.MappingGen import Map


class TestsMovingEntities(unittest.TestCase):
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
        self.assertTrue(pacman.on_ghost(ghost))
        self.assertFalse(pacman.on_ghost(ghost2))

    # todo tests pacman moves

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

        ghost.set_init_pos(map_ar)
        self.assertNotEqual(ghost.pos, pacman.pos)
        ghost.set_init_pos(map_ar)
        self.assertNotEqual(ghost.pos, pacman.pos)
        ghost.set_init_pos(map_ar)
        self.assertNotEqual(ghost.pos, pacman.pos)
        ghost.set_init_pos(map_ar)

    # todo tests ghost moves


if __name__ == "__main__":
    unittest.main()

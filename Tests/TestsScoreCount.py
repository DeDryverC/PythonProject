²²²import unittest

from PythonProject.Module_PacDuel.ScoreCount import ScoreCount


class TestsScoreCount(unittest.TestCase):
    """
    author: Cedric de Dryver
    description: classe de tests pour ScoreCount
    """
    def tests_get_score(self):
        score = ScoreCount(1)
        score1 = ScoreCount(0)
        score2 = ScoreCount(-1)
        self.assertEqual(score.get_score, 1)
        self.assertEqual(score1.get_score, 0)
        self.assertEqual(score2.get_score, -1)

    def add_score(self):
        score = ScoreCount()
        score1 = ScoreCount()
        score2 = ScoreCount()
        score.add_score(1)
        score1.add_score(0)
        score2.add_score(-1)
        self.assertEqual(score.get_score, 1)
        self.assertEqual(score1.get_score, 0)
        self.assertEqual(score2.get_score, -1)


if __name__ == "__main__":
    unittest.main()

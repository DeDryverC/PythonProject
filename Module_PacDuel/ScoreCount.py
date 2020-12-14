''' Class representing a score counter.

Auth: Cédric De Dryver
Last date:

Score counter for a game of Pac Man.
'''


class ScoreCount:
    """Initialization of the Class
    Variables: (Int) score => actual score of the running game.
    """

    def __init__(self, score=0):
        self.__score = score

    '''GETTER
    POST: (Int)  => Return the actual score (int)
    '''

    @property
    def get_score(self):
        return self.__score

    '''ADDITION SCORE
    PRE :  (Int) ajout => points to addition to the score

    POST : (None)  => add points to the private variable score.
    '''

    def add_score(self, ajout):
        self.__score = self.__score + ajout

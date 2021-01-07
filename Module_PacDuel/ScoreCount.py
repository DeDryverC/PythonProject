


class ScoreCount:
    '''
    Class representing a score counter.

    Auth: Cédric De Dryver
    Last date:

    Score counter for a game of Pac Man.
    '''

    def __init__(self, score=0):
        """
            Initialization of the Class
            Variables: (Int) score => actual score of the running game.
        """
        self.__score = score



    @property
    def get_score(self):
        '''
            GETTER
            POST: (Int)  => Return the actual score (int)
        '''
        return self.__score



    def add_score(self, ajout):
        '''
            ADDITION SCORE
            PRE :  (Int) ajout => points to addition to the score

            POST : (None)  => add points to the private variable score.
        '''
        self.__score = self.__score + ajout

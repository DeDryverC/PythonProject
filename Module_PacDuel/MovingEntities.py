import time
import random


class MovingEntities:
    """
    Author: Andreas Bombaert
    Date: 6/12/2020
    Mother class of Pacman and Ghost classes, this class represents any moving entity on the map
    """

    def __init__(self, map_ar):
        self.__pos = [0, 0]
        self.state = 1  # 0: dead, 1: alive
        self.map = map_ar


class Pacman(MovingEntities):
    """
    Author: Andreas Bombaert
    Date: 6/12/2020
    Pacman class, this class contains all the necessary methods for the game to make pacman move through the map
    """

    def __init__(self, lives):
        super().__init__([])
        self.__lives = lives

    @property
    def pos(self):
        return self.__pos

    @property
    def lives(self):
        return self.__lives

    """
    PRE : none
    POST : Pacman.pos now equals pos_x, pos_y
    RAISES : ValueError if pos_x or pos_y is under 0
    """

    def setpos(self, pos_x, pos_y):
        if pos_x < 0 or pos_y < 0:
            raise ValueError("position can't be under 0")
        self.__pos = [pos_x, pos_y]

    """
    PRE : none
    POST : Pacman.lives decrease from 1 life
    RAISES : none
    """

    def death(self):
        self.__lives -= 1

    """
    PRE : There can be multiple args but they must be ghosts
    POST : return a boolean that contains if the pacman is on the same position than a ghost or not
    RAISES : 
    """

    def on_ghost(self, *args):
        for x in args:
            if self.pos == x.pos:
                return True
        return False

    """
    PRE : game_map must not be empty
    POST : returns the updated args
    RAISES : ValueError if map is empty
    """

    def moves(self, key, game_map, score, count_coll):
        if not game_map:
            raise ValueError("game map mustn't be empty")
        if key == ord('z'):
            if game_map[self.__pos[0] - 1][self.__pos[1]] == "#":
                pass
            else:
                if game_map[self.__pos[0] - 1][self.__pos[1]] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0] - 1][self.__pos[1]] == ".":
                    score.add_score(100)
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "x":
                    score.add_score(200)
                if game_map[self.__pos[0] - 1][self.__pos[1]] == "^":
                    score.add_score(500)
                game_map[self.__pos[0] - 1][self.__pos[1]] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[0] -= 1
        if key == ord('q'):
            if game_map[self.__pos[0]][self.__pos[1] - 1] == "#":
                pass
            else:
                if game_map[self.__pos[0]][self.__pos[1] - 1] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0]][self.__pos[1] - 1] == ".":
                    score.add_score(100)
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "x":
                    score.add_score(200)
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "^":
                    score.add_score(500)
                game_map[self.__pos[0]][self.__pos[1] - 1] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[1] -= 1

        if key == ord('s'):
            if game_map[self.__pos[0] + 1][self.__pos[1]] == "#":
                pass
            else:
                if game_map[self.__pos[0] + 1][self.__pos[1]] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0] + 1][self.__pos[1]] == ".":
                    score.add_score(100)
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "x":
                    score.add_score(200)
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "^":
                    score.add_score(500)
                game_map[self.__pos[0] + 1][self.__pos[1]] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[0] += 1

        if key == ord('d'):
            if game_map[self.__pos[0]][self.__pos[1] + 1] == "#":
                pass
            else:
                if game_map[self.__pos[0]][self.__pos[1] + 1] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0]][self.__pos[1] + 1] == ".":
                    score.add_score(100)
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "x":
                    score.add_score(200)
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "^":
                    score.add_score(500)
                game_map[self.__pos[0]][self.__pos[1] + 1] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[1] += 1

        return key, game_map, score, count_coll


"""
    Author: Andreas Bombaert
    Date: 6/12/2020
    Ghosts class, this class contains all the necessary methods for the game to make the ghost move +- randomly through the map
    """


class Ghost(MovingEntities):
    def __init__(self, color):
        super().__init__([])
        self.__color = color
        self.__prev = []

    @property
    def pos(self):
        return self.__pos

    @property
    def prev(self):
        return self.__prev

    @property
    def color(self):
        return self.__color

    """
        PRE : none
        POST : Ghost pos is a random position, except the pacman position and a wall position
        RAISES : none
        """

    def set_init_pos(self, game_map):
        self.__pos = [random.randint(1, 8), random.randint(1, 18)]
        while game_map[self.__pos[0]][self.__pos[1]] == "#" or game_map[self.__pos[0]][self.__pos[1]] == "o":
            self.__pos = [random.randint(1, 8), random.randint(1, 18)]
        self.__prev = game_map[self.__pos[0]][self.__pos[1]]
        game_map[self.__pos[0]][self.__pos[1]] = self
        return game_map

    """
        PRE : game map mustn't be empty
        POST : returns the updated game map
        RAISES : TypeError if an argument is not a Ghost
        """

    # for direction 1: forward, 2: left, 3: backward, 4: right
    def moves(self, game_map, direction):
        if not game_map:
            raise ValueError("Game map mustn't be empty")

        if direction == 1:
            if game_map[self.__pos[0] - 1][self.__pos[1]] == "#":
                direction = random.randint(2, 4)
                self.moves(game_map, direction)
            else:
                if game_map[self.__pos[0]][self.__pos[1]] == "o":
                    pass
                else:
                    game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = game_map[self.__pos[0] - 1][self.__pos[1]]
                game_map[self.__pos[0] - 1][self.__pos[1]] = self

                self.__pos[0] -= 1

        if direction == 2:
            if game_map[self.__pos[0]][self.__pos[1] - 1] == "#":
                direction = random.randint(1, 4)
                while direction == 2:
                    direction = random.randint(1, 4)
                self.moves(game_map, direction)
            else:
                if game_map[self.__pos[0]][self.__pos[1]] == "o":
                    pass
                else:
                    game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = game_map[self.__pos[0]][self.__pos[1] - 1]
                game_map[self.__pos[0]][self.__pos[1] - 1] = self

                self.__pos[1] -= 1

        if direction == 3:
            if game_map[self.__pos[0] + 1][self.__pos[1]] == "#":
                direction = random.randint(1, 4)
                while direction == 3:
                    direction = random.randint(1, 4)
                self.moves(game_map, direction)
            else:
                if game_map[self.__pos[0]][self.__pos[1]] == "o":
                    pass
                else:
                    game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = game_map[self.__pos[0] + 1][self.__pos[1]]
                game_map[self.__pos[0] + 1][self.__pos[1]] = self

                self.__pos[0] += 1

        if direction == 4:
            if game_map[self.__pos[0]][self.__pos[1] + 1] == "#":
                direction = random.randint(1, 3)
                self.moves(game_map, direction)
            else:
                if game_map[self.__pos[0]][self.__pos[1]] == "o":
                    pass
                else:
                    game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = game_map[self.__pos[0]][self.__pos[1] + 1]
                game_map[self.__pos[0]][self.__pos[1] + 1] = self

                self.__pos[1] += 1

        return game_map

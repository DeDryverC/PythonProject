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
        self.__pos = [0, 0]
        self.__eaten = []

    @property
    def pos(self):
        return self.__pos

    @property
    def lives(self):
        return self.__lives

    @property
    def eaten(self):
        return self.__eaten

    """
    PRE : none
    POST : Pacman.pos now equals pos_x, pos_y
    RAISES : ValueError if pos_x or pos_y is under 0
    """
    def setpos(self, pos_x, pos_y):
        self.__pos = [pos_x, pos_y]

    def set_eaten(self, game_array):
        self.__eaten = game_array.copy()

    """
    PRE : none
    POST : Pacman.lives decrease from 1 life
    RAISES : none
    """
    def death(self):
        self.__lives -= 1

    """
    PRE : ghosts mustn't be empty
    POST : return a boolean that contains if the pacman is on the same position than a ghost or not
    RAISES : ValueError
    """
    def on_ghost(self, ghosts):
        if not ghosts:
            raise ValueError("ghosts cannot be empty")
        for x in ghosts:
            if self.pos == x.pos:
                return True
        return False

    """
    PRE: ghost must be a Ghost object
    POST: return the direction of the ghost
    RAISES : TypeError if ghosts is empty
    """
    def locate_ghost(self, ghost):
        if not isinstance(Ghost, ghost):
            raise TypeError("ghost must be a Ghost object")


    """
    PRE : game_map must not be empty
    POST : returns the updated args
    RAISES : ValueError if map is empty
    """
    def moves(self, key, game_map, score, count_coll):

        if key == ord('z'):
            if game_map[self.__pos[0] - 1][self.__pos[1]] == "#":
                pass
            else:
                if game_map[self.__pos[0] - 1][self.__pos[1]] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0] - 1][self.__pos[1]] == ".":
                    score.add_score(100)
                    self.__eaten[self.__pos[0] - 1][self.__pos[1]] = " "
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0] - 1][self.__pos[1]] = " "
                if game_map[self.__pos[0] - 1][self.__pos[1]] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0] - 1][self.__pos[1]] = " "
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
                    self.__eaten[self.__pos[0]][self.__pos[1] - 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0]][self.__pos[1] - 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0]][self.__pos[1] - 1] = " "
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
                    self.__eaten[self.__pos[0] + 1][self.__pos[1]] = " "
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0] + 1][self.__pos[1]] = " "
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0] + 1][self.__pos[1]] = " "
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
                    self.__eaten[self.__pos[0]][self.__pos[1] + 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0]][self.__pos[1] + 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0]][self.__pos[1] + 1] = " "
                game_map[self.__pos[0]][self.__pos[1] + 1] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[1] += 1


        if key == 'z':
            if game_map[self.__pos[0] - 1][self.__pos[1]] == "#":
                pass
            else:
                if game_map[self.__pos[0] - 1][self.__pos[1]] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0] - 1][self.__pos[1]] == ".":
                    score.add_score(100)
                    self.__eaten[self.__pos[0] - 1][self.__pos[1]] = " "
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0] - 1][self.__pos[1]] = " "
                if game_map[self.__pos[0] - 1][self.__pos[1]] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0] - 1][self.__pos[1]] = " "
                game_map[self.__pos[0] - 1][self.__pos[1]] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[0] -= 1
        if key == 'q':
            if game_map[self.__pos[0]][self.__pos[1] - 1] == "#":
                pass
            else:
                if game_map[self.__pos[0]][self.__pos[1] - 1] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0]][self.__pos[1] - 1] == ".":
                    score.add_score(100)
                    self.__eaten[self.__pos[0]][self.__pos[1] - 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0]][self.__pos[1] - 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0]][self.__pos[1] - 1] = " "
                game_map[self.__pos[0]][self.__pos[1] - 1] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[1] -= 1

        if key == 's':
            if game_map[self.__pos[0] + 1][self.__pos[1]] == "#":
                pass
            else:
                if game_map[self.__pos[0] + 1][self.__pos[1]] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0] + 1][self.__pos[1]] == ".":
                    score.add_score(100)
                    self.__eaten[self.__pos[0] + 1][self.__pos[1]] = " "
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0] + 1][self.__pos[1]] = " "
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0] + 1][self.__pos[1]] = " "
                game_map[self.__pos[0] + 1][self.__pos[1]] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[0] += 1

        if key == 'd':
            if game_map[self.__pos[0]][self.__pos[1] + 1] == "#":
                pass
            else:
                if game_map[self.__pos[0]][self.__pos[1] + 1] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0]][self.__pos[1] + 1] == ".":
                    score.add_score(100)
                    self.__eaten[self.__pos[0]][self.__pos[1] + 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "x":
                    score.add_score(200)
                    self.__eaten[self.__pos[0]][self.__pos[1] + 1] = " "
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "^":
                    score.add_score(500)
                    self.__eaten[self.__pos[0]][self.__pos[1] + 1] = " "
                game_map[self.__pos[0]][self.__pos[1] + 1] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[1] += 1


        return key, game_map, score, count_coll


class Ghost(MovingEntities):
    """
    Author: Andreas Bombaert
    Date: 6/12/2020
    Ghosts class, this class contains all the necessary methods for the game to make the ghost move +- randomly through the map
    """
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

    def setpos(self, pos_x, pos_y):
        """ This method is only here for tests"""
        self.__pos = [pos_x, pos_y]

    """
    PRE : none
    POST : Ghost pos is a random position, except the pacman position and a wall position
    RAISES : none
    """
    def set_init_pos(self, game_map, pacman):
        self.__pos = [random.randint(1, len(game_map)), random.randint(1, len(game_map[0]))]
        while game_map[self.__pos[0]][self.__pos[1]] == "#" or game_map[self.__pos[0]][self.__pos[1]] == "o":
            self.__pos = [random.randint(1, len(game_map)), random.randint(1, len(game_map[0]))]
        self.__prev = pacman.eaten[self.__pos[0]][self.__pos[1]]
        game_map[self.__pos[0]][self.__pos[1]] = self
        return game_map

    """
    PRE : game map mustn't be empty
    POST : returns the updated game map
    RAISES : TypeError if an argument is not a Ghost
    """
    def moves(self, game_map, direction, flag, pacman):
        # direction 1: upward, 2: left, 3: downward, 4: right
        # flag indicates if the ghost must move again or not, this avoids the ghost to moves twice in a function call
        if flag == 0:
            return game_map
        if direction == 1:
            if game_map[self.__pos[0] - 1][self.__pos[1]] == "#":
                direction = random.randint(2, 4)
                self.moves(game_map, direction, 0, pacman)
            else:
                game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = pacman.eaten[self.__pos[0] - 1][self.__pos[1]]
                game_map[self.__pos[0] - 1][self.__pos[1]] = self

                self.__pos[0] -= 1

        if direction == 2:
            if game_map[self.__pos[0]][self.__pos[1] - 1] == "#":
                direction = random.randint(1, 4)
                while direction == 2:
                    direction = random.randint(1, 4)
                self.moves(game_map, direction, 0, pacman)
            else:
                game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = pacman.eaten[self.__pos[0]][self.__pos[1] - 1]
                game_map[self.__pos[0]][self.__pos[1] - 1] = self

                self.__pos[1] -= 1

        if direction == 3:
            if game_map[self.__pos[0] + 1][self.__pos[1]] == "#":
                direction = random.randint(1, 4)
                while direction == 3:
                    direction = random.randint(1, 4)
                self.moves(game_map, direction, 0, pacman)
            else:
                game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = pacman.eaten[self.__pos[0] + 1][self.__pos[1]]
                game_map[self.__pos[0] + 1][self.__pos[1]] = self

                self.__pos[0] += 1

        if direction == 4:
            if game_map[self.__pos[0]][self.__pos[1] + 1] == "#":
                direction = random.randint(1, 3)
                self.moves(game_map, direction, 0, pacman)
            else:
                game_map[self.__pos[0]][self.__pos[1]] = self.__prev
                self.__prev = pacman.eaten[self.__pos[0]][self.__pos[1] + 1]
                game_map[self.__pos[0]][self.__pos[1] + 1] = self

                self.__pos[1] += 1

        return game_map

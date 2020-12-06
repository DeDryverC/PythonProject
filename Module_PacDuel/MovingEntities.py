import time


class MovingEntities:
    def __init__(self, map_ar):
        self.__pos = [0, 0]
        self.state = 1  # 0: dead, 1: alive
        self.map = map_ar


class Pacman(MovingEntities):
    def __init__(self, lives):
        super().__init__([])
        self.lives = lives

    def setpos(self, pos_x, pos_y):
        self.__pos = [pos_x, pos_x]

    @property
    def pos(self):
        return self.__pos

    collectables = {"*": 100, "X": 200, "^": 500}

    def moves(self, key, game_map, score, count_coll):  # 1: forward, 2: backward, 3: left, 4: right
        if key == ord('z'):
            if game_map[self.__pos[0] - 1][self.__pos[1]] == "#":
                pass
            else:
                if game_map[self.__pos[0] - 1][self.__pos[1]] != " ":
                    count_coll -= 1
                if game_map[self.__pos[0] - 1][self.__pos[1]] == "*":
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
                if game_map[self.__pos[0]][self.__pos[1] - 1] == "*":
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
                if game_map[self.__pos[0] + 1][self.__pos[1]] == "*":
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
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "*":
                    score.add_score(100)
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "x":
                    score.add_score(200)
                if game_map[self.__pos[0]][self.__pos[1] + 1] == "^":
                    score.add_score(500)
                game_map[self.__pos[0]][self.__pos[1] + 1] = "o"
                game_map[self.__pos[0]][self.__pos[1]] = " "
                self.__pos[1] += 1

        return key, game_map, score, count_coll


class Ghost(MovingEntities):
    def __init__(self, map_ar, speed, color):
        super().__init__(map_ar)
        self.speed = speed
        self.color = color
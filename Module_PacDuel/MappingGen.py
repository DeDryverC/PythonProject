import curses
from Projet.PythonProject.Module_PacDuel.MovingEntities import Pacman, Ghost

class Map:
    def __init__(self, file_name, pos1, pos2):
        self.file = file_name
        self.x = pos1
        self.y = pos2
        self.__map_ar = []

    @property
    def map_ar(self):
        return self.__map_ar

    """
        Auth: Andréas Bombaert
        Last date: November 10 2020 - 17h07
        La fonction traduit le fichier en liste contenant la carte
        PRE (file) : Un fichier contenant une représentation textuelle de la carte de jeu
            (array) : Un array de coordonnées contenant la position du joueur (PacMan)
        POST (none) : utilise la librairie curses pour afficher la carte dans la console
        RAISES : FileNotFoundError et IOError
    """

    def gen_map(self):
        try:
            with open(self.file) as file:
                for line in file:
                    curr = []
                    for x in range(0, len(line) - 1):
                        curr.append(line[x])
                    self.__map_ar.append(curr)
            self.__map_ar[self.x][self.y] = "o"
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    """
        Auth: Andréas Bombaert
        Last date: November 10 2020 - 17h05
        La fonction affiche en console la carte contenue dans un array
        PRE (array) : Une représentation de la carte en 2d sous forme de liste de listes
        POST (none) : utilise la librairie curses pour afficher la carte dans la console
        RAISES curses.error : si erreur lors de l'appel de fonctions curses
    """

    # affiche la map sur l'écran
    def cast_map(self, map_ar, stdscr):
        try:
            for x in range(len(map_ar)):
                for y in range(len(map_ar[x])):
                    print(map_ar[x][y])
                    if map_ar[x][y] == "#":
                        stdscr.addstr(x, y, "#")
                    elif map_ar[x][y] == "^":
                        stdscr.addstr(x, y, "^", curses.color_pair(2))
                    elif map_ar[x][y] == "x":
                        stdscr.addstr(x, y, "x", curses.color_pair(1))
                    elif map_ar[x][y] == "*":
                        stdscr.addstr(x, y, "*", curses.color_pair(1))
                    elif map_ar[x][y] == "o":
                        stdscr.addstr(x, y, "o", curses.color_pair(3))
                    elif map_ar[x][y] == " ":
                        stdscr.addstr(x, y, " ")
        except:
            raise curses.error


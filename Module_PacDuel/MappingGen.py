import curses

"""
    Auth: Andréas Bombaert
    Last date: November 10 2020 - 17h07

    La fonction traduit le fichier en liste contenant la carte

    PRE (file) : Un fichier contenant une représentation textuelle de la carte de jeu
        (array) : Un array de coordonnées contenant la position du joueur (PacMan)
        
    POST (none) : utilise la librairie curses pour afficher la carte dans la console
    
    RAISES : FileNotFoundError et IOError
"""


def gen_map(file_to_open, pos1, pos2):

    try:
        map = []
        with open(file_to_open) as file:
            for line in file:
                curr = []
                for x in range(len(line) - 1):
                    curr.append(line[x])
                map.append(curr)
        map[pos1][pos2] = "o"
        return map
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
def cast_map(map, stdscr):
    try:
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == "#":
                    stdscr.addstr(x, y, "#")
                elif map[x][y] == "^":
                    stdscr.addstr(x, y, "^", curses.color_pair(2))
                elif map[x][y] == "x":
                    stdscr.addstr(x, y, "x", curses.color_pair(1))
                elif map[x][y] == "*":
                    stdscr.addstr(x, y, "*", curses.color_pair(1))
                elif map[x][y] == "o":
                    stdscr.addstr(x, y, "o", curses.color_pair(3))
                elif map[x][y] == " ":
                    stdscr.addstr(x, y, " ")
    except:
        raise curses.error

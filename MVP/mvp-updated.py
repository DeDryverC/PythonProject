"""
Auth: Cédric De Dryver, Andréas Bombaert,
Last Date: 10/11/2020

Update 10/11/2020 : -le mvp utilise maintenant des fichiers pour générer les cartes
                    et se déplacer dessus
                    -quelques optimisations et aération du code

Desc: MVP du projet 2TI en python.
"""

# IMPORT SECTION
import curses


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



"""
Auth: Andréas Bombaert
Last date: November 10 2020 - 17h07

La fonction traduit le fichier en liste contenant la carte

PRE (file) : Un fichier contenant une représentation textuelle de la carte de jeu
PRE (array) : Un array de coordonnées contenant la position du joueur (PacMan)
POST (none) : utilise la librairie curses pour afficher la carte dans la console
RAISES FileNotFoundError et IOError
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

"""
Ecrit par Cedric de Dryver le 09 novembre 2020
Déplacé dans une fonction par Andréas le 10 novembre 2020

Description: initialisation de la fenetre avec curses ainsi que l'initialisation 
des paires de couleur
"""
def init_win(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.start_color()
    curses.initscr()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

"""
Ecrit par Cedric de Dryver le 09 novembre 2020
Déplacé dans une fonction par Andréas le 10 novembre 2020

Description: Affichage de fin de partie
"""
def game_won(stdscr, score):
    stdscr.erase()
    gg = "You won ! Congratz"
    endmessage = "Press Q to quit the game"
    stdscr.addstr(1, 1, gg, curses.color_pair(3))
    stdscr.addstr(2, 1, "Score: ", curses.color_pair(3))
    stdscr.addstr(2, 7, str(score.get_score), curses.color_pair(3))
    stdscr.addstr(3, 1, endmessage, curses.color_pair(3))
    stdscr.refresh()
    key = stdscr.getch()
    if key == ord('q'):
        return True

""" Main function
Auth: Cédric De Dryver, November 09 2020 - 17h27
Modified by Andréas Bombaert, November 10 2020 - 17h

All lines have a step-by-step description in French.

But this main function allows you to play the simplified pac man game. the keys are Z: up, S: down, Q: left, D: right.
It's better with an AZERTY keyboard.
"""

def main(stdscr):
    # Initialisation de la library curse:
    init_win(stdscr)

    # Position du PacMan et sa position initiale.
    pos_pacman = [4, 9]

    # Initialisation du score.
    score = ScoreCount()
    count_coll = 49

    # Initialisation de la carte
    map = gen_map("data/map.txt", pos_pacman[0], pos_pacman[1])

    # Initialisation du Terrain curses
    cast_map(map, stdscr)

    '''
    Voici la boucle du jeu,
    pour quitter cette boucle, appuyez sur "p" ou rammassez tout les collectibles
    touches de mouvement:
    Z : Haut
    S : Bas
    Q : Gauche
    D : Droite
    '''
    while True:
        stdscr.addstr(1, 22, "Score: ", curses.color_pair(3))  # Refreshing du score a chaques mouvement.
        stdscr.addstr(1, 29, str(score.get_score), curses.color_pair(3))

        #affichage de la carte au début
        cast_map(map, stdscr)

        # Si le compteur de collectible atteint 0, alors la partie est fini et affiche un ecran de victoire (Appuyer
        # sur Q pour quitter cet ecran).
        if count_coll == 0:
            if game_won(stdscr, score):
                break

        # On va lire les touches que l'user va rentrer.
        key = stdscr.getch()

        # Reference : Haut(y => -∞) Bas(y => +∞) Gauche(x => -∞) Droite(x => +∞)
        # => : tend vers ...
        # Il y a sous ce commentaire,les 4 touches qui permettent de se déplacer.
        # A Chaques fois que le PacMan veut se déplacer, il verifie ce qu'il y a devant lui, et si il peut,
        # il se déplace et récupere des points (si il y en a)
        # Si l'user decide, il peut quitter le jeu en appuyant sur P (attention pas de verification).

        if key == ord('z'):
            if map[pos_pacman[0] - 1][pos_pacman[1]] == "#":
                pass
            elif map[pos_pacman[0] - 1][pos_pacman[1]] == "*":
                map[pos_pacman[0] - 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] -= 1
                count_coll -= 1
                score.add_score(100)
            elif map[pos_pacman[0] - 1][pos_pacman[1]] == "x":
                map[pos_pacman[0] - 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] -= 1
                count_coll -= 1
                score.add_score(200)
            elif map[pos_pacman[0] - 1][pos_pacman[1]] == "^":
                map[pos_pacman[0] - 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] -= 1
                count_coll -= 1
                score.add_score(500)
            elif map[pos_pacman[0] - 1][pos_pacman[1]] == " ":
                map[pos_pacman[0] - 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] -= 1

        elif key == ord('s'):
            if map[pos_pacman[0] + 1][pos_pacman[1]] == "#":
                pass
            elif map[pos_pacman[0] + 1][pos_pacman[1]] == "*":
                map[pos_pacman[0] + 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] += 1
                count_coll -= 1
                score.add_score(100)
            elif map[pos_pacman[0] + 1][pos_pacman[1]] == "x":
                map[pos_pacman[0] + 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] += 1
                count_coll -= 1
                score.add_score(200)
            elif map[pos_pacman[0] + 1][pos_pacman[1]] == "^":
                map[pos_pacman[0] + 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] += 1
                count_coll -= 1
                score.add_score(500)
            elif map[pos_pacman[0] + 1][pos_pacman[1]] == " ":
                map[pos_pacman[0] + 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] += 1

        elif key == ord('q'):
            if map[pos_pacman[0]][pos_pacman[1] - 1] == "#":
                pass
            elif map[pos_pacman[0]][pos_pacman[1] - 1] == "*":
                map[pos_pacman[0]][pos_pacman[1] - 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] -= 1
                count_coll -= 1
                score.add_score(100)
            elif map[pos_pacman[0]][pos_pacman[1] - 1] == "x":
                map[pos_pacman[0]][pos_pacman[1] - 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] -= 1
                count_coll -= 1
                score.add_score(200)
            elif map[pos_pacman[0]][pos_pacman[1] - 1] == "^":
                map[pos_pacman[0]][pos_pacman[1] - 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] -= 1
                count_coll -= 1
                score.add_score(500)
            elif map[pos_pacman[0]][pos_pacman[1] - 1] == " ":
                map[pos_pacman[0]][pos_pacman[1] - 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] -= 1

        elif key == ord('d'):
            if map[pos_pacman[0]][pos_pacman[1] + 1] == "#":
                pass
            elif map[pos_pacman[0]][pos_pacman[1] + 1] == "*":
                map[pos_pacman[0]][pos_pacman[1] + 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] += 1
                count_coll -= 1
                score.add_score(100)
            elif map[pos_pacman[0]][pos_pacman[1] + 1] == "x":
                map[pos_pacman[0]][pos_pacman[1] + 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] += 1
                count_coll -= 1
                score.add_score(200)
            elif map[pos_pacman[0]][pos_pacman[1] + 1] == "^":
                map[pos_pacman[0]][pos_pacman[1] + 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] += 1
                count_coll -= 1
                score.add_score(500)
            elif map[pos_pacman[0]][pos_pacman[1] + 1] == " ":
                map[pos_pacman[0]][pos_pacman[1] + 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] += 1

        elif key == ord('p'):
            break


if __name__ == "__main__":
    curses.wrapper(main)
"""
Auth: Cédric De Dryver, Andréas Bombaert,
Last Date: 10/11/2020

Update 10/11/2020 : -le mvp utilise maintenant des fichiers pour générer les cartes
                    et se déplacer dessus
                    -quelques optimisations et aération du code

VERSION : INSTABLE

Desc: MVP du projet 2TI en python.

"""

# IMPORT SECTION
import curses

from PythonProject.Module_PacDuel.MappingGen import MapGenerator   # Si jamais, supprimez cette ligne et re-importez grace a Pycharm ligne 82
from PythonProject.Module_PacDuel.ScoreCount import ScoreCount     # Pareil ligne 78


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
    map = MapGenerator.gen_map("data/map.txt", pos_pacman[0], pos_pacman[1])

    # Initialisation du Terrain curses
    MapGenerator.cast_map(map, stdscr)

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
        MapGenerator.cast_map(map, stdscr)

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
            else:
                if map[pos_pacman[0] - 1][pos_pacman[1]] != " ":
                    count_coll -= 1
                if map[pos_pacman[0] - 1][pos_pacman[1]] == "*":
                    score.add_score(100)
                if map[pos_pacman[0]][pos_pacman[1] - 1] == "x":
                    score.add_score(200)
                if map[pos_pacman[0] - 1][pos_pacman[1]] == "^":
                    score.add_score(500)
                map[pos_pacman[0] - 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] -= 1

        if key == ord('q'):
            if map[pos_pacman[0]][pos_pacman[1] - 1] == "#":
                pass
            else:
                if map[pos_pacman[0]][pos_pacman[1] - 1] != " ":
                    count_coll -= 1
                if map[pos_pacman[0]][pos_pacman[1] - 1] == "*":
                    score.add_score(100)
                if map[pos_pacman[0]][pos_pacman[1] - 1] == "x":
                    score.add_score(200)
                if map[pos_pacman[0]][pos_pacman[1] - 1] == "^":
                    score.add_score(500)
                map[pos_pacman[0]][pos_pacman[1] - 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] -= 1

        if key == ord('s'):
            if map[pos_pacman[0] + 1][pos_pacman[1]] == "#":
                pass
            else:
                if map[pos_pacman[0] + 1][pos_pacman[1]] != " ":
                    count_coll -= 1
                if map[pos_pacman[0] + 1][pos_pacman[1]] == "*":
                    score.add_score(100)
                if map[pos_pacman[0] + 1][pos_pacman[1]] == "x":
                    score.add_score(200)
                if map[pos_pacman[0] + 1][pos_pacman[1]] == "^":
                    score.add_score(500)
                map[pos_pacman[0] + 1][pos_pacman[1]] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[0] += 1

        if key == ord('d'):
            if map[pos_pacman[0]][pos_pacman[1] + 1] == "#":
                pass
            else:
                if map[pos_pacman[0]][pos_pacman[1] + 1] != " ":
                    count_coll -= 1
                if map[pos_pacman[0]][pos_pacman[1] + 1] == "*":
                    score.add_score(100)
                if map[pos_pacman[0]][pos_pacman[1] + 1] == "x":
                    score.add_score(200)
                if map[pos_pacman[0]][pos_pacman[1] + 1] == "^":
                    score.add_score(500)
                map[pos_pacman[0]][pos_pacman[1] + 1] = "o"
                map[pos_pacman[0]][pos_pacman[1]] = " "
                pos_pacman[1] += 1

        if key == ord('p'):
            break


if __name__ == "__main__":
    curses.wrapper(main)

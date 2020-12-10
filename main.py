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
import random
import time
from multiprocessing import Process, Queue

from Projet.PythonProject.Module_PacDuel.MappingGen import Map
from Projet.PythonProject.Module_PacDuel.MovingEntities import Pacman, Ghost
from Projet.PythonProject.Module_PacDuel.ScoreCount import ScoreCount

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


def game_lost(stdscr, score):
    stdscr.erase()
    gg = "You Lost ! Better luck next time"
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


def game_loop(stdscr, lives):
    # Initialisation de la library curse:
    init_win(stdscr)

    # Position du PacMan et sa position initiale.
    pacman = Pacman(lives)
    pacman.setpos(4, 9)

    # Initialisation du score.
    score = ScoreCount()
    count_coll = 49

    # Initialisation de la carte
    game_map = Map("data/map.txt", pacman.pos[0], pacman.pos[1])
    game_map.gen_map()
    map_ar = game_map.map_ar


    # Position du/des fantomes et leur(s) position initiale
    ghost1 = Ghost(curses.color_pair(2))
    map_ar = ghost1.set_init_pos(map_ar)

    # Initialisation du Terrain curses
    game_map.cast_map(map_ar, stdscr)

    '''
    Voici la boucle du jeu,
    pour quitter cette boucle, appuyez sur "p" ou ramassez tout les collectibles
    touches de mouvement:
    Z : Haut
    S : Bas
    Q : Gauche
    D : Droite
    '''

    while True:
        if pacman.lives == 0:
            if game_lost(stdscr, score):
                break

        stdscr.addstr(1, 22, "Score: ", curses.color_pair(3))  # Refreshing du score a chaque mouvement.
        stdscr.addstr(1, 29, str(score.get_score), curses.color_pair(3))
        stdscr.addstr(1, 33, "Vies : ", curses.color_pair(3))
        stdscr.addstr(1, 40, str(pacman.lives), curses.color_pair(3))

        # affichage de la carte au début
        game_map.cast_map(map_ar, stdscr)

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

        if key == ord('z') or key == ord('q') or key == ord('s') or key == ord('d'):
            key, map_ar, score, count_coll = pacman.moves(key, map_ar, score, count_coll)
            map_ar = ghost1.moves(map_ar, random.randint(1, 4))
            if pacman.on_ghost(ghost1):
                pacman.death()
                # todo fonction pour afficher qu'une vie a été perdue + presser une touche pour passer a la prochaine vie
                game_loop(stdscr, pacman.lives)
        if key == ord('p'):
            break


def main(stdscr):
    game_loop(stdscr, 1)


if __name__ == "__main__":
    curses.wrapper(main)

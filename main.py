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

from multiprocessing import Process, Queue

# from Projet.Module_PacDuel.MappingGen import Map
# from Projet.Module_PacDuel.MovingEntities import Pacman
# from Projet.Module_PacDuel.ScoreCount import ScoreCount

from PythonProject.Module_PacDuel.MappingGen import Map
from PythonProject.Module_PacDuel.MenuGen import Menu
from PythonProject.Module_PacDuel.MovingEntities import Pacman
from PythonProject.Module_PacDuel.ScoreCount import ScoreCount

"""
Ecrit par Cedric de Dryver le 09 novembre 2020
Déplacé dans une fonction par Andréas le 10 novembre 2020
Description: initialisation de la fenetre avec curses ainsi que l'initialisation 
des paires de couleur
"""


def init_win(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.start_color()
    curses.initscr()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
    y, x = stdscr.getmaxyx()
    resize = curses.is_term_resized(y, x)

    # Action in loop if resize is True:
    if resize is True:
        stdscr.clear()
        curses.resizeterm(30, 25)
        stdscr.refresh()



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


def print_menu(stdscr, selected_row_idx):
    h, w = stdscr.getmaxyx()
    menu = ['Gamemode', 'Scoreboard', 'Settings', 'Exit']
    pacman_logo = ["___________     ____   _____ _____    ____","  \_  __ \__ \  _/ ___\ /      \__  \  /    \ ","     |  |_>/ __ \\\   \___|  | |  |/ _  \|   |  \  ","     |  __(____  /\____  >__|_|_ (____  /___|  /  ","   |__|      \/      \/       \/    \/     \/ "]
    for idx, row in enumerate(pacman_logo):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(pacman_logo) // 2 + idx
        stdscr.addstr(y, x,row, curses.color_pair(4))


    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx + 6
        if idx == (selected_row_idx-5):
            stdscr.attron(curses.color_pair(5))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(5))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def menu_leave(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    leave_menu = ['Yes', 'No']
    leave_message = "Are you sure you want to exit ?"
    x = w // 2 - len(leave_message) // 2
    y = h // 2 - 3
    stdscr.addstr(y, x, leave_message)
    for idx, row in enumerate(leave_menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(leave_menu) // 2 + idx
        if idx == (selected_row_idx - 4):
            stdscr.attron(curses.color_pair(5))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(5))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

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
    pacman = Pacman(3)
    pacman.setpos(4, 9)

    # Initialisation du score.
    score = ScoreCount()
    count_coll = 49

    current_row = 5
    menu = ['Gamemode', 'Scoreboard', 'Settings', 'Exit']
    print_menu(stdscr, current_row)



    stdscr.refresh()
    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP or key == ord('z') and current_row > 5:
            current_row -= 1

        elif key == curses.KEY_DOWN or key == ord('s') and current_row < len(menu) -1 + 5:
            current_row += 1

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 5:
                pass
                # GAMEMODE CHOICE
            elif current_row == 6:
                pass
                # DISPLAY SCOREBOARD
            elif current_row == 7:
                pass
                # DISPLAY SETTINGS
            elif current_row == 8:
                leave_current_row = 4
                menu_leave(stdscr, leave_current_row)
                while True:
                    key = stdscr.getch()
                    if key == curses.KEY_UP or key == ord('z') and leave_current_row == 5:
                        leave_current_row -= 1
                    elif key == curses.KEY_DOWN or key == ord('s') and leave_current_row == 4:
                        leave_current_row += 1
                    elif key == curses.KEY_ENTER or key in [10, 13]:
                        if leave_current_row == 4:
                            exit()
                        elif leave_current_row == 5:
                            stdscr.clear()
                            break
                    menu_leave(stdscr, leave_current_row)
                    stdscr.refresh()
                # VERIFICATION BEFORE LEAVING
        print_menu(stdscr, current_row)
        stdscr.refresh()

"""
    # Initialisation de la carte
    game_map = Map("data/map.txt", pacman.pos[0], pacman.pos[1])
    game_map.gen_map()
    map_ar = game_map.map_ar

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
        stdscr.addstr(1, 22, "Score: ", curses.color_pair(3))  # Refreshing du score a chaques mouvement.
        stdscr.addstr(1, 29, str(score.get_score), curses.color_pair(3))

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
        if key == ord('p'):
            break
"""

if __name__ == "__main__":
    curses.wrapper(main)
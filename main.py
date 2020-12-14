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


from Projet.PythonProject.Module_PacDuel.MappingGen import Map
from Projet.PythonProject.Module_PacDuel.MovingEntities import Pacman, Ghost
from Projet.PythonProject.Module_PacDuel.ScoreCount import ScoreCount
from Projet.PythonProject.Module_PacDuel.MenuGen import Menu


def init_win(stdscr):
    """
    Ecrit par Cedric de Dryver le 09 novembre 2020
    Déplacé dans une fonction par Andréas le 10 novembre 2020
    Description: initialisation de la fenetre avec curses ainsi que l'initialisation
    des paires de couleur
    """

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
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLUE)
    y, x = stdscr.getmaxyx()
    resize = curses.is_term_resized(y, x)

    # Resize si c'est trop petit
    if resize is True:
        stdscr.clear()
        curses.resizeterm(30, 25)
        stdscr.refresh()


def game_won(stdscr, score):
    """
        Ecrit par Cedric de Dryver le 09 novembre 2020
        Déplacé dans une fonction par Andréas le 10 novembre 2020
        Description: Affichage de fin de partie
    """

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


def life_lost(stdscr, lives, score):
    stdscr.erase()
    msg = ""
    if lives > 1:
        msg = f"You lost one life, you have {lives} lives left!"
    elif lives == 1:
        msg = f"You lost one life, you have {lives} life left!"
    else:
        game_lost(stdscr, score)
    nxt = "Press Enter to go to next life"

    stdscr.addstr(1, 1, msg, curses.color_pair(3))
    stdscr.addstr(3, 1, nxt, curses.color_pair(3))
    stdscr.refresh()

    key = stdscr.getch()
    if key == curses.KEY_ENTER:
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
        stdscr.erase()
        stdscr.refresh()
        return True


def clear_window(stdscr):
    stdscr.erase()
    stdscr.refresh()


def game_loop(stdscr, lives):
    """ Main function
    Auth: Cédric De Dryver, November 09 2020 - 17h27
    Modified by Andréas Bombaert, November 10 2020 - 17h
    All lines have a step-by-step description in French.
    But this main function allows you to play the simplified pac man game.
    the keys are Z: up, S: down, Q: left, D: right.
    It's better with an AZERTY keyboard.
    """

    # Initialisation de la library curse:
    init_win(stdscr)

    # Position du PacMan et sa position initiale.
    pacman = Pacman(lives)
    pacman.setpos(4, 9)

    # Initialisation de la carte
    game_map = Map("data/map1.txt", pacman.pos[0], pacman.pos[1])
    game_map.gen_map()
    map_ar = game_map.map_ar

    # Position du/des fantomes et leur(s) position initiale
    ghosts = []
    ghost1 = Ghost(curses.color_pair(2))
    ghosts.append(ghost1)
    map_ar = ghost1.set_init_pos(map_ar)

    # Initialisation du Terrain curses
    game_map.cast_map(map_ar, stdscr)

    # Initialisation du score.
    score = ScoreCount()
    count_coll = game_map.collectibles

    positions = [pacman.pos]
    for x in ghosts:
        positions.append(x.pos)

    while True:
        """
            boucle du jeu,
            pour quitter cette boucle, appuyez sur "p" ou ramassez tout les collectibles
            touches de mouvement:
            Z : Haut
            S : Bas
            Q : Gauche
            D : Droite
        """
        if pacman.lives <= 0:
            if game_lost(stdscr, score):
                break

        stdscr.addstr(1, 22, "Score: ", curses.color_pair(3))  # Refreshing du score a chaque mouvement.
        stdscr.addstr(1, 29, str(score.get_score), curses.color_pair(3))
        stdscr.addstr(1, 33, "Lives : ", curses.color_pair(3))
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
            prev_pacman = pacman.pos.copy()
            key, map_ar, score, count_coll = pacman.moves(key, map_ar, score, count_coll)  # pacman moves

            direction = random.randint(1, 4)
            for x in ghosts:
                # direction 1: forward, 2: left, 3: backward, 4: right
                prev_ghost = x.pos.copy()
                map_ar = x.moves(map_ar, direction)  # every ghost moves
                if x.pos == prev_pacman and pacman.pos == prev_ghost:
                    pacman.death()
                    life_lost(stdscr, pacman.lives, score)
                    stdscr.erase()
                    stdscr.refresh()
                    game_loop(stdscr, pacman.lives)

            positions = [[pacman.pos]]
            for x in ghosts:
                positions.append(x.pos)

        if pacman.on_ghost(ghosts):
            pacman.death()
            life_lost(stdscr, pacman.lives, score)
            stdscr.erase()
            stdscr.refresh()
            game_loop(stdscr, pacman.lives)

        if key == ord('p'):
            break


def menu_gamemode(stdscr, menu_obj):
    """
    auth: C. De Dryver
        Cette fonction est utilisé pour creer un menu gamemode,
        et l'utilisateur peut choisir l'un des choix qui s'offre a lui
        en naviguant d'une réponse a l'autre.
        PRE: (curses) stdscr : Interface console sur laquelle on travaille
             (Menu) menu_obj : Classe local qui nous permet de creer un menu

        POST: Creer un choix entre le mode solo ou le mode duo. Solo / Duo
    """

    gamemode_current_row = 6
    menu_obj.menu_gamemode(stdscr, gamemode_current_row)
    while True:
        key = stdscr.getch()
        if (key == curses.KEY_LEFT or key == ord('q')) and gamemode_current_row == 7:
            gamemode_current_row -= 1
        elif (key == curses.KEY_RIGHT or key == ord('d')) and gamemode_current_row == 6:
            gamemode_current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if gamemode_current_row == 6:
                stdscr.clear()
                game_loop(stdscr, 3)
            elif gamemode_current_row == 7:
                stdscr.clear()
                break
        menu_obj.menu_gamemode(stdscr, gamemode_current_row)
        stdscr.refresh()


def menu_exit(stdscr, menu_obj):
    """
    auth: C. De Dryver
        Cette fonction est utilisé pour creer un menu exit,
        et l'utilisateur peut choisir l'un des choix qui s'offre a lui
        en naviguant d'une réponse a l'autre.
        PRE: (curses) stdscr : Interface console sur laquelle on travaille
             (Menu) menu_obj : Classe local qui nous permet de creer un menu

        POST: Creer un choix pour quitter l'application. Yes / No
    """

    leave_current_row = 4
    menu_obj.menu_leave(stdscr, leave_current_row)
    while True:
        key = stdscr.getch()
        if (key == curses.KEY_UP or key == ord('z')) and leave_current_row == 5:
            leave_current_row -= 1
        elif (key == curses.KEY_DOWN or key == ord('s')) and leave_current_row == 4:
            leave_current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if leave_current_row == 4:
                exit()
            elif leave_current_row == 5:
                stdscr.clear()
                break
        menu_obj.menu_leave(stdscr, leave_current_row)
        stdscr.refresh()


def main(stdscr):
    # Initialisation de la library curse:
    init_win(stdscr)
    menu_obj = Menu(5)
    current_row = menu_obj.current_row
    menu = menu_obj.menu_tab
    menu_obj.print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()
        if (key == curses.KEY_UP or key == ord('z')) and current_row > 5:
            current_row -= 1
        elif (key == curses.KEY_DOWN or key == ord('s')) and current_row < len(menu) - 1 + 5:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:

            if current_row == 5:
                menu_gamemode(stdscr, menu_obj)
            elif current_row == 6:
                pass
                # DISPLAY SCOREBOARD
            elif current_row == 7:
                pass
                # DISPLAY SETTINGS
            elif current_row == 8:
                menu_exit(stdscr, menu_obj)
        menu_obj.print_menu(stdscr, current_row)
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)

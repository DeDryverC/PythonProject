import curses

"""
Class : Menu
Author : C. De Dryver
Cette classe permet d'afficher un menu ou l'on peut choisir le mode que l'on veut, c'est a dire on a le choix du
gamemode (solo ou duo), le choix de voir la page des score (TODO), gerer les paramètre grace aux settings, ou quitter
l'application avec Exit
"""


class Menu:
    """
    On va creer le menu et toute les variables qui vont avec
    PRE : start_row (int) : Determine la ou va commencer le choix (en dessous du logo)
    POST: Va creer les variables globales pour le menu pacman.

    RAISE: ValueError : start_row doit etre un int.
    """

    def __init__(self, start_row):
        if isinstance(start_row, type(int)):
            raise TypeError

        self.__current_row = start_row
        self.__menu = ['Gamemode', 'Scoreboard', 'Settings', 'Exit']
        self.__logo = ["___________     ____   _____ _____    ____", "  \_  __ \__ \  _/ ___\ /      \__  \  /    \ ",
                       "     |  |_>/ __ \\\   \___|  | |  |/ __ \|   |  \  ",
                       "     |  __(____  /\____  >__|_|_ (____  /___|  /  ",
                       "   |__|      \/      \/       \/    \/     \/ "]
        self.__leave_menu = ['Yes', 'No']
        self.__leave_message = "Are you sure you want to exit ?"
        self.__gamemode_menu = ['Solo', 'Duo']
        self.__gamemode_message = 'Choose your gamemode'

    @property
    def menu_tab(self):
        return self.__menu

    @property
    def current_row(self):
        return self.__current_row

    """
    Cette méthode va permettre d'afficher dans une interface console, le logo pac man et un menu ou l'on va
    choisir l'action (le menu qu'on choisit a un fond gris-blanc sur des lettre en noir.
    
    PRE:    stdscr (curses)  : Importation du screen (fenetre) curse avec les paramètres définit dans main.
            selected_row_idx (int) : Permet de savoir a quel index se situe l'utilisateur dans son choix dans le menu.
            
    POST:   Grace au stdscr qu'on importe, tout les changement seront directement appliquée a celui ci, on ne retourne
                rien et de plus, les changement qu'on a fait apparaiterons dans la fenètre grace au stdscr.refresh()
                Mais cette methode va creer un menu pacman.
    
    RAISE: TypeError : selected_row_idx doit etre un int.
    """

    def print_menu(self, stdscr, selected_row_idx):

        if isinstance(selected_row_idx, type(int)):
            raise TypeError

        h, w = self.__print_logo(stdscr)

        for idx, row in enumerate(self.__menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.__menu) // 2 + idx + 6
            if idx == (selected_row_idx - 5):
                stdscr.attron(curses.color_pair(5))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(5))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()

    """
    Cette méthode permet de re-créer un menu, ou les choix disponible sont yes-no pour verifier que l'utilisateur veut
    quitter l'application, si il choisit oui, la fenètre se ferme, le code s'arrète. Si il choisit non, il reviendra 
    sur le menu précédent.
    
    PRE:    stdscr (curses)  : Importation du screen (fenetre) curse avec les paramètres définit dans main.
            selected_row_idx (int) : Permet de savoir a quel index se situe l'utilisateur dans son choix dans le menu.
            
    POST: Va creer une verification pour quitter l'application dans l'interface stdscr.
    
    RAISE: TypeError : selected_row_idx doit etre un int.
    """

    def menu_leave(self, stdscr, selected_row_idx):

        if isinstance(selected_row_idx, type(int)):
            raise TypeError

        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x = w // 2 - len(self.__leave_message) // 2
        y = h // 2 - 3
        stdscr.addstr(y, x, self.__leave_message)
        for idx, row in enumerate(self.__leave_menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.__leave_menu) // 2 + idx
            if idx == (selected_row_idx - 4):
                stdscr.attron(curses.color_pair(5))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(5))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    """
    Cette méthode va creer un mini-menu lorsque l'utilisateur a choisit Gamemode, il va pouvoir choisir le mode Solo
    ou le mode Duel ( Duel n'est pas encore implémenté donc ça retournera au menu de base.
    
    PRE:    stdscr (curses)  : Importation du screen (fenetre) curse avec les paramètres définit dans main.
            selected_row_idx (int) : Permet de savoir a quel index se situe l'utilisateur dans son choix dans le menu.
            
    POST: Va creer un choix entre le mode solo ou le mode Duo dans l'interface stdscr
    
    RAISE: TypeError : selected_row_idx doit etre un int.
    """

    def menu_gamemode(self, stdscr, selected_row_idx):

        if isinstance(selected_row_idx, type(int)):
            raise TypeError

        stdscr.clear()
        h, w = self.__print_logo(stdscr)

        x = w // 2 - len(self.__gamemode_message) // 2
        y = h // 2 + 6
        stdscr.addstr(y, x, self.__gamemode_message)
        for idx, row in enumerate(self.__gamemode_menu):
            if idx == 0 and idx == selected_row_idx - 6:
                x = w // 2 - len(self.__gamemode_menu[0]) - 2
                stdscr.addstr(y + 1, x, self.__gamemode_menu[0], curses.color_pair(5))
            elif idx == 0:
                x = w // 2 - len(self.__gamemode_menu[0]) - 2
                stdscr.addstr(y + 1, x, self.__gamemode_menu[0])
            if idx == 1 and idx == selected_row_idx - 6:
                x = w // 2 + 2
                stdscr.addstr(y + 1, x, self.__gamemode_menu[1], curses.color_pair(5))
            elif idx == 1:
                x = w // 2 + 2
                stdscr.addstr(y + 1, x, self.__gamemode_menu[1])

    """
    Methode privée, car on va re-creer plusieurs fois le logo dans les differents menu, alors pour éviter des doublons
    de code inutiles, voici une fonction qui va creer le logo pacman.
    
    PRE: stdscr (curses)  : Importation du screen (fenetre) curse avec les paramètres définit dans main.
    
    POST:   va créer un logo sur l'interface stdscr
            (int) h : hauteur de la fenètre stdscr.
            (int) w : largeur de la fenetre stdscr
    """

    def __print_logo(self, stdscr):
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(self.__logo):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.__logo) // 2 + idx
            stdscr.addstr(y, x, row, curses.color_pair(4))
        return h, w

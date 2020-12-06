import curses


class Menu:
    def __init__(self, filename, color_filename):
        self.__filename = filename
        self.__color_filename = color_filename
        self.__menu_ar = []
        self.__menu_color_ar = []

    @property
    def menu_ar(self):
        return self.__menu_ar

    @property
    def color_menu_ar(self):
        return self.__menu_color_ar

    def gen_menu(self):
        try:
            with open(self.__filename) as file:
                for line in file:
                    curr = []
                    for x in range(0, len(line) - 1):
                        curr.append(line[x])
                    self.__menu_ar.append(curr)
            with open(self.__color_filename) as file:
                for line in file:
                    curr = []
                    for x in range(0, len(line) - 1):
                        curr.append(line[x])
                    self.__menu_color_ar.append(curr)

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')


    """
    
    RAISE: curses.error : Writing outside the pad, window, or subwindow will cause a curses.error Exception.  
                        Also, attempting to write the lower right corner of a pad, window, or sub window will cause an 
                        exception to be raised after the character is printed.  You may safely ignore the error in this 
                        case.
    """
    def cast_menu(self, menu_ar, color_menu_ar, stdscr):
        for x in range(len(menu_ar)):
            for y in range(len(menu_ar[x])):
                if color_menu_ar[x][y]== " ":
                    stdscr.addstr(x, y, str(menu_ar[x][y]))
                elif color_menu_ar[x][y] == "4":
                    stdscr.addstr(x, y, str(menu_ar[x][y]), curses.color_pair(4))


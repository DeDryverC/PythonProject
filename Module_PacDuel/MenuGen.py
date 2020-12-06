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

    def cast_menu(self, menu_ar, color_menu_ar, stdscr):
        try:
            for x in range(len(menu_ar)):
                for y in range(len(menu_ar[x])):
                    stdscr.addstr(x, y, menu_ar[x][y], curses.color_pair(color_menu_ar[x][y]))
        except:
            raise curses.error


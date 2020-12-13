import curses


class Menu:
    def __init__(self, start_row):
        self.__current_row = start_row
        self.__menu = ['Gamemode', 'Scoreboard', 'Settings', 'Exit']
        self.__logo = ["___________     ____   _____ _____    ____","  \_  __ \__ \  _/ ___\ /      \__  \  /    \ ","     |  |_>/ __ \\\   \___|  | |  |/ _  \|   |  \  ","     |  __(____  /\____  >__|_|_ (____  /___|  /  ","   |__|      \/      \/       \/    \/     \/ "]
        self.__leave_menu = ['Yes', 'No']
        self.__leave_message = "Are you sure you want to exit ?"

    @property
    def menu_tab(self):
        return self.__menu

    @property
    def current_row(self):
        return self.__current_row

    def print_menu(self, stdscr, selected_row_idx):
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(self.__logo):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.__logo) // 2 + idx
            stdscr.addstr(y, x, row, curses.color_pair(4))

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

    def menu_leave(self, stdscr, selected_row_idx):
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


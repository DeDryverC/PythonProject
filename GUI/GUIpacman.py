from kivy import Config
from kivy.app import App
from kivy.core.window import Window

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock

from kivy.uix import widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget

from PythonProject.Module_PacDuel.MovingEntities import Ghost


class GameApp(App):
    def __init__(self, file, pos_x, pos_y, pacman, **kwargs):
        super(GameApp, self).__init__(**kwargs)
        self.__filename = file
        self.__key = ''
        self.__pos= [pos_x, pos_y]
        self.__map_ar = []
        self.__collectibles = 0
        self._init_map = False
        self.__pacman = pacman
        self.__prev_pacman = ''
        self.__score = 0
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    @property
    def prev_pacman(self):
        return self.__prev_pacman


    @property
    def map_ar(self):
        return self.__map_ar

    @property
    def collectibles(self):
        return self.__collectibles

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def key(self):
        return str(self.__key)

    @property
    def init_map(self):
        return self._init_map

    def create_game(self):
        try:
            with open(self.__filename) as file:
                for line in file:
                    curr = []
                    for x in range(0, len(line) - 1):
                        curr.append(line[x])
                    self.__map_ar.append(curr)
            self.__map_ar[self.__pos[0]][self.__pos[1]] = "o"
        except FileNotFoundError:
                print('Fichier introuvable.')
        except IOError:
                print('Erreur IO.')

        box = self.root.ids.main_box
        box.clear_widgets()
        grid = GridLayout(cols=len(self.__map_ar[0]), rows=len(self.__map_ar))

        for y in range(len(self.__map_ar)):
            for x in range(len(self.__map_ar[y])):
                if self.__map_ar[y][x] == " ":
                    grid.add_widget(Label(text=""))
                if self.__map_ar[y][x] == "#":
                    grid.add_widget(Image(source='data/mur.png'))
                elif self.__map_ar[y][x] == "^":
                    self.__collectibles += 1
                    grid.add_widget(Image(source='data/fruit.png'))
                elif self.__map_ar[y][x] == "x":
                    self.__collectibles += 1
                    grid.add_widget(Image(source='data/ballspe.png'))
                elif self.__map_ar[y][x] == ".":
                    self.__collectibles += 1
                    grid.add_widget(Image(source='data/ball.png'))
                elif self.__map_ar[y][x] == "o":
                    grid.add_widget(Image(source='data/pacman.gif'))
                elif isinstance(self.__map_ar[y][x], Ghost):
                    grid.add_widget(Label(text='Monstre'))

        box.add_widget(grid)
        self.refresh()


    def refresh(self):

        box = self.root.ids.main_box
        box.clear_widgets()
        grid = GridLayout(cols=len(self.__map_ar[0]), rows=len(self.__map_ar))

        for y in range(len(self.__map_ar)):
            for x in range(len(self.__map_ar[y])):
                if self.__map_ar[y][x] == " ":
                    grid.add_widget(Label(text=""))
                if self.__map_ar[y][x] == "#":
                    grid.add_widget(Image(source='data/mur.png'))
                elif self.__map_ar[y][x] == "^":
                    grid.add_widget(Image(source='data/fruit.png'))
                elif self.__map_ar[y][x] == "x":
                    grid.add_widget(Image(source='data/ballspe.png'))
                elif self.__map_ar[y][x] == ".":
                    grid.add_widget(Image(source='data/ball.png'))
                elif self.__map_ar[y][x] == "o":
                    grid.add_widget(Image(source='data/pacman.gif'))
                elif isinstance(self.__map_ar[y][x], Ghost):
                    grid.add_widget(Label(text='Monstre'))

        box.add_widget(grid)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.__key = str(keycode[1])
        if keycode[1] == ord('z') or keycode[1] == ord('q') or keycode[1] == ord('s') or keycode[1] == ord('d'):
            self.__prev_pacman = self.pacman.pos.copy()
            self.__key, self.__map_ar, score, count_coll = self.pacman.moves(keycode[1], self.__map_ar, self.__score, self.__collectibles)
        return True

    def life_lost(self, lives, score):
        box = self.root.ids.main_box
        box.clear_widgets()
        box2 = BoxLayout()
        if lives > 1:
            box2.add_widget(Label(text=f"You lost one life, you have {lives} lives left!"))
        elif lives == 1:
            box2.add_widget(Label(text=f"You lost one life, you have {lives} life left!"))
        else:
            self.game_lost(score)
        box2.add_widget(Label(text= "Press any key to go to next life"))

        box.add_widget(box2)

        self.refresh()

        key = self.keyboard_list()
        if key!= None:
            return True

    def game_lost(self, score):
        box = self.root.ids.main_box
        box.clear_widgets()

        box2 = BoxLayout()
        box2.add_widget(Label(text= "You Lost ! Better luck next time"))
        box2.add_widget(Label(text="Score:"))
        box2.add_widget(Label(text=str(score.get_score)))
        box2.add_widget(Label(text="Press any key to quit the game"))

        box.add_widget(box2)

        self.refresh()
        key = self.keyboard_list()

        if key != None:
            return True

    def game_won(self, score):
        """
            Ecrit par Cedric de Dryver le 09 novembre 2020
            Déplacé dans une fonction par Andréas le 10 novembre 2020
            Description: Affichage de fin de partie
        """

        box = self.root.ids.main_box
        box.clear_widgets()

        box2 = BoxLayout()
        box2.add_widget(Label(text= "You won ! Congratz"))
        box2.add_widget(Label(text="Score: "))
        box2.add_widget(Label(text=str(score.get_score)))
        box2.add_widget(Label(text= "Press Q to quit the game"))
        box.add_widget(box2)

        self.refresh()
        key = self.keyboard_list()

        if key != ord('q'):
            return True


if __name__ == "__main__":
    Config.set('graphics', 'width', '1420')
    Config.set('graphics', 'height', '800')
    GameApp("data/map.txt", 16, 11).run()

def GameInit(file, pos_x, pos_y, pacman):
    GameApp(file, pos_x, pos_y, pacman).run()

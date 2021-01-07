from kivy import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition


class GameMode_GUI:
    def __init__(self, file_name, pos1, pos2):
        self.file = file_name
        self.x = pos1
        self.y = pos2
        self.__map_ar = []
        self.__collectibles = 0

    @property
    def map_ar(self):
        return self.__map_ar

    @property
    def collectibles(self):
        return self.__collectibles

    def gen_map_gui(self):
        """
                Auth: Andréas Bombaert
                Last date: November 10 2020 - 17h07
                La fonction traduit le fichier en liste contenant la carte
                PRE (file) : Un fichier contenant une représentation textuelle de la carte de jeu
                    (array) : Un array de coordonnées contenant la position du joueur (PacMan)
                POST (none) : utilise la librairie curses pour afficher la carte dans la console
                RAISES : FileNotFoundError et IOError
            """

        try:
            with open(self.file) as file:
                for line in file:
                    curr = []
                    for x in range(0, len(line) - 1):
                        curr.append(line[x])
                    self.__map_ar.append(curr)
            self.__map_ar[self.x][self.y] = "o"
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def cast_man_gui(self, map_ar):
        pass


class GameScreen(Screen):
    def __init__(self, map_ar, **kwargs):
        self.__map_ar_gui = map_ar
        super(GameApp, self).__init__(**kwargs)

    @property
    def map_ar_gui(self):
        return self.__map_ar_gui

    @map_ar_gui.setter
    def map_ar_gui(self, map_ar_gui):
        self.__map_ar_gui = map_ar_gui

    def refresh(self):
        map = self.__map_ar_gui


class StartScreen(Screen):
    pass


class GameScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        self.current = '_start_screen_'


class PacmanApp(App):
    def build(self):
        return GameScreenManager()


if __name__ == '__main__':
    Config.set('graphics', 'width', '1440')
    Config.set('graphics', 'height', '810')
    PacmanApp().run()

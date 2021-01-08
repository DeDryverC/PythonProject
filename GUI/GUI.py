from kivy import Config
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MenuScreen(Screen):
    pass

class GameModeScreen(Screen):
    pass

class ExitScreen(Screen):
    pass

class MapChoiceScreen(Screen):
    def __init__(self, **kwargs):
        super(MapChoiceScreen, self).__init__(**kwargs)


    def map_2_launch(self):
        ampm = StringProperty("")



class PacManScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(PacManScreenManager, self).__init__(**kwargs)
        self.screen_switch_menu
    def screen_switch_menu(self):
        self.current = '_menu_screen_'

    def screen_switch_gamemode(self):
        self.current = '_gamemode_screen_'

    def screen_switch_exit(self):
        self.current = '_exit_screen_'

class MenuApp(App):
    def build(self):
        return PacManScreenManager()

    def map_1_launch(self):
        self.stop()
        return 1

def launch_menu():
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '400')
    oui = MenuApp().run()
    return oui
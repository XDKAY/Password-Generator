from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.core.clipboard import Clipboard

from Screens import generator_screen
from Screens import settings_screen
from Screens import information_screen

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('main.kv')
Config.set('graphics', 'resizable', '0')
Config.write()


class PasswordGenerator(App):
    def build(self):
        self.icon = 'Icon/App_icon/keys.png'
        return kv

    def returning_name(self, widget, *arsg):
        animate = Animation(
            pos_hint={'top': 1.9, 'center_x': 0.5, 'bottom': 0},
            duration=0.25)
        animate.start(widget)

    def returning_settings_window(self, widget, *args):
        animate = Animation(
            top_hint=0,
            duration=0.25)
        animate.start(widget)

    def animate_name(self, widget, *args):
        animate = Animation(
            pos_hint={'top': 1.43}
            )
        animate.start(widget)

    def animate_settings_menu(self, widget, *args):
        animate = Animation(
            top_hint=0.8)
        animate.start(widget)


if __name__ == '__main__':
    PasswordGenerator().run()
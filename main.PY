from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation


import Screens


class WindowManager(ScreenManager):
    pass


KV = Builder.load_file('main.kv')


class PasswordGenerator(App):
    def build(self):
        self.icon = 'Icon/App_icon/keys.png'
        return KV

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
        animate = Animation(pos_hint={'top': 1.43})
        animate.start(widget)

    def animate_settings_menu(self, widget, *args):
        animate = Animation(top_hint=0.8)
        animate.start(widget)


PasswordGenerator().run()
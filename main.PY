import sqlite3


from kivy.lang import Builder
from kivymd.app import MDApp
from kivy import platform
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar import Snackbar


import Screens


from kv import KV


# KV = Builder.load_file('main.kv')

Builder.load_string(KV)

# 500, 650
class PasswordGenerator(MDApp):
    def build(self):
        self.icon = 'image/App_icon/keys.png'

        self.os_check()

        # Create database passwords and time     
        base = sqlite3.connect('data/db/db.db')
        base.execute('CREATE TABLE IF NOT EXISTS db(password PRIMARY KEY, date_time)')
        base.commit()

        sm = ScreenManager()

        sm.add_widget(Screens.generator_screen.GeneratorScreen(name='password_geniration'))
        sm.add_widget(Screens.settings_screen.SettingsScreen(name='settings'))
        sm.add_widget(Screens.saved_passwords.SavedPasswordsScreen(name='saved_passwords'))
        sm.add_widget(Screens.information_screen.InformationScreen(name='information'))

        return sm

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

    def os_check(self):
        """
        OS type checking function
        return: None
        """

        if platform in ('win', 'linux', 'macosx', 'unknow'):
            Config.set('graphics','resizable', 0)
            Config.write()

    def copy_password(self, password):
        """
        A function that copies the password from the List (Item)
        param: password
        return: class Snacbar()
        """
        
        Clipboard.copy(password)
        return Snackbar(
            text='Password copied successfully!',
            snackbar_x = '20dp',
            snackbar_y = '10dp',
            size_hint_x = 0.9
            ).open()

PasswordGenerator().run()
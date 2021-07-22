from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.storage.dictstore import DictStore


class SettingsScreen(Screen):
	def animate_settings_button(self, widget, *args):
		# animate = Animation(
		# 	size_hint=(0.25, 0.15),
		# 	duration=0.3
		# 	)

		# animate += Animation(
		# 	size_hint=(0.2, 0.1),
		# 	)

		# animate += Animation(
		# 	pos_hint={'center_x': 0.6},
		# 	duration=0.1
		# 	)

		# animate += Animation(
		# 	pos_hint={'center_x': 0.4},
		# 	duration=0.08
		# 	)

		# animate += Animation(
		# 	pos_hint={'center_x': 0.6},
		# 	duration=0.06
		# 	)

		# animate += Animation(
		# 	pos_hint={'center_x': 0.4},
		# 	duration=0.04
		# 	)

		# animate += Animation(
		# 	pos_hint={'center_x': 0.6},
		# 	duration=0.02
		# 	)

		# animate += Animation(
		# 	pos_hint={'center_x': 2},
		# 	duration=0.1
		# 	)

		# animate += Animation(
		# 	pos_hint={'top': 2},
		# 	duration=0.1)

		animate = Animation(
			opacity=0,
			duration=0.5)
		animate.start(widget)

	def returning_settings_button(self, widget, *args):
		animate = Animation(
			pos_hint={'center_x': 0.5, 'top': 0.5},
			opacity=1)
		animate.start(widget)


class SettingsWindow(TabbedPanel):
	config = DictStore('data/config.dat')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.color = (1, 1, 1, 1)
		self.name = 'window_color'
		self.update_window_color()

	# window background color
	def color_change(self, color):
		if color is 'Yellow':
			Window.clearcolor = (247/255, 255/255, 230/255, 1)
			self.color = (0.9686274509803922, 1.0, 0.9019607843137255, 1)

		elif color is 'White':
			Window.clearcolor = (1, 1, 1, 1)
			self.color = (1, 1, 1, 1)

		elif color is 'Blue':
			Window.clearcolor = (204/255, 255/255, 255/255, 1)
			self.color = (0.8, 1.0, 1.0, 1)

	def save_settings(self):
		self.config.put(self.name, background_color=self.color)

	def update_window_color(self):
		Window.clearcolor = (1, 1, 1, 1)
		if self.config.exists(self.name):
			color = self.config[self.name]['background_color']
			Window.clearcolor = color
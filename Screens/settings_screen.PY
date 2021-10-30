from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.storage.dictstore import DictStore


Window.clearcolor = (1, 1, 1, 1)


class SettingsScreen(Screen):
	def animate_settings_button(self, widget, *args):
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
	Config = DictStore('data/config.dat')

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.color = (1, 1, 1, 1)
		self.name = 'window_background_color'
		self.update_window_background_color()

	# window background color 
	def color_change(self, color):
		background_color = {
			'Grey':(69/255, 69/255, 69/255, 1),
			'White':(1, 1, 1, 1),
			'Blue':(0.8, 1.0, 1.0, 1)
		}
		Window.clearcolor = background_color[color]
		self.color = background_color[color]

	def save_settings(self):
		self.Config.put(self.name, background_color=self.color)

	def update_window_background_color(self):
		if self.Config.exists(self.name):
			background_color = self.Config[self.name]['background_color']
			Window.clearcolor = background_color

	def animated_save_setting_button(self, widget, *args):
		animate = Animation(
			width=220,
			duration=0.2)
		animate += Animation(
			width=205,
			duration=0.2)
		animate.start(widget)
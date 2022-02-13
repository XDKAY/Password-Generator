from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.config import Config
from kivy.uix.label import Label
from kivymd.uix.list import ThreeLineAvatarListItem


Window.size = (450, 650)


class SettingsScreen(Screen):
	def animate_settings_button(self, widget, *args):
		animate = Animation(opacity=0, duration=0.5)
		animate.start(widget)

	def returning_settings_button(self, widget, *args):
		animate = Animation(
			pos_hint={'center_x': 0.5, 'top': 0.5},
			opacity=1)
		animate.start(widget)


class SettingsWindow(TabbedPanel):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.color = (1, 1, 1, 1)

	# window background color 
	def background_color_change(self, color):
		background_color = {
			'Grey':(69/255, 69/255, 69/255, 1),
			'White':(1, 1, 1, 1)
		}
		Window.clearcolor = background_color[color]
		self.color = background_color[color]

	# FIX ME
	def save_settings(self):
		pass

	def animated_save_setting_button(self, widget, *args):
		animate = Animation(width=220, duration=0.2)
		animate += Animation(width=205, duration=0.2)
		animate.start(widget)

	def button_animation(self, widget, *args):
		animate = Animation(width=220, duration=0.2)
		animate += Animation(width=205, duration=0.2)
		animate.start(widget)
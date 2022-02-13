import random
import sqlite3
import string

from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


class Open(MDFlatButton):
	pass


class Warning(Snackbar):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.snackbar_x = '20dp'
		self.snackbar_y = '10dp'
		self.size_hint_x = 0.9


class ErrorWindow(MDDialog):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.radius = [20, 7, 20, 7]


class GeneratorScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.upper_case_letters = [i for i in string.ascii_uppercase]
		self.lower_case_letters = [i for i in string.ascii_lowercase]
		self.numbers = [i for i in string.digits]
		self.symbols = [i for i in """!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""]

		Clock.schedule_interval(self.animate_info_button, 1.5)

	def generator(self):
		"""
		Function generate password
		return: None
		"""

		try:
			self.password = []
			self.len_password = int(self.ids.len_password.text)
		except ValueError:
			self.ids.len_password.text = ''
			return ErrorWindow(title='ERROR', text='It should be a number, not a string!').open()
		finally:
			pass

		if self.len_password < 8:
			return ErrorWindow(title='ERROR', text='Password length less than 8').open()

		elif self.len_password > 25:
			return ErrorWindow(title='ERROR', text='Password length more than 25').open()

		# Generate
		else:
			self.items = []
			self.password = ''
			# Upper case letters, numbers, lower case letters and symbols
			if all((self.ids.upper_case.active, self.ids.numbers.active,\
					self.ids.lower_case.active, self.ids.symbol.active)):
				self.items += self.upper_case_letters + self.lower_case_letters + self.symbols + self.numbers
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters, numbers and symbols
			elif all((self.ids.upper_case.active, self.ids.numbers.active, self.ids.symbol.active)):
					self.items += self.upper_case_letters + self.symbols + self.numbers
					for i in range(self.len_password):
						self.password += f'{random.choice(self.items)}'

			# Upper case letters, lower case letters and symbols
			elif all((self.ids.upper_case.active, self.ids.lower_case.active, self.ids.symbol.active)):
				self.items += self.upper_case_letters + self.symbols + self.lower_case_letters
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters?, numbers and lower case letters
			elif all((self.ids.upper_case.active, self.ids.numbers.active, self.ids.lower_case.active)):
				self.items += self.upper_case_letters + self.lower_case_letters + self.numbers
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters and numbers
			elif self.ids.upper_case.active and self.ids.numbers.active:
				self.items += self.upper_case_letters + self.numbers
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters and lower case letters
			elif self.ids.upper_case.active and self.ids.lower_case.active:
				self.items += self.upper_case_letters + self.lower_case_letters
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters and symbols
			elif self.ids.upper_case.active and self.ids.symbol.active:
				self.items += self.upper_case_letters + self.symbols
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Only upper case letters
			elif self.ids.upper_case.active:
				self.items += self.upper_case_letters
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Lower case letters, numbers and symbols
			if all((self.ids.lower_case.active, self.ids.numbers.active, self.ids.symbol.active)):
				self.items += self.lower_case_letters + self.numbers + self.symbols
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Lower case letters and numbers
			elif self.ids.lower_case.active and self.ids.numbers.active:
				self.items += self.lower_case_letters + self.numbers
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Lower case letters and symbols
			elif self.ids.lower_case.active and self.ids.symbol.active:
				self.items += self.lower_case_letters + self.symbols
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Only lower case letters
			elif self.ids.lower_case.active:
				self.items += self.lower_case_letters
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Symbols and numbers
			if self.ids.symbol.active and self.ids.numbers.active:
				self.items += self.numbers + self.symbols
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Only numbers
			elif self.ids.numbers.active:
				self.items += self.numbers
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			# Only symbols
			elif self.ids.symbol.active:
				self.items += self.symbols
				for i in range(self.len_password):
					self.password += f'{random.choice(self.items)}'

			self.password = self.password[:self.len_password]

			if not self.items:
				pass

			else:
				self.ids.password.text = f'{self.password}'

	def clear(self):
		"""
		Function clearing password length and password
		return: None
		"""

		self.ids.len_password.text = ''
		self.ids.password.text = ''

	def copy_password(self):
		"""
		Password copy function
		return: None
		"""
		password = self.ids.password.text
		Clipboard.copy(password)

	def animate_info_button(self, *args):
		widget = self.ids.info_button

		animate = Animation(width=40, height=40, duration=0.6, font_size=50)

		animate += Animation(width=25, height=25, duration=0.6, font_size=30)

		# animate.bind(on_complete=self.reset)
		animate.start(widget)

	def button_animation(self, widget, *args):
		animate = Animation(width=220, duration=0.2)
		animate += Animation(width=205, duration=0.2)
		animate.start(widget)

	def save_password(self):
		"""
		A function that saves the password and the time it was saved
		return: class Warning()
		"""
		password = self.ids.password.text
		date_time = datetime.today()

		if password == '':
			return Warning(
				text="Generate a password to save it!",
				buttons=[Open()]
				).open()

		else:
			try:
				# adds password to the database
				base = sqlite3.connect('data/db/db.db')
				cursor = base.cursor()
				
				cursor.execute('INSERT INTO db VALUES(?, ?)', (password, date_time,))
				base.commit()

			except sqlite3.IntegrityError:
				return ErrorWindow(title='ERROR', text='This password has already been saved.').open()

			finally: pass

			return Warning(text="Password saved successfull!", buttons=[Open()]).open()
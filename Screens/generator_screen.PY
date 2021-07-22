import random

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


class GeneratorScreen(Screen):
	UPPER_CASE_LETTERS = 'A B C D E F G H I K L M N O P Q R S T V X Y Z'
	LOWER_CASE_LETTERS = 'a b c d e f g h i k l m n o p q r s t v x y z'
	NUMBERS = '1 2 3 4 5 6 7 8 9 0'
	SYMBOLS = """! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^ _` { | } ~ """


	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.on_start()

	def generator(self):
		"""Function generate password"""

		self.upper_case_letters = GeneratorScreen.UPPER_CASE_LETTERS.split(' ')
		self.lower_case_letters = GeneratorScreen.LOWER_CASE_LETTERS.split(' ')
		self.numbers = GeneratorScreen.NUMBERS.split(' ')
		self.symbols = GeneratorScreen.SYMBOLS.split(' ')

		self.password = []
		self.len_password = [self.ids.len_password.text]


		if '' in self.len_password:
			l = 0
			self.len_password.clear()
			self.len_password.append(l)

		else:
			for len_ in self.len_password:
				try:
					len_ = int(len_)
					self.len_password.clear()
					self.len_password.append(len_)
				except ValueError:
					popup = Popup(
									title='[color=#339933][font=Dopestyle]ERROR[/font][/color]',
									content=Label(
										text='[font=times][color=#339933]It should be a number, not a string![/color][/font]',
										font_size=16
										),
									size_hint=(None, None),
									size= (250, 250),
							       	auto_dismiss=True,
							       	title_align='center'
				       				)

					self.ids.len_password.text = ''

					return popup.open()
				finally:
					pass


		if self.len_password[0] < 8:
			popup = Popup(
							title='[color=#339933][font=Dopestyle]ERROR[/font][/color]',
							content=Label(
								text='[font=times][color=#339933]Password length less than 8[/color][/font]',
								font_size=18.5
								),
							size_hint=(None, None),
							size= (250, 250),
		       				auto_dismiss=True,
		       				title_align='center'
		       				)
			return popup.open()

		elif self.len_password[0] > 25:
			popup = Popup(
							title='[color=#339933][font=Dopestyle]ERROR[/font][/color]',
							content=Label(
								text='[font=times][color=#339933]Password length more than 25[/color][/font]',
								font_size=18.5
								),
							size_hint=(None, None),
							size= (250, 250),
		       				auto_dismiss=True,
		       				title_align='center'
		       				)
			return popup.open()


		# Generate
		else:
			self.items = []
			self.password = ''

			# ONLY NUMBERS
			if self.ids.only_numbers.active is True:
				self.items += self.numbers
				for i in range(1, self.len_password[0]+1):
					self.password += f'{random.choice(self.items)}'

			# UPPER CASE
			elif self.ids.upper_case.active is True:
				if self.ids.numbers.active is True:
					if self.ids.lower_case.active is True:
						if self.ids.symbol.active is True:

							self.items += self.upper_case_letters
							self.items += self.lower_case_letters
							self.items += self.symbols
							self.items += self.numbers

							for i in range(1, self.len_password[0]+1):
								self.password += f'{random.choice(self.items)}'

						else:
							self.items += self.upper_case_letters
							self.items += self.lower_case_letters
							self.items += self.numbers 

							for i in range(1, self.len_password[0]+1):
								self.password += f'{random.choice(self.items)}'

					elif self.ids.symbol.active is True:
						self.items += self.upper_case_letters
						self.items += self.symbols
						self.items += self.numbers

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

					else:
						self.items += self.upper_case_letters
						self.items += self.numbers

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

				elif self.ids.lower_case.active is True:
					if self.ids.symbol.active is True:
						self.items += self.upper_case_letters
						self.items += self.lower_case_letters
						self.items += self.symbols

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

					else:
						self.items += self.upper_case_letters
						self.items += self.lower_case_letters

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

				elif self.ids.lower_case.active is True:
					if self.ids.numbers.active is True:
						self.items += self.upper_case_letters
						self.items += self.lower_case_letters
						self.items += self.numbers 

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

				elif self.ids.symbol.active is True:
					self.items += self.upper_case_letters
					self.items += self.symbols

					for i in range(1, self.len_password[0]+1):
						self.password += f'{random.choice(self.items)}'

				else:
					self.items += self.upper_case_letters

					for i in range(1, self.len_password[0]+1):
						self.password += f'{random.choice(self.items)}'


			# LOWER CASE
			elif self.ids.lower_case.active is True:
				if self.ids.numbers.active is True:
					if self.ids.symbol.active is True:
						self.items += self.lower_case_letters
						self.items += self.numbers
						self.items += self.symbols

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

					else:
						self.items += self.lower_case_letters
						self.items += self.numbers

						for i in range(1, self.len_password[0]+1):
							self.password += f'{random.choice(self.items)}'

				elif self.ids.symbol.active is True:
					self.items += self.lower_case_letters
					self.items += self.symbols

					for i in range(1, self.len_password[0]+1):
						self.password += f'{random.choice(self.items)}'

				else:
					self.items += self.lower_case_letters
					
					for i in range(1, self.len_password[0]+1):
						self.password += f'{random.choice(self.items)}'


			# NUMBERS
			elif self.ids.numbers.active is True:
				if self.ids.symbol.active is True:
					self.items += self.numbers
					self.items += self.symbols

					for i in range(1, self.len_password[0]+1):
						self.password += f'{random.choice(self.items)}'

				else:
					pass


			if not self.items:
				pass

			else:
				self.ids.password.text = f'{self.password}'

	def clear_text(self):
		self.ids.len_password.text = ''
		self.ids.password.text = ''

	def copy_password(self):
		text = self.ids.password.text
		Clipboard.copy(text)

	def animate_info_button(self, *args):
		widget = self.ids.info_button
		# animate = Animation(
		# 		pos_hint={'y': 0.95},
		# 		duration=0.4)

		# animate += Animation(
		# 		pos_hint={'y': 0.9},
		# 		duration=0.4)
		animate = Animation(
			width=40,
			height=40,
			duration=0.6,
			font_size=50
			)

		animate += Animation(
			width=25,
			height=25,
			duration=0.6,
			font_size=30
			)

		# animate.bind(on_complete=self.reset)
		animate.start(widget)

	# reset animation for a mine of app information 
	# def reset(self, *args):
	# 	widget = args[1]
	# 	widget.width = 25
	# 	widget.height = 25
	# 	widget.duration = 0.6
	# 	widget.font_size = 30

	def on_start(self):
		Clock.schedule_interval(self.animate_info_button, 1.5)

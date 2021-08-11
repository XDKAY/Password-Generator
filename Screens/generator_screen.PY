import random

from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard


class GeneratorScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.start_button_animation()

	def generator(self):
		"""Function generate password"""

		self.upper_case_letters = 'A B C D E F G H I K L M N O P Q R S T V X Y Z'.split(' ')
		self.lower_case_letters = 'a b c d e f g h i k l m n o p q r s t v x y z'.split(' ')
		self.numbers = '1 2 3 4 5 6 7 8 9 0'.split(' ')
		self.symbols = """! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^ _` { | } ~ """.split(' ')

		try:
			self.password = []
			self.len_password = [int(self.ids.len_password.text)]
		except ValueError:
			popup = Popup(title='[color=#339933][font=Dopestyle]ERROR[/font][/color]',
							content=Label(text='[font=times][color=#339933]It should be a number, not a string![/color][/font]',
										  font_size=16),
							size_hint=(None, None),
							size=(250, 250),
							auto_dismiss=True,
						title_align='center')

			self.ids.len_password.text = ''

			return popup.open()
		finally:
			pass

		if self.len_password[0] < 8:
			popup = Popup(title='[color=#339933][font=Dopestyle]ERROR[/font][/color]',
						content=Label(text='[font=times][color=#339933]Password length less than 8[/color][/font]',
									  font_size=18.5),
						size_hint=(None, None),
						size= (250, 250),
		       			auto_dismiss=True,
		       			title_align='center')
			return popup.open()

		elif self.len_password[0] > 25:
			popup = Popup(title='[color=#339933][font=Dopestyle]ERROR[/font][/color]',
							content=Label(text='[font=times][color=#339933]Password length more than 25[/color][/font]',
										  font_size=18.5),
							size_hint=(None, None),
							size= (250, 250),
		       				auto_dismiss=True,
		       				title_align='center')
			return popup.open()


		# Generate
		else:
			self.items = []
			self.password = ''

			# Upper case letters, numbers, lower case letters and symbols
			if all((self.ids.upper_case.active, self.ids.numbers.active, self.ids.lower_case.active, self.ids.symbol.active)):
				self.items += self.upper_case_letters + self.lower_case_letters + self.symbols + self.numbers
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters, numbers and symbols
			elif all((self.ids.upper_case.active, self.ids.numbers.active, self.ids.symbol.active)):
					self.items += self.upper_case_letters + self.symbols + self.numbers
					for i in range(self.len_password[0]):
						self.password += f'{random.choice(self.items)}'

			# Upper case letters, lower case letters and symbols
			elif all((self.ids.upper_case.active, self.ids.lower_case.active, self.ids.symbol.active)):
				self.items += self.upper_case_letters + self.symbols + self.lower_case_letters
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters?, numbers and lower case letters
			elif all((self.ids.upper_case.active, self.ids.numbers.active, self.ids.lower_case.active)):
				self.items += self.upper_case_letters + self.lower_case_letters + self.numbers
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters and numbers
			elif self.ids.upper_case.active and self.ids.numbers.active:
				self.items += self.upper_case_letters + self.numbers
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters and lower case letters
			elif self.ids.upper_case.active and self.ids.lower_case.active:
				self.items += self.upper_case_letters + self.lower_case_letters
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Upper case letters and symbols
			elif self.ids.upper_case.active and self.ids.symbol.active:
				self.items += self.upper_case_letters + self.symbols
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Only upper case letters
			elif self.ids.upper_case.active:
				self.items += self.upper_case_letters
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Lower case letters, numbers and symbols
			if all((self.ids.lower_case.active, self.ids.numbers.active, self.ids.symbol.active)):
				self.items += self.lower_case_letters + self.numbers + self.symbols
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Lower case letters and numbers
			elif self.ids.lower_case.active and self.ids.numbers.active:
				self.items += self.lower_case_letters + self.numbers
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Lower case letters and symbols
			elif self.ids.lower_case.active and self.ids.symbol.active:
				self.items += self.lower_case_letters + self.symbols
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Only lower case letters
			elif self.ids.lower_case.active:
				self.items += self.lower_case_letters
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Symbols and numbers
			if self.ids.symbol.active and self.ids.numbers.active:
				self.items += self.numbers + self.symbols
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Only numbers
			elif self.ids.numbers.active:
				self.items += self.numbers
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			# Only symbols
			elif self.ids.symbol.active:
				self.items += self.symbols
				for i in range(self.len_password[0]):
					self.password += f'{random.choice(self.items)}'

			self.password = self.password[0:self.len_password[0]]

			if not self.items:
				pass

			else:
				self.ids.password.text = f'{self.password}'

	def clear_text(self):
		self.ids.len_password.text = ''
		self.ids.password.text = ''

	def copy_password(self):
		password = self.ids.password.text
		Clipboard.copy(password)

	def animate_info_button(self, *args):
		widget = self.ids.info_button

		animate = Animation(width=40, height=40,
							duration=0.6, font_size=50)

		animate += Animation(width=25, height=25,
							 duration=0.6, font_size=30)

		# animate.bind(on_complete=self.reset)
		animate.start(widget)

	def start_button_animation(self):
		Clock.schedule_interval(self.animate_info_button, 1.5)

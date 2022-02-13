import sqlite3

from kivymd.uix.label import MDLabel
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import Screen
from kivy.properties import *
from kivy.clock import Clock
from kivymd.uix.list import TwoLineAvatarIconListItem


class Item(TwoLineAvatarIconListItem):
	pass


class SavedPasswordsScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.item()

	def item(self, *args):
		base = sqlite3.connect('data/db/db.db')
		cursor = base.cursor()

		passwords = cursor.execute('SELECT password FROM db').fetchall()
		date_time = cursor.execute('SELECT date_time FROM db').fetchall()

		if len(passwords) == 0: self.add_widget(MDLabel(text='What a void...\n Save at least one password', halign='center', font_style='H3'))
		else:
			for first_item in passwords:
				for second_item in date_time:
					continue
				self.ids.list_item.add_widget(
					Item(
						text=f'{first_item[0]}',
						secondary_text=f'{second_item[0]}'
						)
					)
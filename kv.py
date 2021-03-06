KV = """
#:import utils kivy.utils
#:import Clipboard kivy.core.clipboard.Clipboard
#:import Factory kivy.factory.Factory

<Item>:
	id: item
	IconRightWidget:
        icon: "content-copy"
        on_release:
        	app.copy_password(item.text)


<Label>:
	markup: True

<BackgroundColor@Widget>:
	background_color: (0, 0, 0, 0)
	background_normal: ''
	border_radius: 12
	canvas.before:
		Color:
			rgba: (159/255, 223/255, 159/255, 1)
		RoundedRectangle:
			size: self.size
			pos: self.pos
			radius: [30]

<BackgroundLabel@Label+BackgroundColor>:
	background_color: (0, 0, 0, 0)


<SavedPasswordsScreen>:
	name: 'saved_passwords'
	BoxLayout:
		orientation: 'vertical'
		size: root.width, root.height
		Label:
			text:'[font=Dopestyle][color=#339933]Saved Passwords[/color][/font]'
			font_size: 40
			size_hint:(0.1, 0.1)
			pos_hint:{'center_x': 0.5}
		ScrollView:
			MDList:
				id: list_item
		StrokeButton:
			text: '[font=BebasNeueBold][color=#339933]BACK[/color][/font]'
			pos_hint: {'center_x': 0.5, 'top': 0.1}
			# size_hint: (0.2, 0.08)
			size_hint: (None, None)
			width: 80
			height: 50
			font_size: 25
			on_release:
				app.root.current = 'password_geniration'
				root.manager.transition.direction = 'right'


# First Screen
<GeneratorScreen>:
	name:'password_geniration'
	# Information Button
	MDFloatLayout:
		size:root.width, root.height
		InfoButton:
			id: info_button
			text: '[font=SouthernAire_Personal_Use_Only][color=#b3e6b3]?[/color][/font]'
			font_size:30
			size_hint: (None, None)
			width: 25
			height: 25
			# size_hint: (0.08, 0.058)
			pos_hint: {'x': 0.9, 'y': 0.9}
			on_release:
				root.animate_info_button(self)
			on_release:
				app.root.current = 'information'
				root.manager.transition.direction = 'right'

	FloatLayout:
		Button:
			background_color: (1, 1, 1, 0)
			background_normal: ''
			size_hint: None, None
			width: 25
			height: 25
			pos_hint: {'center_x':0.88, 'center_y': 0.7}
			on_press:
				root.copy_password()
			Image:
				source: 'image/copy.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y

	# Programm Name
	BoxLayout:
		orientation:'vertical'
		size:root.width, root.height
		padding: 10
		spacing: 20
		Label:
			text:'[font=Dopestyle][color=#339933]Password Generator[/color][/font]'
			font_size: 40
			size_hint:(0.5, 0.5)
			pos_hint:{'center_x': 0.5}
		# Length and Generated password
		BoxLayout:
			orientation:'vertical'
			size:root.width, root.height
			padding: 10
			spacing: 5
			# Lenght Password
			TextInput:
				id: len_password
				pos_hint: {'center_x':0.5}
				multiline: False
				font_size: 23
				hint_text: 'Password length'
				hint_text_color: (51/255, 153/255, 51/255, 1)
				background_color: (0, 0, 0, 0)
				halign: 'center'
			# Generated Password
			TextInput:
				id: password
				multiline: False
				size_hint_x: None
				width: 330
				pos_hint: {'center_x':0.5}
				font_size: 23
				hint_text: 'Generated password'
				hint_text_color: (51/255, 153/255, 51/255, 1)
				readonly: True
				input_filter: 'int'
				background_color: (0, 0, 0, 0)
				halign: 'center'
				allow_copy: True
				copydata: self.text
		# Genirate Button
		StrokeButton:
			text:'[font=BebasNeueBold][color=#339933]Generate[/color][/font]'
			font_size: 25
			size_hint: (None, None)
			width: 205
			height: 45
			# size_hint:(0.55, 0.4)
			pos_hint:{'center_x': 0.5}
			on_press:
				root.generator()
			on_release:
				root.button_animation(self)
		# Clear Button
		StrokeButton:
			text:'[font=BebasNeueBold][color=#339933]Clear[/color][/font]'
			font_size: 25
			size_hint: (None, None)
			width: 205
			height: 45
			# size_hint:(0.55, 0.4)
			pos_hint:{'center_x': 0.5}
			on_press:
				root.clear()
			on_release:
				root.button_animation(self)
		# Save Password Button
		StrokeButton:
			text:'[font=BebasNeueBold][color=#339933]Save Password[/color][/font]'
			font_size: 25
			size_hint: (None, None)
			width: 205
			height: 45
			# size_hint:(0.55, 0.4)
			pos_hint:{'center_x': 0.5}
			on_release:
				root.button_animation(self)
			on_press:
				root.save_password()
		# Settings Button
		StrokeButton:
			id: settings_button
			text: '[font=BebasNeueBold][color=#339933]Settings[/color][/font]'
			size_hint: (None, None)
			font_size: 25
			width: 205
			height: 45
			pos_hint: {'center_x':0.5}
			on_release:
				app.root.current = 'settings'
				root.manager.transition.direction = 'left'
		# Choosing code generation
		BoxLayout:
			orientation:'vertical'
			size:root.width, root.height
			MDGridLayout:
				cols: 4
				rows: 5
				spacing: 20
				padding: 5
				Label:
					text:'[font=BebasNeueBold][color=#339933]The numbers[/color][/font]'
					font_size: 19
				Switch:
					id: numbers

				Label:
					text:'[font=BebasNeueBold][color=#339933]Upper Case[/color][/font]'
					font_size: 19
				Switch:
					id: upper_case

				Label:
					text:'[font=BebasNeueBold][color=#339933]Lower Case[/color][/font]'
					font_size: 19
				Switch:
					id: lower_case

				Label:
					text:'[font=BebasNeueBold][color=#339933]Symbols[/color][/font]'
					font_size: 19
				Switch:
					id: symbol

<ColorButton@Button>:
	background_color: (0, 0, 0, 0)
	background_normal: ''
	canvas.before:
		Color:
			rgba: (191/255, 191/255, 191/255, 1)
		Line:
			rectangle: (self.x, self.y, self.width, self.height)
			width: 1.7

<InfoButton@Button>:
	background_color: (0, 0, 0, 0)
	background_normal: ''
	canvas.before:
		Color:
			rgba: (57/255, 172/255, 57/255, 1)
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: [10000]

<StrokeButton@Button>:
	background_color: (0, 0, 0, 0)
	background_normal: ''
	border_radius: 21
	canvas.before:
		Color:
			rgba: (159/255, 223/255, 159/255, 1)
		Line:
			rounded_rectangle: (self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
			width: 1.5

<Settings_@BoxLayout>:
	Label:
		text: '[font=Dopestyle][color=#339933]Settings[/color][/font]'
		font_size: 40

<SettingsWindow>:
	do_default_tab: False
	background_color: (179/255, 229/255, 205/255, 0)
	TabbedPanelItem:
		text:'[font=BebasNeueBold][color=#339933]Color[/color][/font]'
		font_size: 23
		background_color: (179/255, 229/255, 205/255, 0)
		FloatLayout:
			size:root.width, root.height
			Label:
				text: '[font=BebasNeueBold][color=#339933]Background Color[/color][/font]'
				font_size: 23
				pos_hint: {'center_x': 0.225, 'y': 0.4}
			#Grey
			ColorButton:
				text:''
				background_color: (69/255, 69/255, 69/255, 1)
				size_hint: (None, None)
				width: 25
				height: 25
				pos_hint: {'center_x': 0.6, 'y': 0.88}
				on_press:
					root.background_color_change('Grey')
			#White
			ColorButton:
				text:''
				background_color: (1, 1, 1, 1)
				width: 25
				size_hint: (None, None)
				height: 25
				pos_hint: {'center_x': 0.5, 'y': 0.88}
				on_press:
					root.background_color_change('White')
			#Save Settings
			StrokeButton:
				text: '[font=BebasNeueBold][color=#339933]Save Settings[/color][/font]'
				size_hint: (None, None)
				font_size: 25
				width: 205
				height: 45
				pos_hint: {'center_x':0.5, 'y':0.328}
				on_press:
					root.save_settings()
				on_release:
					root.animated_save_setting_button(self)

#Second Screen
<SettingsScreen>:
	name:'settings'
	FloatLayout:
		size:root.width, root.height
		# Back Button
		StrokeButton:
			text: '[font=BebasNeueBold][color=#339933]Back[/color][/font]'
			size_hint: (None, None)
			width:68
			height: 47
			# size_hint: (0.15, 0.08)
			font_size: 24
			pos_hint: {'x': 0.03, 'top': 0.97}
			on_release:
				app.root.current = 'password_geniration'
				root.manager.transition.direction = 'right'
				root.returning_settings_button(settings_button)
				app.returning_name(settings_)
				app.returning_settings_window(settings_window)
		# Settings Button
		StrokeButton:
			id: settings_button
			text: '[font=BebasNeueBold][color=#339933]Settings[/color][/font]'
			font_size: 25
			size_hint: (0.2, 0.1)
			pos_hint: {'center_x': 0.5, 'top': 0.5}
			on_release:
				root.animate_settings_button(self)
			on_release:
				app.animate_name(settings_)
			on_release:
				app.animate_settings_menu(settings_window)
		Settings_:
			id: settings_
			size_hint: 1, 1
			pos_hint: {'top': 1.9, 'center_x': 0.5, 'bottom': 0}
		SettingsWindow:
			id: settings_window
			size_hint: 1, 1
			top_hint: 0
			pos_hint: {'top': self.top_hint, 'right': 1}

#Third Screen
<InformationScreen>:
	name: 'information'
	FloatLayout:
		size: root.width, root.height
		Label:
			text: '[font=Dopestyle][color=#339933]About  the program[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.68}
			size_hint: (0.5, 0.5)
			font_size: 40
		Label:
			text: '[font=BebasNeueBold][color=#339933]version 1.0.0[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.56}
			size_hint: (0.5, 0.5)
			font_size: 40
		Label:
			text: '[font=BebasNeueBold][color=#339933]BETA[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.7}
			size_hint: (0.1, 0.1)
			font_size: 25
		Label:
			text: '[font=BebasNeueBold][color=#339933]Description:[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.44}
			size_hint: (0.5, 0.5)
			font_size: 25
		# Description
		Label:
			text: '[font=BebasNeueBold][color=#339933]This password generator generates a random strong password.[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y':0.48}
			size_hint: (0.2, 0.2)
			font_size: 18
		Label:
			text: '[font=BebasNeueBold][color=#339933]Create a strong password consisting of numbers,[/color][/font]'
			pos_hint:{'center_x': 0.5, 'y':0.41}
			size_hint: (0.2, 0.2)
			font_size: 18
		Label:
			text: '[font=BebasNeueBold][color=#339933]lower and upper case letters, symbols.[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.37}
			size_hint: (0.2, 0.2)
			font_size: 17.5
		Label:
			text: '[font=BebasNeueBold][color=#339933]Minimum password length 8,[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.31}
			size_hint: (0.2, 0.2)
			font_size: 18
		Label:
			text: '[font=BebasNeueBold][color=#339933]maximum password length 25.[/color][/font]'
			pos_hint: {'center_x': 0.5, 'y': 0.27}
			size_hint: (0.2, 0.2)
			font_size: 18
		#Return Generator Screen
		StrokeButton:
			text: '[font=BebasNeueBold][color=#339933]OK[/color][/font]'
			pos_hint: {'center_x': 0.5, 'top': 0.1}
			# size_hint: (0.2, 0.08)
			size_hint: (None, None)
			width: 80
			height: 50
			font_size: 25
			on_release:
				app.root.current = 'password_geniration'
				root.manager.transition.direction = 'left'

<Open>:
	text: 'OPEN'
	on_release:
		app.root.current = 'saved_passwords'
"""
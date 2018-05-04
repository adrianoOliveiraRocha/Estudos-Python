# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.2, 0.7, 1)


class MyAnchorLayout(AnchorLayout):
	pass
	

class MyTestApp(App):
	def build(self):
		return MyAnchorLayout()


if __name__ == '__main__':
	MyTestApp().run()



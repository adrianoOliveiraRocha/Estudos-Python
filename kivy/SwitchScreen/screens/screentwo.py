# -*- coding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string(
"""
<ScreenTwo>:
    id: "b2"
    Label:
        text: 'This is my secound screen'
    Button:
        id: call_screen1
        text: 'S2'
        on_press: app.switch_screen(self)
""")

class ScreenTwo(BoxLayout):
    pass

# -*- coding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string(
"""
<ScreenOne>:
    
    orientation: 'vertical'
    Label:
        text: 'This is my first screen'
    Button:
        id: call_screen2
        text: 'B1'
        on_press: app.switch_screen(self)
    Button:
        id: b2
        text: 'B2'
        on_press: app.switch_screen(self)
    
""")

class ScreenOne(BoxLayout):
        
    def callback(self):
        print('A im learning')

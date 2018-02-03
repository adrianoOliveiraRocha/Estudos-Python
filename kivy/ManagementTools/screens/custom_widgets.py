# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Builder.load_string(
"""

<Title@Label>:
    size: self.texture_size
    font_size: '50sp'
    
<MyTextInput@TextInput>:
    multiline: False
    background_color: [0.8, 0.9, 1, 1]
    font_size: '20sp'

<MyButton@Button>:
    font_size: '20sp'

"""

)

class Title(Label):
    pass


class MyTextInput(TextInput):
    pass

class MyButton(Button):
    pass
# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<Title@Label>:
    size: self.texture_size
    font_size: '50sp'
    #text_size: root.width, root.height
    #ellipsis_options: {'color':(1,0.5,0.5,1),'underline':True}
<MyTextInput@TextInput>:
    multiline: False
    
    
<LoginSceen>:
    orientation: 'vertical'
    size_hint: (0.5, 0.5)
    spacing: 30
    pos_hint: {'center_x': .5, 'center_y': .5}
    Title:
        text: '[color=3344ff]Bem Vindo![/color]'
        markup: True
    MyTextInput:
        id: email
        
    MyTextInput:
        id: password
        password: True
        
    BoxLayout:
        spacing: 10
        orientation: 'horizontal'
        Button:
            id: login
            text: 'Login'
        Button:
            id: register
            text: 'Cadastro'
""")

class LoginSceen(BoxLayout):
    pass
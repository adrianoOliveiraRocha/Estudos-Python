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
    background_color: [0.8, 0.9, 1, 1]
    #foreground_color: [1, 0.9, 1, 1]
    font_size: '20sp'
    
    
<LoginSceen>:
    orientation: 'vertical'
    size_hint: (0.5, 0.5)
    spacing: 30
    pos_hint: {'center_x': .5, 'center_y': .5}
    anchor_x: 'center'
    anchor_y: 'center'
    id: inputs
    
    Title:
        #text: '[color=3344ff]Bem Vindo![/color]'
        text: 'Bem Vindo!'
        markup: True

    MyTextInput:
        id: email
        hint_text: 'Seu e-mail aqui'
        
    MyTextInput:
        id: password
        hint_text: 'Sua senha aqui'
        password: True
        
    BoxLayout:
        id: buttons
        spacing: 10
        orientation: 'horizontal'
        Button:
            id: login
            text: 'Login'
        Button:
            id: register
            text: 'Cadastro'
            on_press: app.action_btn('register')
""")

class LoginSceen(BoxLayout):
    pass
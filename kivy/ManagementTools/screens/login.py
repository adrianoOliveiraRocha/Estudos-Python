# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from custom_widgets import Title, MyTextInput, MyButton

Builder.load_string("""
    
<LoginSceen>:
    orientation: 'vertical'
    size_hint: (0.5, 0.5)
    spacing: 30
    pos_hint: {'center_x': .5, 'center_y': .5}
    anchor_x: 'center'
    anchor_y: 'center'
    id: inputs
    
""")

class LoginSceen(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(LoginSceen, self).__init__(*args, **kwargs)
        self.app = kwargs['app']
        self.createInputs()
        self.add_widget(self.createButtons())
    
    def createInputs(self):
        self.add_widget(Title(text='Bem Vindo!'))
        self.add_widget(MyTextInput(
            hint_text='Seu e-mail',
            id='email'
        ))
        self.add_widget(MyTextInput(
            hint_text='Sua senha',
            id='password',
            password=True
        ))
    
    def createButtons(self):
        boxButtons = BoxLayout(id='boxButtons')
        btn_login = MyButton(
            id='btn_login',
            text='Login'
        )
        btn_register = MyButton(
            id='call_form',
            text='Cadastrar-se',
            on_press=self.app.action_btn
        )
        boxButtons.add_widget(btn_login)
        boxButtons.add_widget(btn_register)
        return boxButtons
    
    
        
        

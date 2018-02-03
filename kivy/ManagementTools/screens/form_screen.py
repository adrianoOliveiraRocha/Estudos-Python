# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from custom_widgets import Title, MyTextInput, MyButton

Builder.load_string("""
    
<FormSceen>:
    orientation: 'vertical'
    size_hint: (0.6, 0.6)
    spacing: 30
    pos_hint: {'center_x': .5, 'center_y': .5}
    anchor_x: 'center'
    anchor_y: 'center'
    id: inputs
        
""")

class FormSceen(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(FormSceen, self).__init__(*args, **kwargs)
        self.app = kwargs['app']
        self.createInputs()
        self.add_widget(self.createButtons())
    
    def createInputs(self):
        self.add_widget(Title(text='Cadastro', id='title'))
        # user
        self.user = MyTextInput(hint_text='Nome')       
        self.add_widget(self.user)
        
        # e-mail
        self.email = MyTextInput(hint_text='E-Mail')        
        self.add_widget(self.email)
        
        # password
        self.password = MyTextInput(
                hint_text='Senha',
                password=True
            )
        self.add_widget(self.password)
            
    def createButtons(self):
        boxButtons = BoxLayout(id='boxButtons')
        btn_login = MyButton(
            id='btn_save',
            text='Salvar',
            on_press=self.app.action_btn
        )
        btn_register = MyButton(
            id='btn_clear',
            text='Limpar',
            on_press=self.action_btn
        )
        boxButtons.add_widget(btn_login)
        boxButtons.add_widget(btn_register)
        return boxButtons
    
    def action_btn(self, btn):
        
        if btn.id == 'btn_clear':
            for field in self.children:
                if field.id is not 'title':
                    field.text = ''
                                                    
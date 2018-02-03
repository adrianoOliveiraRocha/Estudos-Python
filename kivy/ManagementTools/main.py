# -*- coding: utf-8 -*-
import kivy
kivy.require("1.9.0")
from kivy.app import App
from screens.login import LoginSceen
from screens.form_screen import FormSceen
from kivy.uix.anchorlayout import AnchorLayout
from models.models import User


class MainScreen(AnchorLayout):
    pass


class MTApp(App):
    def build(self):
        self.mainSreen = MainScreen()
        self.loginScreen = LoginSceen(app=self)
        self.formScreen = FormSceen(app=self)
        self.mainSreen.add_widget(self.loginScreen)
        return self.mainSreen
        
    def action_btn(self, btn):
        """ This methd controll  the actions buttons"""
        if btn.id == 'call_form':
            self.mainSreen.clear_widgets()
            self.mainSreen.add_widget(self.formScreen)
        
        elif btn.id == 'btn_save':
            user = User(self.formScreen.user.text,
                        self.formScreen.email.text,
                        self.formScreen.password.text)
            string = """
                Your name is {}, your email is {} and 
                your password is {}
            """.format(user.user, 
                       user.email, 
                       user.password)
            print(string)


if __name__ == '__main__':
    MTApp().run()

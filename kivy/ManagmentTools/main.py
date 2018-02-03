# -*- coding: utf-8 -*-
import kivy
kivy.require("1.9.0")
from kivy.app import App
from screens.login import LoginSceen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

class MainScreen(AnchorLayout):
    pass

class MTApp(App):
    def build(self):
        self.mainSreen = MainScreen()
        self.mainSreen.add_widget(LoginSceen())
        return self.mainSreen
    
    def action_btn(self, action):
        if action == 'register': self.register()
        
    def register(self):
        print("Let's go")


if __name__ == '__main__':
    MTApp().run()

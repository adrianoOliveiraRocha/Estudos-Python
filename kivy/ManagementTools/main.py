# -*- coding: utf-8 -*-
import kivy
kivy.require("1.9.0")
from kivy.app import App
from screens.login import LoginSceen
#from screens.register import RegisterSceen
from kivy.uix.anchorlayout import AnchorLayout


class MainScreen(AnchorLayout):
    pass

class MTApp(App):
    def build(self):
        self.mainSreen = MainScreen()
        self.mainSreen.add_widget(LoginSceen(app=self))
        return self.mainSreen
        
    def action_btn(self, btn):
        if btn.id == 'call_form':
            print('Show Form')
        
#        self.mainSreen.clear_widgets()
#        self.mainSreen.add_widget(RegisterSceen())


if __name__ == '__main__':
    MTApp().run()

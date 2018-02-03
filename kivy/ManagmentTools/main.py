# -*- coding: utf-8 -*-
import kivy
kivy.require("1.9.0")
from kivy.app import App
from screens.login import LoginSceen


class MTApp(App):
    def build(self):
        return LoginSceen()

if __name__ == '__main__':
    MTApp().run()

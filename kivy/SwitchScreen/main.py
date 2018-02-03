# -*- coding: utf-8 -*-
import kivy
kivy.require("1.9.0")

from kivy.app import App
from screens.screenone import ScreenOne
from screens.screentwo import ScreenTwo
from kivy.uix.boxlayout import BoxLayout

class ManagementTools(App):
    
    def build(self):
        self.boxLayout = BoxLayout()
        self.screenOne = ScreenOne()
        self.screenTwo = ScreenTwo()
        
        self.boxLayout.add_widget(self.screenOne)
                
        return self.boxLayout
    
    def switch_screen(self, instance):
        ids = instance.parent.ids # take id and instance
        for _id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                if _id == 'call_screen2':
                    self.boxLayout.clear_widgets()
                    self.boxLayout.add_widget(self.screenTwo)
                elif _id == 'call_screen1':
                    self.boxLayout.clear_widgets()
                    self.boxLayout.add_widget(self.screenOne)
    
           
        
ManagementTools().run()

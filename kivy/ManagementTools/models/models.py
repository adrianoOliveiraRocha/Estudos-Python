# -*- coding: utf-8 -*-
class User:
    def __init__(self, user=None, email=None, password=None):
        self.user = user
        self.email = email
        self.setPassWord(password)
    
    def setPassWord(self, password):
        if ' ' in password:
            print('Have white space')
        self.password = password

        

#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *

class Application(Frame):
    def __init__(self):
        super().__init__()
        self.master.resizable(False, False)
        self.master.title("English Phrases Application")
        self.style = Style()
        self.style.theme_use("default")
        self.initUI()
    
    def initUI(self):        
        self.frame = Frame(self, relief=RAISED, borderwidth=5)
        self.frame.pack(fill=BOTH, expand=True)
        self.currentPhrase = None
        
        self.insertMenuBar()
        self.insertLabels()
        self.insertBottomButtons()
        
        self.pack(fill=BOTH, expand=True)    
    
    def insertMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        phraseMenu = Menu(menubar)
        phraseMenu.add_command(label="New Phrase", command=self.newPhrase)
        phraseMenu.add_command(label="Give a Phrase", command=self.getOnePhrase)
        phraseMenu.add_command(label="Init", command=self.init)
        phraseMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="Pharase", menu=phraseMenu)
        
    
    def newPhrase(self):
        self.messageLabel.destroy()        
        try:
            if self.insertFrame.winfo_exists() == 1:
                print("Done")                
        except Exception as e:
            self.insertFrame = Frame(self.frame, relief=RAISED, borderwidth=5)
            self.insertFrame.pack(side=TOP, padx=100, pady=200)
            self.insertButton = Button(
                self.insertFrame, text="Insert", command=self.insert)
            self.insertButton.pack(side=LEFT, padx=5, pady=5)
            self.phraseVariable = StringVar()
            self.enterPhrase = Entry(
                self.insertFrame, width=100, textvariable=self.phraseVariable)
            self.enterPhrase.pack(side=RIGHT, padx=50, pady=5)          
        
    def getOnePhrase(self):
        self.messageLabel.destroy() 
        from modules.models import Phrase
        error, phrase = Phrase.getOnePhrase()
        if error is not None:
            try:                
                if self.phraseFrame.winfo_exists() == 1:
                    self.phraseFrame.destroy()
                    self.messageLabel.destroy()
                    self.messageLabel = Label(self.frame, 
                                    text="NO PHRASES", width=200)
                    self.messageLabel.pack(side=TOP, pady=200, padx=400)
                    try: 
                        self.markAsChecked(phrase[0])
                    except Exception as e:
                        print(e)
            except Exception as e:
                self.messageLabel = Label(self.frame, 
                                text="NO PHRASES", width=200)
                self.messageLabel.pack(side=TOP, pady=200, padx=400)
                try: 
                    self.markAsChecked(phrase[0])
                except Exception as e:
                    print(e)
                
        else:
            self.currentPhrase = phrase[1]
            try:
                if self.phraseFrame.winfo_exists() == 1:
                    self.messageLabel.destroy()
                    self.messageLabel = Label(self.phraseFrame, 
                                    text=phrase[1], width=100)
                    self.messageLabel.pack(side=RIGHT, padx=50, pady=5)
                    try: 
                        self.markAsChecked(phrase[0])
                    except Exception as e:
                        print(e)
            except Exception as e:
                self.phraseFrame = Frame(self.frame, relief=RAISED, borderwidth=5)
                self.phraseFrame.pack(side=TOP, padx=100, pady=200)
                self.speakButton = Button(
                    self.phraseFrame, text="Speak!", command=self.speak)
                self.speakButton.pack(side=LEFT, padx=5, pady=5)
                self.messageLabel = Label(self.phraseFrame, 
                                    text = phrase[1], 
                                    width=100)
                self.messageLabel.pack(side=RIGHT, padx=50, pady=5)
                try: 
                    self.markAsChecked(phrase[0])
                except Exception as e:
                    print(e)
                
                
    
    def speak(self):
        print(self.currentPhrase)
        from gtts import gTTS
        import os
        tts = gTTS(self.currentPhrase, lang='en')
        tts.save('audio/phrase.mp3')
        os.system('mpg123 audio/phrase.mp3')
    
    def init(self):
        from modules.models import Phrase
        Phrase.init()        
    
    def markAsChecked(self, id):
        from modules.models import Phrase
        Phrase.markAsChecked(id)
    
    def onExit(self):
        self.quit()
    
    def insert(self):
        from modules.models import Phrase
        p = Phrase(self.phraseVariable.get())
        result = p.save()
        if result == True:
            self.insertFrame.destroy()
            self.messageLabel = Label(self.frame, 
                                  text='Your new phrase was saved')
            self.messageLabel.pack(side=TOP, pady=200)        
        else:
            print('Something wrong!')
           
    
    def insertLabels(self):
        self.messageLabel = Label(self.frame, 
                                  text='ENGLISH PHRASES APPLICATION')
        self.messageLabel.pack(side=TOP, pady=200)
        
    
    def insertBottomButtons(self):
        closeButton = Button(self, text="Close", command=self.onExit)
        closeButton.pack(side=LEFT, padx=5, pady=5)
        

def main():
    root = Tk()
    root.geometry('900x500+200+70')
    app = Application()
    root.mainloop()

def test():
    print('test')
    
if __name__ == '__main__':
    main()

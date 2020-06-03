import curses

class Main:
    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.init_color(0, 0, 0, 0)
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK) 
        curses.curs_set(0)
        self.printCenter("English Phrases Application")
        self.initialMenu()        
        
    def initialMenu(self):
        self.screen.addstr(0, 2, "1 - New Phrase", curses.color_pair(1))
        self.screen.addstr(0, 20, "2 - Give me a Phrase", curses.color_pair(1))
        self.screen.addstr(0, 44, "3 - Exit", curses.color_pair(1))
        opt = self.screen.getch()
        self.analizeOpt(opt)    
    
    def phraseMenu(self):
        self.screen.clear()
        self.screen.refresh()
        self.screen.addstr(0, 2, "1 - Speak", curses.color_pair(1))
        self.screen.addstr(0, 15, "2 - Delete", curses.color_pair(1))
        self.screen.addstr(0, 29, "3 - Come Back", curses.color_pair(1))
        self.screen.addstr(0, 46, "4 - Exit", curses.color_pair(1))
        try:
            self.printCenter(self.currentPhrase)
        except Exception as e:
            pass
        opt = self.screen.getch()
        self.analizeOptPhrase(opt) 
        
    
    def analizeOpt(self, opt):
        if opt == 49:
            self.screen.clear()
            self.screen.refresh()
            self.printCenter('1 choosed')
            self.initialMenu()
        elif opt == 50:
            self.screen.clear()
            self.screen.refresh()
            self.getOnePhrase()
        elif opt == 51:
            self.screen.clear()
            self.screen.refresh()
            self.printCenter('finalyzing...')
            self.exit()
        else:
            self.screen.clear()
            self.screen.refresh()
            self.__init__()
            
    def analizeOptPhrase(self, opt):
        if opt == 49:
            self.screen.clear()
            self.screen.refresh()
            self.phraseMenu()
            print('\nSpeak')
            
        elif opt == 50:
            self.screen.clear()
            self.screen.refresh()
            self.phraseMenu()
            print('\nDelete')
            
        elif opt == 51:
            self.screen.clear()
            self.screen.refresh()
            self.phraseMenu()
            print('\nCome Back')
            
        elif opt == 52:
            self.screen.clear()
            self.screen.refresh()
            self.printCenter('finalyzing...')
            self.exit()
        else:
            self.screen.clear()
            self.screen.refresh()
            self.__init__()
    
    def exit(self):
        curses.napms(1000)
        curses.endwin()
        
        
    def printCenter(self, message):
        num_rows, num_cols = self.screen.getmaxyx()
        middle_row = int(num_rows / 2)
        half_length_of_message = int(len(message) / 2)
        middle_column = int(num_cols / 2)
        x_position = middle_column - half_length_of_message
        self.screen.addstr(middle_row, x_position, message)
        self.screen.refresh()
    
    def getOnePhrase(self):
        from modules.models import Phrase
        error, phrase = Phrase.getOnePhrase()
        if error is not None:
            self.printCenter('No Phrase:')
        else:
            self.currentPhrase = phrase[1]
            Phrase.markAsChecked(phrase[0])            
            self.phraseMenu()
            

if __name__ == '__main__':
    m = Main()
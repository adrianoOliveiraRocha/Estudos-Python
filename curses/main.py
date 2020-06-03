import curses

class Main:
    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        # curses.init_color(0, 0, 0, 0)
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK) 
        curses.curs_set(0)
        self.initialScreen()        
        
    def initialScreen(self):
        self.screen.addstr(0, 0, "Choose a option", curses.color_pair(1))
        self.screen.addstr(1, 2, "1 - New Phrase", curses.color_pair(2))
        self.screen.addstr(2, 2, "2 - Give me a Phrase", curses.color_pair(2))
        self.screen.addstr(3, 2, "3 - Exit", curses.color_pair(2))
        opt = self.screen.getch()
        self.analizeOpt(opt)      
        curses.napms(2000)
        curses.endwin()
    
    def analizeOpt(self, opt):
        if opt == 49:
            self.screen.clear()
            self.screen.refresh()
            print('1 choosed')
        elif opt == 50:
            self.screen.clear()
            self.screen.refresh()
            print('2 choosed')
        elif opt == 51:
            self.screen.clear()
            self.screen.refresh()
            print('3 choosed')
        else:
            self.screen.clear()
            self.screen.refresh()
            print('invalid operation: ', opt)

m = Main()
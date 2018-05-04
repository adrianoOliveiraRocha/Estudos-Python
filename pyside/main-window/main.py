# -*- coding: utf-8 -*-
import sys, time
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, \
    QProgressBar, QLabel, QTextEdit



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)
        self.statusLabel = QLabel('Showing Progress')
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
    
    def createStatusBar(self):
        self.myStatusBar = QStatusBar()
        self.progressBar.setValue(10) # beginning with ten
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)

    def showProgress(self):
        while(self.progressBar.value() < self.progressBar.maximum()):
            self.progressBar.setValue(self.progressBar.value() + 10)
            time.sleep(1)
        self.statusLabel.setText('Ready')

    def setupComponents(self):
        textEdit = QTextEdit()
        self.centralWidget(textEdit)
               
   
if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.createStatusBar()
        mainWindow.show()
        mainWindow.showProgress()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name error: ", sys.exc_info()[1])
    except SystemError:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

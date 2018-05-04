import sys, time
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel,\
 QToolTip, QFont, QPushButton, QMessageBox, QDesktopWidget

class SampleWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Icon Sample")
        self.setGeometry(300, 300, 400, 300)
        QToolTip.setFont(QFont("Decorative", 8, QFont.Bold))
        self.setToolTip('Our Main Window')
        
    def setIcon(self):
        appIcon = QIcon('pyside_logo.png')
        self.setWindowIcon(appIcon)
        
    def setIconModes(self):
        myIcon1 = QIcon('pyside_logo.png')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.setToolTip('Active Icon')
        
        myIcon2 = QIcon('pyside_logo.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.setToolTip('Disabled Icon')
        myLabel2.move(50, 0)
        
        myIcon3 = QIcon('pyside_logo.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.setToolTip('Selected Icon')
        myLabel3.move(100, 0)
    
    def setButton(self):
        myButton = QPushButton('Quit', self)
        myButton.move(50, 240)
        myButton.clicked.connect(self.quitApp)
    
    def quitApp(self):
        userInfo = QMessageBox.question(self, 'Confirmation', 
                                        "This will quit the application. "
                                        "Do you want to cotinue?",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            myApp.quit()
        if userInfo == QMessageBox.No:
            pass
    
    def center(self):
        # get height, width, top, and left points
        qRect = self.frameGeometry()
        # it call the center point of the screen        
        centerPoint = QDesktopWidget().availableGeometry().center()
        # will move the window to the center point of the screen        
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
            
    def setAboutButton(self):
        self.aboutButton = QPushButton("About", self)
        self.aboutButton.move(150, 240)
        self.aboutButton.clicked.connect(self.showAbout)
    
    def showAbout(self):
        QMessageBox.about(self.aboutButton, "About PySide",
                             "PySide is a cross-platform tool "
                             "for generating GUI Programs")
    # aboutQt
    def setAboutQtButton(self):
        self.aboutQtButton = QPushButton("About Qt", self)
        self.aboutQtButton.move(250, 240)
        self.aboutQtButton.clicked.connect(self.showAboutQt)
    
    def showAboutQt(self):
        QMessageBox.aboutQt(self)
    
    
if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.setIconModes()
        myWindow.setButton()
        myWindow.setAboutButton()
        myWindow.setAboutQtButton()
        myWindow.center()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print('Name Error: ', sys.exc_info()[1])
    except SystemExit:
        print('Closing window...')
    except Exception:
        print(sys.exc_info()[1])

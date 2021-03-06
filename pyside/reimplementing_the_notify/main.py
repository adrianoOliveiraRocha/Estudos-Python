# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyApplication(QApplication):
    # Constructor function
    def __init__(self, args):
      super(MyApplication, self).__init__(args)
    # take tha key press
    def notify(self, receiver, event):
        if (event.type() == QEvent.KeyPress):
            QMessageBox.information(None, "Received Key Release EVent", 
                "You Pressed: "+ event.text())
        return super(MyApplication, self).notify(receiver, event)

class MyWidget(QWidget):
    # Constructor function
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Reimplementing Events")
        self.setGeometry(300, 250, 300, 100)

if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = MyApplication(sys.argv)
        myWidget = MyWidget()
        myWidget.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
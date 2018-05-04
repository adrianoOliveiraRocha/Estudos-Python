import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Reimplementing Event")
		self.installEventFilter(self)
		self.setGeometry(300, 250, 300, 100)
		self.myLayout = QVBoxLayout()
		self.myLabel1 = QLabel("Text 1")
		self.myLineEdit1 = QLineEdit()
		self.myLabel2 = QLabel("Text 2")
		self.myLineEdit2 = QLineEdit()
		self.myLabel3 = QLabel("Text 3")
		self.myLineEdit3 = QLineEdit()
		self.myLayout.addWidget(self.myLabel1)
		self.myLayout.addWidget(self.myLineEdit1)
		self.myLayout.addWidget(self.myLabel2)
		self.myLayout.addWidget(self.myLineEdit2)
		self.myLayout.addWidget(self.myLabel3)
		self.myLayout.addWidget(self.myLineEdit3)
		self.setLayout(self.myLayout)

	def event(self, event):
		if event.type() == QEvent.KeyRelease and event.key() == Qt.Key_Tab:
			self.myLineEdit3.setFocus()
			return True
		return QWidget.event(self, event)

	def eventFilter(self, receiver, event):
		if(event.type() == QEvent.MouseButtonPress):
			QMessageBox.information(None, "Filtered Mouse Press Event!!!", 
				"Mouse Press Detected")
			return True
		return super(MyWidget, self).eventFilter(receiver, event)


if __name__ == '__main__':
	try:

		myApp = QApplication(sys.argv)
		myWidget = MyWidget()
		myWidget.show()
		myApp.exec_()
		sys.exit(0)

	except Exception as e:
		raise e
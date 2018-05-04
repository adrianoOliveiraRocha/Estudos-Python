import sys
from PySide.QtGui import *
from PySide.QtCore import *


class MyColorDialog(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		myColor = QColor(0, 0, 0)

		self.setGeometry(300, 300, 400, 300)
		self.setWindowTitle("Color dialog - Example")

		self.myButton = QPushButton('Press to Change Color', self)
		self.myButton.move(10, 50)
		self.myButton.clicked.connect(self.showColorDialog)

		self.myFrame = QFrame(self)
		self.myFrame.setStyleSheet("QWidget { background-color: %s }" 
			% myColor.name())
		self.myFrame.setGeometry(250, 50, 100, 100)

		self.show()

	def showColorDialog(self):

		color = QColorDialog.getColor()

		if color.isValid():
			self.myFrame.setStyleSheet("QWidget { background-color: %s }" 
				% color.name())


if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myCD = MyColorDialog()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e
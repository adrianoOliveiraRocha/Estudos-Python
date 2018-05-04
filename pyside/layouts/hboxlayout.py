import sys
from PySide.QtGui import QHBoxLayout, QApplication, QPushButton, QWidget, \
	QMainWindow	


class MainWindow(QWidget):
	"""docstring for MainWindow"""
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Horizontal Layout")
		self.setGeometry(300, 250, 400, 300)
		self.SetLayout()

	def SetLayout(self):
		horizontalLayout = QHBoxLayout(self)
		hButton1 = QPushButton('Button 1', self)
		hButton2 = QPushButton('Button 2', self)
		hButton3 = QPushButton('Button 3', self)
		hButton4 = QPushButton('Button 4', self)

		horizontalLayout.addWidget(hButton1)
		horizontalLayout.addWidget(hButton2)
		horizontalLayout.addStretch()
		horizontalLayout.addWidget(hButton3)
		horizontalLayout.addWidget(hButton4)

		self.setLayout(horizontalLayout)

if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myWindow = MainWindow()
		myWindow.show()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e

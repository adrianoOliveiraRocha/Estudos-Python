import sys
from PySide.QtGui import QVBoxLayout, QApplication, QPushButton, QWidget, \
	QMainWindow	


class MainWindow(QWidget):
	"""docstring for MainWindow"""
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Horizontal Layout")
		self.setGeometry(300, 250, 400, 300)
		self.SetLayout()

	def SetLayout(self):
		verticalLayout = QVBoxLayout(self)
		vButton1 = QPushButton('Button 1', self)
		vButton2 = QPushButton('Button 2', self)
		vButton3 = QPushButton('Button 3', self)
		vButton4 = QPushButton('Button 4', self)

		verticalLayout.addWidget(vButton1)
		verticalLayout.addWidget(vButton2)
		verticalLayout.addStretch()
		verticalLayout.addWidget(vButton3)
		verticalLayout.addWidget(vButton4)

		self.setLayout(verticalLayout)

if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myWindow = MainWindow()
		myWindow.show()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e

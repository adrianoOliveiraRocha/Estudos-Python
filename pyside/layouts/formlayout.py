import sys
from PySide.QtGui import QApplication, QWidget, QMainWindow, QFormLayout, \
	QPushButton, QLabel, QLineEdit


class MainWindow(QWidget):
	
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("FormLayout")
		self.setGeometry(300, 250, 400, 300)
		self.SetLayout()

	def SetLayout(self):
		formLayout = QFormLayout(self)

		labelUserName = QLabel("Username")
		txtUserName = QLineEdit()
		labelPassword = QLabel("Password")
		txtPassword = QLineEdit()
		
		formLayout.addRow(labelUserName, txtUserName)
		formLayout.addRow(labelPassword, txtPassword)
		
		self.setLayout(formLayout)


if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myWindow = MainWindow()
		myWindow.show()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e
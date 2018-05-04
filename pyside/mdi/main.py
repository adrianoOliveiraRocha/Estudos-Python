import sys
from PySide.QtGui import *
from PySide.QtCore import *


class MyMDIApp(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		workspace = QWorkspace()
		workspace.setWindowTitle("Simple WorkSpace Example")

		for i in range(5):
			textEdit = QTextEdit()
			textEdit.setPlainText("Dummy Text " * 100)
			textEdit.setWindowTitle("Document %i" % i)
			workspace.addWindow(textEdit)

		workspace.tile()
		self.setCentralWidget(workspace)

		self.setGeometry(300, 300, 600, 350)
		self.show()


if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myMDIApp = MyMDIApp()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e

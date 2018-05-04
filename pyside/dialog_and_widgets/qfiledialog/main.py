import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyFileDialog(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QAction(QIcon('img/open.png'), 'Open', self)
		openFile.setShortcut("Ctrl+O")
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)

		self.setGeometry(300, 300, 400, 350)
		self.setWindowTitle("Example - File Dialog")
		self.show()

	def showDialog(self):
		fileName, _ = QFileDialog.getOpenFileName(self, "Open Text Files", 
			"/home/adriano", "Text files(*.txt)")
		contents = open(fileName, 'r')

		with contents:
			data = contents.read()
			self.textEdit.setText(data)


if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myFD = MyFileDialog()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e

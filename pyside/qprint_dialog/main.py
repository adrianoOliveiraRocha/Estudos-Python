import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MyFileDialog(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		printFile = QAction(QIcon("img/print.png"), "Print", self)
		printFile.setShortcut("Ctrl+P")
		printFile.setStatusTip("Prints a File")
		printFile.triggered.connect(self.printDialog)

		menuBar = self.menuBar()
		fileMenu = menuBar.addMenu("&File")
		fileMenu.addAction(printFile)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle("Example - File Dialog")
		self.show()

	def printDialog(self):
		printer = QPrinter()
		dialog = QPrintDialog(printer, self)
		if(dialog.exec_() != QDialog.Accepted):
			return
		self.textEdit.print_(printer)


if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myFD = MyFileDialog()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e
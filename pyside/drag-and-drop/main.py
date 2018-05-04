import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.myListWidget1 = QListWidget()
		self.myListWidget2 = QListWidget()

		self.myListWidget2.setViewMode(QListWidget.IconMode)

		self.myListWidget1.setAcceptDrops(True)
		self.myListWidget1.setDragEnabled(True)

		self.myListWidget2.setAcceptDrops(True)
		self.myListWidget2.setDragEnabled(True)

		self.setGeometry(300, 350, 500, 150)

		self.myLayout = QHBoxLayout()
		self.myLayout.addWidget(self.myListWidget1)
		self.myLayout.addWidget(self.myListWidget2)

		l1 = QListWidgetItem(QIcon('img/blue_bird.png'), "Angry Bird Blue")
		l2 = QListWidgetItem(QIcon('img/red_bird.png'), "Angry Bird Red")
		l3 = QListWidgetItem(QIcon('img/green_bird.png'), "Angry Bird Green")
		l4 = QListWidgetItem(QIcon('img/black_bird.png'), "Angry Bird Black")
		l5 = QListWidgetItem(QIcon('img/white_bird.png'), "Angry Bird White")

		self.myListWidget1.insertItem(1, l1)
		self.myListWidget1.insertItem(2, l2)
		self.myListWidget1.insertItem(3, l3)
		self.myListWidget1.insertItem(4, l4)
		self.myListWidget1.insertItem(5, l5)

		QListWidgetItem(QIcon("img/gray_pig.png"), "Gray Pig", self.myListWidget2)
		QListWidgetItem(QIcon("img/brown_pig.png"), "Brown Pig", self.myListWidget2)
		QListWidgetItem(QIcon("img/green_pig.png"), "Green Pig", self.myListWidget2)

		self.setWindowTitle("Drag and Drop Example")
		self.setLayout(self.myLayout)


if __name__ == '__main__':
	try:
		myApp = QApplication(sys.argv)
		myWidget = MyWidget()
		myWidget.show()
		myApp.exec_()
		sys.exit(0)
	except Exception as e:
		raise e
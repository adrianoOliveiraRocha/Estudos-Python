import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Reimplementing Events")
		self.setGeometry(300, 250, 400, 300)

		self.myLayout = QVBoxLayout()
		self.myLabel = QLabel("Press 'Esc' to close this App")
		self.infoLabel = QLabel()
		self.myLabel.setAlignment(Qt.AlignCenter)
		self.infoLabel.setAlignment(Qt.AlignCenter)
		self.myLayout.addWidget(self.myLabel)
		self.myLayout.addWidget(self.infoLabel)
		self.setLayout(self.myLayout)
	# Function reimplementing Key Press, Mouse Click and Resize Events
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
		
		elif event.key() == Qt.Key_PageDown and \
		event.modifiers() == Qt.ControlModifier:
			print("Ctrl + PageDown key is pressed")

		elif event.key() == Qt.Key_PageUp and \
		event.modifiers() == Qt.ControlModifier:
			print("Ctrl + PageUp key is pressed")

	def mouseDoubleClickEvent(self, event):
		self.close()

	def resizeEvent(self, event):
		self.infoLabel.setText("Window Resized to QSize(%d, %d)" % (event.
			size().width(), event.size().height()))
		

if __name__ == '__main__':
	try:

		myApp = QApplication(sys.argv)
		myWidget = MyWidget()
		myWidget.show()
		myApp.exec_()
		sys.exit(0)

	except Exception as e:
		raise e
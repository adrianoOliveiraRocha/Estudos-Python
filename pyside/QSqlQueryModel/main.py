# -*- coding: utf-8 -*-
import sys 
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSql import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("QTableView within a QMainWindow")
        self.createStatusBar()
        self.initUI()
        self.show()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('mtk.db')
        
        db.open()
        
        model = QSqlQueryModel()
        model.setQuery("select id, en_type, launch from Entry")
        model.setHeaderData(0, Qt.Horizontal, "id")
        model.setHeaderData(1, Qt.Horizontal, "Entry Type")
        model.setHeaderData(2, Qt.Horizontal, "Launch")
        
        tableView = QTableView()
        tableView.setFont(QFont("Courier New", 15))
        tableView.setModel(model)
        tableView.horizontalHeader().setResizeMode(QHeaderView.Stretch)
                
        self.setCentralWidget(tableView)
    
    def createStatusBar(self):
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage("Read Status Bar", 5000)
        self.setStatusBar(self.myStatusBar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    sys.exit(0)
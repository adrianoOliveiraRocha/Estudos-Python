# -*- coding: utf-8 -*-
import sys 
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSql import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 300)
        self.setWindowTitle("QTableView within a QWidget")
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
        
        table_view = QTableView()
        table_view.setFont(QFont("Courier New", 15))
        table_view.setModel(model)
        table_view.horizontalHeader().setResizeMode(QHeaderView.Stretch)
#        self.setCentralWidget(table_view)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    sys.exit(0)
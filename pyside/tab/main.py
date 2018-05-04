# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("Using tabs")
        self.createStatusBar()
        self.initUI()
        self.show()
        
    def initUI(self):
        tabWidget = QTabWidget(self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db/mtk.db')
            
        db.open()
            
        tabWidget.addTab(self.getTableViewCj(), "Diário de Caixa")
        tabWidget.addTab(self.getTableViewUser(), "Usuários Cadastrados")
                
        self.setCentralWidget(tabWidget)

    def getTableViewCj(self):
        model = QSqlQueryModel()
        sql = """
        select strftime('%d/%m/%Y', Launch._date), Launch._value,  Entry.en_type
        from Launch, Entry 
        where Launch.id = Entry.launch
        """
        model.setQuery(sql)
        model.setHeaderData(0, Qt.Horizontal, "Data")
        model.setHeaderData(1, Qt.Horizontal, "Valor R$")
        model.setHeaderData(2, Qt.Horizontal, "Tipo de Entrada")
            
        table_view_cj = QTableView()
        table_view_cj.setFont(QFont("Courier New", 15))
        table_view_cj.setModel(model)
        table_view_cj.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        return table_view_cj
    
    def getTableViewUser(self):
        model = QSqlQueryModel()
        model.setQuery("select id, user, email from User")
        model.setHeaderData(0, Qt.Horizontal, "id")
        model.setHeaderData(1, Qt.Horizontal, "Nome")
        model.setHeaderData(2, Qt.Horizontal, "E-Mail")
            
        table_view_user = QTableView()
        table_view_user.setFont(QFont("Courier New", 15))
        table_view_user.setModel(model)
        table_view_user.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        return table_view_user
    
    def createStatusBar(self):
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage("Read Status Bar", 5000)
        self.setStatusBar(self.myStatusBar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    sys.exit(0)
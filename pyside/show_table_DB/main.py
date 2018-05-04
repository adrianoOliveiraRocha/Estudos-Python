import sys
from PySide import QtGui, QtCore, QtSql


class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        #-------
        #CREATE WIDGETS
        #-------
        frame = QtGui.QFrame()
        
        someLabel = QtGui.QLabel("Some Label")
        someOtherLabel = QtGui.QLabel("Some Other Label")
        self.tableView = QtGui.QTableView()
        
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('mtk.db')
        db.open
        
        tableViewModel = QtSql.QSqlTableModel()
        tableViewModel.setTable("Entry")
        tableViewModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        tableViewModel.select()
        
#        tableViewModel.setQuery("select id, en_type from Entry")
        tableViewModel.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        tableViewModel.setHeaderData(1, QtCore.Qt.Horizontal, "en_type")
        tableViewModel.setHeaderData(1, QtCore.Qt.Horizontal, "launch")
        self.tableView.setModel(tableViewModel)
        
        #--------
        #CREATE LAYOUT
        #--------
        self.setCentralWidget(frame)
        frameLayout = QtGui.QVBoxLayout()
        frameLayout.addWidget(someLabel)
        frameLayout.addWidget(self.tableView)
        frame.setLayout(frameLayout)
        
        self.show()
        
def main():
    
    try:
        app = QtGui.QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        app.exec_()
        sys.exit(0)
    except Exception as e:
        raise e
        
main()        





        
        
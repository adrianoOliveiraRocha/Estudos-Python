# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("Ferramentas de Gestão")
        self.createStatusBar()
        self.initUI()
        self.show()
        self.centralize()
        
    def centralize(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
        
    def initUI(self):
        self.createMenus()   
        self.createActions()
        
        # connect actions to menus
        self.cashJournal.addAction(self.newEntryAction)
        self.cashJournal.addAction(self.showEntryAction)
        self.cashJournal.addAction(self.showExitAction)
        
        tabWidget = QTabWidget(self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db/mtk.db')
            
        db.open()
            
        tabWidget.addTab(self.getTableViewCj(), "Diário de Caixa")
                        
        self.setCentralWidget(tabWidget)
    
    def createMenus(self):
        self.menuBar().setFont(QFont("Helvetica", 15))
        self.cashJournal = self.menuBar().addMenu("&Diário de Caixa")
        self.cashJournal.setFont(QFont("Helvetica", 15))
        self.controlTributes = self.menuBar().addMenu("&Controle de Tributos")
        self.controlTributes.setFont(QFont("Helvetica", 15))        
        self.formatMenu = self.menuBar().addMenu("&Fluxo de Caixa")
        self.formatMenu.setFont(QFont("Helvetica", 15))
        self.helpMenu = self.menuBar().addMenu("&Help")
    
    def createActions(self):
        self.newEntryAction = QAction(QIcon('img/new.png'), 'Nova &Entrada', 
                                self, statusTip="Cria uma nova entrada",
                                triggered=self.newEntry)                                
        self.showEntryAction = QAction('Exibir E&ntradas', 
                                self, statusTip="Exibi somente as entradas")
        self.showExitAction = QAction('Exibir &Saídas', 
                                self, statusTip="Exibi somente as saídas")
    
    def newEntry(self):
        self.formEntry = QWidget()
        self.formEntry.setFont(QFont("Helvetica", 20))
        self.formEntry.setWindowTitle('Nova Entrada')
        self.formEntry.resize(700, 400)
        self.formEntry.move(300, 100)
        
        #create fields        
        self.descriptionEdit = QLineEdit()
        self.descriptionLabel = QLabel('Descrição')
        self.descriptionLabel.setBuddy(self.descriptionEdit)
        
        self.valueEdit = QLineEdit()
        self.valueLabel = QLabel('Valor R$')
        self.valueLabel.setBuddy(self.valueEdit)
        
        self.enTypeLabel = QLabel("Tipo de Entrada")
        self.enTypeCombo = QComboBox(self)
        self.enTypeCombo.addItem("")        
        self.enTypeCombo.addItem("Dinheiro")
        self.enTypeCombo.addItem("Cheque")
        self.enTypeCombo.addItem("Débito")
        self.enTypeCombo.addItem("Crédito")
        self.enTypeCombo.addItem("Transferência")
        self.enTypeCombo.addItem("Depósito")
        
        self.saveEntryButton = QPushButton('Salvar', self)
        self.saveEntryButton.clicked.connect(self.saveEntry)
        self.clearEntryButton = QPushButton('Limpar', self)
        self.clearEntryButton.clicked.connect(self.clearEntry)
        self.closeEntryButton = QPushButton('Fechar', self)
        self.closeEntryButton.clicked.connect(self.closeEntry)
        
        # Main Layout        
        self.gridLayout = QGridLayout()
        
        # Fields Layout
        self.gridLayoutFields = QGridLayout()
        self.gridLayoutFields.addWidget(self.descriptionLabel, 0, 0)
        self.gridLayoutFields.addWidget(self.descriptionEdit, 0, 1)
        self.gridLayoutFields.addWidget(self.valueLabel, 1, 0)
        self.gridLayoutFields.addWidget(self.valueEdit, 1, 1)
        self.gridLayoutFields.addWidget(self.enTypeLabel, 2, 0)
        self.gridLayoutFields.addWidget(self.enTypeCombo, 2, 1)
        # Buttons Layout
        self.gridLayoutButtons = QGridLayout()        
        self.gridLayoutButtons.addWidget(self.saveEntryButton, 3, 0)
        self.gridLayoutButtons.addWidget(self.clearEntryButton, 3, 1)
        self.gridLayoutButtons.addWidget(self.closeEntryButton, 3, 2)
        
        self.gridLayout.addLayout(self.gridLayoutFields, 0, 0)
        self.gridLayout.addLayout(self.gridLayoutButtons, 1, 0)        
        
        self.formEntry.setLayout(self.gridLayout)        
        self.formEntry.show()
    
    def saveEntry(self):
        print("Save Entry Form")
    
    def clearEntry(self):
        self.descriptionEdit.setText("")
        self.valueEdit.setText("")
        self.enTypeCombo.setCurrentIndex(0)
    
    def closeEntry(self):
        self.formEntry.close()

    def getTableViewCj(self):
        model = QSqlQueryModel()
        sql = """
        select strftime('%d/%m/%Y', Launch._date), Launch._value,  Launch.l_type
        from Launch
        """
        model.setQuery(sql)
        model.setHeaderData(0, Qt.Horizontal, "Data")
        model.setHeaderData(1, Qt.Horizontal, "Valor R$")
        model.setHeaderData(2, Qt.Horizontal, "Tipo de Entrada")
            
        table_view_cj = QTableView()
        table_view_cj.setFont(QFont("Helvetica", 20))
        table_view_cj.setModel(model)
        table_view_cj.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        return table_view_cj
    
    def createStatusBar(self):
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage("Read Status Bar", 5000)
        self.setStatusBar(self.myStatusBar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    sys.exit(0)
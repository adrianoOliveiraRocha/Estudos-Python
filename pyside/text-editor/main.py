# -*- coding: utf-8 -*-
import sys, time
from PySide.QtGui import * 
from PySide.QtCore import QRect

# python3.5 and pyside 2.2

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Main Window")
        self.setWindowIcon(QIcon('img/appicon.png'))
        self.setGeometry(0, 0, 900, 600)
        self.SetupComponents()
        self.centralize()
        
    def centralize(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def SetupComponents(self):
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage("Ready", 10000)
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBar()

        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectAllAction)
        self.formatMenu.addAction(self.fontAction)
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutQtAction)
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addAction(self.openAction)
        self.mainToolBar.addAction(self.saveAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.cutAction)
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.undoAction)
        self.mainToolBar.addAction(self.redoAction)

    def newFile(self):
        self.textEdit.setText('')
        self.fileName = None

    def openFile(self):
        self.fileName, self.filterName = QFileDialog.getOpenFileName(self)
        self.textEdit.setText(open(self.fileName).read())

    def saveFile(self):
        if self.fileName == None or self.fileName == '':
            self.fileName, self.filterName = QFileDialog.getSaveFileName(self, filter=self.filters)
        if self.fileName != '':
            file = open(self.fileName, 'w')
            file.write(self.textEdit.toPlainText())
            self.myStatusBar.showMessage("File saved", 2000)

    def exitFile(self):
        self.close()

    def fontChange(self):
        (font, ok) = QFileDialog.getFont(QFont("Helvetica [Cronyx]", 10), self)
        if ok:
            self.textEdit.setCurrentFont(font)

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor", 
            "A simple text editor where you can edit and save files")

    def createActions(self):
        self.newAction = QAction(QIcon('img/new.png'), '&New',
            self, shortcut=QKeySequence.New,
            statusTip="Create a New File") # this is showed in status bar

        self.openAction = QAction(QIcon('img/open.png'), 'O&pen',
            self, shortcut=QKeySequence.Open,
            statusTip="Open a existing file",
            triggered=self.openFile)

        self.saveAction = QAction(QIcon('img/save.png'), '&Save',
            self, shortcut=QKeySequence.Save,
            statusTip="Save the current file to disk",
            triggered=self.saveFile)

        self.exitAction = QAction(QIcon('img/exit.png'), 'E&xit',
            self, shortcut="Ctrl+Q",
            statusTip="Exit the Application",
            triggered=self.exitFile)

        self.cutAction = QAction(QIcon('img/cut.png'), 'C&ut',
            self, shortcut=QKeySequence.Cut,
            statusTip="Cut the current selection to clipboard",
            triggered=self.textEdit.cut)

        self.copyAction = QAction(QIcon('img/copy.png'), 'C&opy',
            self, shortcut=QKeySequence.Copy,
            statusTip="Copy",
            triggered=self.textEdit.copy)

        self.pasteAction = QAction(QIcon('img/paste.png'), '&Paste',
            self, shortcut=QKeySequence.Paste,
            statusTip="Paste the clopboard's content in current location",
            triggered=self.textEdit.paste)

        self.selectAllAction = QAction(QIcon('img/selectAll.png'), 'Select All',
            self, shortcut=QKeySequence.Paste,
            statusTip="Select All",
            triggered=self.textEdit.selectAll)

        self.redoAction = QAction(QIcon('img/redo.png'), 'Redo',
            self, shortcut=QKeySequence.Redo,
            statusTip="Redo previus action",
            triggered=self.textEdit.redo)

        self.undoAction = QAction(QIcon('img/undo.png'), 'Redo',
            self, shortcut=QKeySequence.Undo,
            statusTip="Undo previus action",
            triggered=self.textEdit.undo)

        self.fontAction = QAction('F&ont', self, 
            statusTip="Modify font properties", 
            triggered=self.fontChange)

        self.aboutAction = QAction(QIcon('img/about.png'), 'A&bout',
            self, statusTip="Display info about text editor",
            triggered=self.aboutHelp)

        self.aboutQtAction = QAction("About &Qt", self,
            statusTip="Show the Qt library's About box",
            triggered=qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.formatMenu = self.menuBar().addMenu("F&ormat")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def createToolBar(self):
        self.mainToolBar = self.addToolBar('Main')
               

if __name__ == '__main__':
    try:
        QApplication.setStyle('plastique')
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except Exception as e:
        raise e

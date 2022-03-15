#   Item List - Lists anything using a name and a comment section.
#   Copyright (C) 2021  Kerem Biçen

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt5 import QtCore, QtWidgets
from DialogAdd import Ui_Dialog as FormAdd
from DialogEdit import Ui_Dialog as FormEdit
from DialogPreferences import Ui_Dialog as FormPreferences
from GetLanguage import Language
from os import path
import json

# Setting language variable
language = Language.Get()

# User interface code generated by PyQt5 UI code generator
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listBox = QtWidgets.QTableWidget(self.centralwidget)
        self.listBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listBox.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listBox.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listBox.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listBox.setColumnCount(2)
        self.listBox.setObjectName("listBox")
        self.listBox.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listBox.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listBox.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.listBox)
        self.searchBox = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBox.setObjectName("searchBox")
        self.verticalLayout.addWidget(self.searchBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.contextActionAdd = QtWidgets.QAction(MainWindow)
        self.contextActionAdd.setObjectName("contextActionAdd")
        self.contextActionEdit = QtWidgets.QAction(MainWindow)
        self.contextActionEdit.setObjectName("contextActionEdit")
        self.contextActionRemove = QtWidgets.QAction(MainWindow)
        self.contextActionRemove.setObjectName("contextActionRemove")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionAdd)
        self.menuEdit.addAction(self.actionEdit)
        self.menuEdit.addAction(self.actionRemove)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.listBox.addAction(self.contextActionAdd)
        self.listBox.addAction(self.contextActionEdit)
        self.listBox.addAction(self.contextActionRemove)
        self.listBox.setColumnWidth(0, 171)
        self.listBox.setColumnWidth(1, 685)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event handling
        self.searchBox.textChanged.connect(self.textChange)
        self.actionAdd.triggered.connect(self.open_DialogAdd)
        self.actionEdit.triggered.connect(self.open_DialogEdit)
        self.actionRemove.triggered.connect(self.removeItem)
        self.actionPreferences.triggered.connect(self.open_DialogPreferences)
        self.actionQuit.triggered.connect(lambda: MainWindow.close())
        self.contextActionAdd.triggered.connect(self.open_DialogAdd)
        self.contextActionEdit.triggered.connect(self.open_DialogEdit)
        self.contextActionRemove.triggered.connect(self.removeItem)

    def retranslateUi(self, MainWindow):
        global language
        language = Language.Get()
        MainWindow.setWindowTitle("Item List")
        self.listBox.setSortingEnabled(True)

        # language.get("key") method for applying language
        item = self.listBox.horizontalHeaderItem(0)
        item.setText(language.get("columnItem"))
        item = self.listBox.horizontalHeaderItem(1)
        item.setText(language.get("columnComment"))
        self.menuFile.setTitle(language.get("menuFile"))
        self.menuEdit.setTitle(language.get("menuEdit"))
        self.menuSettings.setTitle(language.get("menuSettings"))
        self.menuHelp.setTitle(language.get("menuHelp"))
        self.actionImport.setText(language.get("actionImport"))
        self.actionExport.setText(language.get("actionExport"))
        self.actionQuit.setText(language.get("actionQuit"))
        self.actionAdd.setText(language.get("actionAdd"))
        self.actionEdit.setText(language.get("actionEdit"))
        self.actionRemove.setText(language.get("actionRemove"))
        self.actionPreferences.setText(language.get("actionPreferences"))
        self.actionAbout.setText(language.get("actionAbout"))
        self.contextActionAdd.setText(language.get("actionAdd"))
        self.contextActionEdit.setText(language.get("actionEdit"))
        self.contextActionRemove.setText(language.get("actionRemove"))
    
    # Event that triggers when searchBox's text changes
    def textChange(self):
        # Create a new list of items that starts with the word in the searchBox
        resultlist = [item for item in self.returnItemList() if item["item"].lower().startswith(self.searchBox.text().lower())]

        # Clear items in listBox
        self.listBox.setRowCount(0)
            
        # Add searched items in listBox
        for item in resultlist:
            self.listBox.insertRow(self.listBox.rowCount()) 
            itemItem = QtWidgets.QTableWidgetItem(item["item"])
            itemComment = QtWidgets.QTableWidgetItem(item["comment"])
            self.listBox.setSortingEnabled(False)
            self.listBox.setItem(self.listBox.rowCount() - 1, 0, itemItem)
            self.listBox.setItem(self.listBox.rowCount() - 1, 1, itemComment)
            self.listBox.setSortingEnabled(True)
            
    # Show DialogAdd then clear and update contents of the listBox
    def open_DialogAdd(self):
        DialogAdd = QtWidgets.QDialog()
        DialogAdd.ui = FormAdd()
        DialogAdd.ui.setupUi(DialogAdd)
        DialogAdd.exec_()
        DialogAdd.show()
        self.updateItemList()
    
    # Pass selected item and show DialogEdit then clear and update contents of the listBox
    def open_DialogEdit(self):
        r = self.listBox.currentRow()
        if r == -1:
            msgEmpty = QtWidgets.QMessageBox()
            msgEmpty.setWindowTitle(language.get("actionEdit"))
            msgEmpty.setText(language.get("selectSomethingToEdit"))
            msgEmpty.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msgEmpty.exec_()
            return
        DialogEdit = QtWidgets.QDialog()
        DialogEdit.ui = FormEdit(self.listBox.item(r, 0).text(), self.listBox.item(r, 1).text())
        DialogEdit.ui.setupUi(DialogEdit)
        DialogEdit.exec_()
        DialogEdit.show()
        self.updateItemList()
    
    def open_DialogPreferences(self):
        DialogPreferences = QtWidgets.QDialog()
        DialogPreferences.ui = FormPreferences()
        DialogPreferences.ui.setupUi(DialogPreferences)
        DialogPreferences.exec_()
        DialogPreferences.show()
        self.retranslateUi(MainWindow)

    def removeItem(self):
        r = self.listBox.currentRow()
        if r == -1:
            msgEmpty = QtWidgets.QMessageBox()
            msgEmpty.setWindowTitle(language.get("actionRemove"))
            msgEmpty.setText(language.get("selectSomethingToRemove"))
            msgEmpty.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msgEmpty.exec_()
            return
        
        if not path.isfile("db.json"):
            dbfile = open("db.json", "w", encoding="UTF-8")
            dbfile.close()

        with open("db.json", "r", encoding="UTF-8") as dbfile:
            try: jsondb = json.load(dbfile)
            except: jsondb = []
        
        for i in range(len(jsondb)):
            if jsondb[i]["item"] == self.listBox.item(r, 0).text():
                del jsondb[i]
                break
        
        with open("db.json", "w", encoding="UTF-8") as dbfile: json.dump(jsondb, dbfile)
            
        self.updateItemList()
    
    def updateItemList(self):
        if not path.isfile("db.json"):
            dbfile = open("db.json", "w", encoding="UTF-8")
            dbfile.close()

        with open("db.json", "r", encoding="UTF-8") as dbfile:
            try: jsondb = json.load(dbfile)
            except: jsondb = []
        
        if not len(jsondb) < 1:
            # Clear items in listBox
            self.listBox.setRowCount(0)

            # Add items to listBox
            for item in jsondb:
                self.listBox.insertRow(self.listBox.rowCount()) 
                itemItem = QtWidgets.QTableWidgetItem(item["item"])
                itemComment = QtWidgets.QTableWidgetItem(item["comment"])
                self.listBox.setSortingEnabled(False)
                self.listBox.setItem(self.listBox.rowCount() - 1, 0, itemItem)
                self.listBox.setItem(self.listBox.rowCount() - 1, 1, itemComment)
                self.listBox.setSortingEnabled(True)
        else: self.listBox.setRowCount(0)

    def returnItemList(self):
        if not path.isfile("db.json"):
            dbfile = open("db.json", "w", encoding="UTF-8")
            dbfile.close()

        with open("db.json", "r", encoding="UTF-8") as dbfile:
            try: jsondb = json.load(dbfile)
            except: jsondb = []
        return jsondb

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.updateItemList()
    MainWindow.show()
    sys.exit(app.exec_())
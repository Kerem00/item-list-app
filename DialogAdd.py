#   This file is part of Item List.

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
from GetLanguage import Language
from os import path
import json

# Setting language variable
language = Language.Get()

# User interface code generated by PyQt5 UI code generator
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 111)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.textItem = QtWidgets.QLineEdit(Dialog)
        self.textItem.setObjectName("textItem")
        self.gridLayout.addWidget(self.textItem, 0, 1, 1, 1)
        self.textComment = QtWidgets.QLineEdit(Dialog)
        self.textComment.setObjectName("textComment")
        self.gridLayout.addWidget(self.textComment, 1, 1, 1, 1)
        self.labelItem = QtWidgets.QLabel(Dialog)
        self.labelItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelItem.setObjectName("labelItem")
        self.gridLayout.addWidget(self.labelItem, 0, 0, 1, 1)
        self.labelComment = QtWidgets.QLabel(Dialog)
        self.labelComment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelComment.setObjectName("labelComment")
        self.gridLayout.addWidget(self.labelComment, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.clicked.connect(Dialog.accept)
        self.buttonBox.accepted.connect(self.addItem)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global language
        language = Language.Get()
        Dialog.setWindowTitle(language.get("actionAdd"))
        self.labelItem.setText(language.get("columnItem") + ":")
        self.labelComment.setText(language.get("columnComment") + ":")

    def addItem(self):
        if not self.textItem.text().strip() or not self.textComment.text().strip():
            msgEmpty = QtWidgets.QMessageBox()
            msgEmpty.setWindowTitle(language.get("actionAdd"))
            msgEmpty.setText(language.get("emptyText"))
            msgEmpty.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msgEmpty.exec_()
        else:
            if not path.isfile("db.json"):
                dbfile = open("db.json", "w", encoding="UTF-8")
                dbfile.close()

            with open("db.json", "r", encoding="UTF-8") as dbfile:
                try: jsondb = json.load(dbfile)
                except: jsondb = []

            for item in jsondb:
                if item["item"].lower() == self.textItem.text().lower():
                    msgAlready = QtWidgets.QMessageBox()
                    msgAlready.setWindowTitle(language.get("actionAdd"))
                    msgAlready.setText(language.get("alreadyInDatabase"))
                    msgAlready.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msgAlready.exec_()
                    return

            item = {
                "item": self.textItem.text(),
                "comment": self.textComment.text()
            }

            jsondb.append(item)

            with open("db.json", "w", encoding="UTF-8") as dbfile: json.dump(jsondb, dbfile)
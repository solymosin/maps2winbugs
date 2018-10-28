# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nbEditor_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nbEditor_dialog(object):
    def setupUi(self, nbEditor_dialog):
        nbEditor_dialog.setObjectName("nbEditor_dialog")
        nbEditor_dialog.resize(557, 537)
        self.gridLayout = QtWidgets.QGridLayout(nbEditor_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(nbEditor_dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(nbEditor_dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(181, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.tableView = QtWidgets.QTableView(nbEditor_dialog)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 3)
        self.pushCancel = QtWidgets.QPushButton(nbEditor_dialog)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName("pushCancel")
        self.gridLayout.addWidget(self.pushCancel, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(nbEditor_dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)
        self.pushOK = QtWidgets.QPushButton(nbEditor_dialog)
        self.pushOK.setAutoDefault(False)
        self.pushOK.setDefault(True)
        self.pushOK.setObjectName("pushOK")
        self.gridLayout.addWidget(self.pushOK, 2, 2, 1, 1)

        self.retranslateUi(nbEditor_dialog)
        QtCore.QMetaObject.connectSlotsByName(nbEditor_dialog)

    def retranslateUi(self, nbEditor_dialog):
        _translate = QtCore.QCoreApplication.translate
        nbEditor_dialog.setWindowTitle(_translate("nbEditor_dialog", "Neighbouring list"))
        self.label.setText(_translate("nbEditor_dialog", "Method:"))
        self.pushCancel.setText(_translate("nbEditor_dialog", "Close"))
        self.pushOK.setText(_translate("nbEditor_dialog", "Convert to BUGS"))


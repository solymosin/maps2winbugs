# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exp2BUGS_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exp2BUGS_dialog(object):
    def setupUi(self, exp2BUGS_dialog):
        exp2BUGS_dialog.setObjectName("exp2BUGS_dialog")
        exp2BUGS_dialog.resize(422, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        exp2BUGS_dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(exp2BUGS_dialog)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(exp2BUGS_dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(exp2BUGS_dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(201, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(exp2BUGS_dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(exp2BUGS_dialog)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(exp2BUGS_dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(exp2BUGS_dialog)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.retranslateUi(exp2BUGS_dialog)
        QtCore.QMetaObject.connectSlotsByName(exp2BUGS_dialog)

    def retranslateUi(self, exp2BUGS_dialog):
        _translate = QtCore.QCoreApplication.translate
        exp2BUGS_dialog.setWindowTitle(_translate("exp2BUGS_dialog", "Editor"))
        self.label.setText(_translate("exp2BUGS_dialog", "GeoBUGS importable format:"))
        self.pushButton_2.setText(_translate("exp2BUGS_dialog", "Close"))
        self.pushButton.setText(_translate("exp2BUGS_dialog", "Save"))


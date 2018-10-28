# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editor_dialog(object):
    def setupUi(self, editor_dialog):
        editor_dialog.setObjectName("editor_dialog")
        editor_dialog.resize(533, 430)
        self.gridLayout = QtWidgets.QGridLayout(editor_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(editor_dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushCancel = QtWidgets.QPushButton(editor_dialog)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName("pushCancel")
        self.horizontalLayout.addWidget(self.pushCancel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushSave = QtWidgets.QPushButton(editor_dialog)
        self.pushSave.setAutoDefault(False)
        self.pushSave.setDefault(True)
        self.pushSave.setObjectName("pushSave")
        self.horizontalLayout.addWidget(self.pushSave)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(editor_dialog)
        QtCore.QMetaObject.connectSlotsByName(editor_dialog)

    def retranslateUi(self, editor_dialog):
        _translate = QtCore.QCoreApplication.translate
        editor_dialog.setWindowTitle(_translate("editor_dialog", "Dialog"))
        self.pushCancel.setText(_translate("editor_dialog", "Close"))
        self.pushSave.setText(_translate("editor_dialog", "Save"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_dialog_base.ui'
#
# Created: Mon Aug  3 22:01:32 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_editor_dialog(object):
    def setupUi(self, editor_dialog):
        editor_dialog.setObjectName(_fromUtf8("editor_dialog"))
        editor_dialog.resize(533, 430)
        self.gridLayout = QtGui.QGridLayout(editor_dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(editor_dialog)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushCancel = QtGui.QPushButton(editor_dialog)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName(_fromUtf8("pushCancel"))
        self.horizontalLayout.addWidget(self.pushCancel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushSave = QtGui.QPushButton(editor_dialog)
        self.pushSave.setAutoDefault(False)
        self.pushSave.setDefault(True)
        self.pushSave.setObjectName(_fromUtf8("pushSave"))
        self.horizontalLayout.addWidget(self.pushSave)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(editor_dialog)
        QtCore.QMetaObject.connectSlotsByName(editor_dialog)

    def retranslateUi(self, editor_dialog):
        editor_dialog.setWindowTitle(QtGui.QApplication.translate("editor_dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushCancel.setText(QtGui.QApplication.translate("editor_dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSave.setText(QtGui.QApplication.translate("editor_dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))


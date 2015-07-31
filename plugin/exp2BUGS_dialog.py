# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exp2BUGS_dialog_base.ui'
#
# Created: Fri Jul 31 18:59:57 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_exp2BUGS_dialog(object):
    def setupUi(self, exp2BUGS_dialog):
        exp2BUGS_dialog.setObjectName(_fromUtf8("exp2BUGS_dialog"))
        exp2BUGS_dialog.resize(422, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        exp2BUGS_dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(exp2BUGS_dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(exp2BUGS_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(exp2BUGS_dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(201, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(exp2BUGS_dialog)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(exp2BUGS_dialog)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(exp2BUGS_dialog)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.retranslateUi(exp2BUGS_dialog)
        QtCore.QMetaObject.connectSlotsByName(exp2BUGS_dialog)

    def retranslateUi(self, exp2BUGS_dialog):
        exp2BUGS_dialog.setWindowTitle(QtGui.QApplication.translate("exp2BUGS_dialog", "Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("exp2BUGS_dialog", "GeoBUGS importable format:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("exp2BUGS_dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("exp2BUGS_dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))


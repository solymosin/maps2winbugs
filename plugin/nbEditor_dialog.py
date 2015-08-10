# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nbEditor_dialog_base.ui'
#
# Created: Sun Aug  9 04:16:17 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_nbEditor_dialog(object):
    def setupUi(self, nbEditor_dialog):
        nbEditor_dialog.setObjectName(_fromUtf8("nbEditor_dialog"))
        nbEditor_dialog.resize(557, 537)
        self.gridLayout = QtGui.QGridLayout(nbEditor_dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(nbEditor_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(nbEditor_dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(181, 23))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(119, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.tableView = QtGui.QTableView(nbEditor_dialog)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 3)
        self.pushCancel = QtGui.QPushButton(nbEditor_dialog)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName(_fromUtf8("pushCancel"))
        self.gridLayout.addWidget(self.pushCancel, 2, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(nbEditor_dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)
        self.pushOK = QtGui.QPushButton(nbEditor_dialog)
        self.pushOK.setAutoDefault(False)
        self.pushOK.setDefault(True)
        self.pushOK.setObjectName(_fromUtf8("pushOK"))
        self.gridLayout.addWidget(self.pushOK, 2, 2, 1, 1)

        self.retranslateUi(nbEditor_dialog)
        QtCore.QMetaObject.connectSlotsByName(nbEditor_dialog)

    def retranslateUi(self, nbEditor_dialog):
        nbEditor_dialog.setWindowTitle(QtGui.QApplication.translate("nbEditor_dialog", "Neighbouring list", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("nbEditor_dialog", "Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushCancel.setText(QtGui.QApplication.translate("nbEditor_dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOK.setText(QtGui.QApplication.translate("nbEditor_dialog", "Convert to BUGS", None, QtGui.QApplication.UnicodeUTF8))


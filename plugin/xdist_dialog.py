# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xdist_dialog_base.ui'
#
# Created: Mon Aug  3 22:42:32 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_xDist(object):
    def setupUi(self, xDist):
        xDist.setObjectName(_fromUtf8("xDist"))
        xDist.resize(232, 84)
        self.gridLayout = QtGui.QGridLayout(xDist)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(xDist)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(xDist)
        self.lineEdit.setMinimumSize(QtCore.QSize(141, 26))
        self.lineEdit.setMaximumSize(QtCore.QSize(141, 26))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushCancel = QtGui.QPushButton(xDist)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName(_fromUtf8("pushCancel"))
        self.horizontalLayout_2.addWidget(self.pushCancel)
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushOK = QtGui.QPushButton(xDist)
        self.pushOK.setAutoDefault(False)
        self.pushOK.setDefault(True)
        self.pushOK.setObjectName(_fromUtf8("pushOK"))
        self.horizontalLayout_2.addWidget(self.pushOK)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(xDist)
        QtCore.QMetaObject.connectSlotsByName(xDist)

    def retranslateUi(self, xDist):
        xDist.setWindowTitle(QtGui.QApplication.translate("xDist", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("xDist", "Distance:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushCancel.setText(QtGui.QApplication.translate("xDist", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOK.setText(QtGui.QApplication.translate("xDist", "OK", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splusimport_dialog_base.ui'
#
# Created: Wed Aug 12 19:49:11 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SPlusImport(object):
    def setupUi(self, SPlusImport):
        SPlusImport.setObjectName(_fromUtf8("SPlusImport"))
        SPlusImport.resize(584, 109)
        self.gridLayout_2 = QtGui.QGridLayout(SPlusImport)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SPlusImport)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(SPlusImport)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.toolButton = QtGui.QToolButton(SPlusImport)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(SPlusImport)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(SPlusImport)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.toolButton_3 = QtGui.QToolButton(SPlusImport)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.gridLayout.addWidget(self.toolButton_3, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SPlusImport)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SPlusImport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SPlusImport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SPlusImport.reject)
        QtCore.QMetaObject.connectSlotsByName(SPlusImport)

    def retranslateUi(self, SPlusImport):
        SPlusImport.setWindowTitle(QtGui.QApplication.translate("SPlusImport", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SPlusImport", "S-Plus file:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("SPlusImport", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SPlusImport", "Output shape  file:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("SPlusImport", "...", None, QtGui.QApplication.UnicodeUTF8))


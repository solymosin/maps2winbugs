# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splusimport_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SPlusImport(object):
    def setupUi(self, SPlusImport):
        SPlusImport.setObjectName("SPlusImport")
        SPlusImport.resize(584, 109)
        self.gridLayout_2 = QtWidgets.QGridLayout(SPlusImport)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SPlusImport)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(SPlusImport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(SPlusImport)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(SPlusImport)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(SPlusImport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 23))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(SPlusImport)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SPlusImport)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SPlusImport)
        self.buttonBox.accepted.connect(SPlusImport.accept)
        self.buttonBox.rejected.connect(SPlusImport.reject)
        QtCore.QMetaObject.connectSlotsByName(SPlusImport)

    def retranslateUi(self, SPlusImport):
        _translate = QtCore.QCoreApplication.translate
        SPlusImport.setWindowTitle(_translate("SPlusImport", "Dialog"))
        self.label.setText(_translate("SPlusImport", "S-Plus file:"))
        self.toolButton.setText(_translate("SPlusImport", "..."))
        self.label_3.setText(_translate("SPlusImport", "Output shape  file:"))
        self.toolButton_3.setText(_translate("SPlusImport", "..."))


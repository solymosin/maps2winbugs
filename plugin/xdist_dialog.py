# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xdist_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_xDist(object):
    def setupUi(self, xDist):
        xDist.setObjectName("xDist")
        xDist.resize(232, 84)
        self.gridLayout = QtWidgets.QGridLayout(xDist)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(xDist)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(xDist)
        self.lineEdit.setMinimumSize(QtCore.QSize(141, 26))
        self.lineEdit.setMaximumSize(QtCore.QSize(141, 26))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushCancel = QtWidgets.QPushButton(xDist)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName("pushCancel")
        self.horizontalLayout_2.addWidget(self.pushCancel)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushOK = QtWidgets.QPushButton(xDist)
        self.pushOK.setAutoDefault(False)
        self.pushOK.setDefault(True)
        self.pushOK.setObjectName("pushOK")
        self.horizontalLayout_2.addWidget(self.pushOK)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(xDist)
        QtCore.QMetaObject.connectSlotsByName(xDist)

    def retranslateUi(self, xDist):
        _translate = QtCore.QCoreApplication.translate
        xDist.setWindowTitle(_translate("xDist", "Dialog"))
        self.label.setText(_translate("xDist", "Distance:"))
        self.pushCancel.setText(_translate("xDist", "Cancel"))
        self.pushOK.setText(_translate("xDist", "OK"))


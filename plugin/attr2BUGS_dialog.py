# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attr2BUGS_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_attr2BUGS(object):
    def setupUi(self, attr2BUGS):
        attr2BUGS.setObjectName("attr2BUGS")
        attr2BUGS.resize(527, 409)
        attr2BUGS.setAcceptDrops(False)
        attr2BUGS.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(attr2BUGS)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(attr2BUGS)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(attr2BUGS)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.listView = QtWidgets.QListView(attr2BUGS)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(attr2BUGS)
        self.pushButton.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(attr2BUGS)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 3, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(attr2BUGS)
        self.pushButton_2.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(324, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(attr2BUGS)
        self.pushButton_3.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)

        self.retranslateUi(attr2BUGS)
        QtCore.QMetaObject.connectSlotsByName(attr2BUGS)

    def retranslateUi(self, attr2BUGS):
        _translate = QtCore.QCoreApplication.translate
        attr2BUGS.setWindowTitle(_translate("attr2BUGS", "Dialog"))
        self.label.setText(_translate("attr2BUGS", "Fields:"))
        self.label_2.setText(_translate("attr2BUGS", "BUGS script:"))
        self.pushButton.setText(_translate("attr2BUGS", ">>"))
        self.pushButton_2.setText(_translate("attr2BUGS", "Close"))
        self.pushButton_3.setText(_translate("attr2BUGS", "Save"))


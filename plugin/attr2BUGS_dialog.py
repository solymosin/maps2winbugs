# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attr2BUGS_dialog_base.ui'
#
# Created: Tue Aug 11 07:55:05 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_attr2BUGS(object):
    def setupUi(self, attr2BUGS):
        attr2BUGS.setObjectName(_fromUtf8("attr2BUGS"))
        attr2BUGS.resize(527, 409)
        attr2BUGS.setAcceptDrops(False)
        attr2BUGS.setModal(False)
        self.gridLayout = QtGui.QGridLayout(attr2BUGS)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(attr2BUGS)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(attr2BUGS)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.listView = QtGui.QListView(attr2BUGS)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(attr2BUGS)
        self.pushButton.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(attr2BUGS)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 1, 3, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(attr2BUGS)
        self.pushButton_2.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(324, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 3)
        self.pushButton_3 = QtGui.QPushButton(attr2BUGS)
        self.pushButton_3.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)

        self.retranslateUi(attr2BUGS)
        QtCore.QMetaObject.connectSlotsByName(attr2BUGS)

    def retranslateUi(self, attr2BUGS):
        attr2BUGS.setWindowTitle(QtGui.QApplication.translate("attr2BUGS", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("attr2BUGS", "Fields:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("attr2BUGS", "BUGS script:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("attr2BUGS", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("attr2BUGS", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("attr2BUGS", "Save", None, QtGui.QApplication.UnicodeUTF8))


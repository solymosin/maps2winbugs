# -*- coding: utf-8 -*-
"""
/***************************************************************************
 maps2WinBUGS
                                 A QGIS plugin  a tool to facilitate data processing for Bayesian spatial modeling
                              -------------------
        begin                : 2015-07-31
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Norbert Solymosi
        email                : solymosi.norbert@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtCore import Qt, QFile, QIODevice, QTextStream
from qgis.PyQt.QtWidgets import QDialog, QFileDialog, QApplication
from qgis.PyQt.QtGui import QStandardItemModel, QStandardItem
from qgis.core import QgsFeature, QgsFeatureRequest

from .attr2BUGS_dialog import Ui_attr2BUGS


class Dialog(QDialog, Ui_attr2BUGS):
    def __init__(self, iface, ml):
        """Constructor for the dialog.
        
        Args:
          iface: QgsInterface instance.
        """

        QDialog.__init__(self, iface.mainWindow())

        self.setupUi(self)
        self.setWindowTitle('Attributes to BUGS')

        self.ml = ml

        self.ids = []
        self.polynum = self.ml.featureCount()

        self.model = QStandardItemModel(0, 1)
        self.listView.setModel(self.model)
        self.model.setHeaderData(0, Qt.Horizontal, 'Field')

        provider = self.ml.dataProvider()
        fields = provider.fields()
        for f in fields:
            item = QStandardItem(f.name())
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Unchecked, Qt.CheckStateRole)
            self.model.appendRow(item)

        self.control()

        self.pushButton.clicked.connect(self.konv)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.save)


    def konv(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        self.plainTextEdit.clear()

        mod = min(self.ids)

        provider = self.ml.dataProvider()
        fields = provider.fields()
        lst = '#data\nlist('

        for row in range(0, self.model.rowCount()):
            it = self.model.itemFromIndex(self.model.index(row, 0))
            if it.checkState()==2:
                fld = str(self.model.itemData(self.model.index(row, 0))[0])
                var = fld + '=c('
                ft = fields[row].type()
                if ft==10:
                    for ne in range(mod, self.polynum + mod):
                        feat = QgsFeature()
                        fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
                        if fiter.nextFeature(feat):
                            u = feat.attribute(fld)
                            var += "'%s'," % u
                    var = var[:-2] + "')"
                else:
                    for ne in range(mod, self.polynum + mod):
                        feat = QgsFeature()
                        fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
                        if fiter.nextFeature(feat):
                            u = feat.attribute(fld)
                            var += "%s," % u
                    var = var[:-1] + ')'
                lst += var + ', '
        lst += ')'
        lst = lst.replace('), )', '))')
        self.plainTextEdit.appendPlainText(lst)

        QApplication.restoreOverrideCursor()


    def control(self):
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        feats = provider.getFeatures()
        #self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        #self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, self.polynum))
        ne = 0
        while feats.nextFeature(feat):
            ne += 1
            #self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)
            self.ids.append(feat.id())

    def save(self):
        fileName, _ = QFileDialog.getSaveFileName(self, caption='Save As...')
        try:
            file = QFile(fileName + '.txt')
            file.open(QIODevice.WriteOnly | QIODevice.Text)
            out = QTextStream(file)
            out << self.plainTextEdit.toPlainText()
            out.flush()
            file.close()
            self.close()
            return True
        except IOError:
            return False


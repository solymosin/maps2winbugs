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

from PyQt4.QtCore import SIGNAL, Qt, QFile, QIODevice, QTextStream
from PyQt4.QtGui import QDialog, QFileDialog, QMessageBox, QApplication, QTextCursor
from qgis.core import QgsFeature, QgsGeometry, QgsFeatureRequest

from exp2BUGS_dialog import Ui_exp2BUGS_dialog


class Dialog(QDialog, Ui_exp2BUGS_dialog):
    def __init__(self, iface, ml):
        """Constructor for the dialog.
        
        Args:
          iface: QgsInterface instance.
        """

        QDialog.__init__(self, iface.mainWindow())

        self.setupUi(self)

        self.ml = ml
        self.polynum = 0
        self.deccount = 0
        self.dh = 0
        self.intlen = 0
        self.kicsi = 0
        self.mind = 0
        self.minull = 1000
        self.ids = []

        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.close)

        self.comboBox.addItems(['', 'ArcInfo', 'S-Plus'])

        self.comboBox.currentIndexChanged.connect(self.formatSelect)

    def control(self):
        self.ids = []
        self.polynum = self.ml.featureCount()
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        feats = provider.getFeatures()
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, self.polynum))
        ne = 0
        while feats.nextFeature(feat):
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)
            geom = QgsGeometry(feat.geometry())
            if geom.isMultipart():
                multi_polygon = geom.asMultiPolygon()
                for polygon in multi_polygon:
                    for ring in polygon:
                        for v in ring:
                            self.cintlen(str(v.x()))
                            self.cintlen(str(v.y()))
            else:
                polygon = geom.asPolygon()
                for ring in polygon:
                    for v in ring:
                        self.cintlen(str(v.x()))
                        self.cintlen(str(v.y()))

            self.ids.append(feat.id())

    def cintlen(self, num):
        nulls = 0
        darab = num.partition('.')
        if len(darab) > 2:
            hossz = len(darab[0])
            sdec = darab[2]
            if float(sdec) < 0.1:
                self.kicsi += 1
            h = len(sdec) + 1
            for x in range(1, h):
                if float(sdec[-x:]) == 0:
                    nulls = x
            if nulls < self.minull:
                self.minull = nulls
            if hossz > self.intlen:
                self.intlen = hossz
            self.mind += 1

    def formatSelect(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        self.plainTextEdit.clear()
        self.control()

        dh = 0
        prec = (11 - self.intlen) - self.minull
        scale = 0

        if (float(self.kicsi) / float(self.mind)) > 0.7:
            prec = 0

        if self.comboBox.currentText() == '':
            return
        elif self.comboBox.currentText() == 'ArcInfo':
            self.convArcInfo(prec)
        elif self.comboBox.currentText() == 'S-Plus':
            self.convSplus(prec)

        self.plainTextEdit.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)

        if prec <= 3:
            scale = pow(10, (prec - 1))
        if prec >= 4:
            scale = pow(10, 4)
        if (float(self.kicsi) / float(self.mind)) > 0.7:
            scale = pow(10, 0)

        self.plainTextEdit.insertPlainText('map:%s\n\nXscale:%s\nYscale:%s\n\n' % (self.polynum, scale, scale))

        QApplication.restoreOverrideCursor()

    def save(self):
        fileName = QFileDialog.getSaveFileName(self, caption='Save As...')
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

    def convArcInfo(self, prec):
        for i in range(0, self.polynum):
            j = i + 1
            self.plainTextEdit.appendPlainText("%s area%s" % (j, j))

        self.plainTextEdit.appendPlainText("\nregions")

        provider = self.ml.dataProvider()
        i = 1
        n = 1

        mod = min(self.ids)
        p = 1
        if mod==1:
            p = 0

        for ne in range(mod, self.polynum + mod):
            feat = QgsFeature()
            geom = QgsGeometry()
            fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
            if fiter.nextFeature(feat):
                geom = QgsGeometry(feat.geometry())

            if geom.isMultipart():
                multi_polygon = geom.asMultiPolygon()
                for polygon in multi_polygon:
                    for ring in polygon:
                        self.plainTextEdit.appendPlainText("%s area%s" % (n, feat.id()+p))
                        n += 1
            else:
                polygon = geom.asPolygon()
                for ring in polygon:
                    self.plainTextEdit.appendPlainText("%s area%s" % (n, feat.id()+p))
                    n += 1
            i += 1

        self.plainTextEdit.appendPlainText("END")

        n = 1
        for ne in range(mod, self.polynum + mod):
           pn = 1
           feat = QgsFeature()
           geom = QgsGeometry()
           fiter = self.ml.getFeatures(QgsFeatureRequest(ne))


           if fiter.nextFeature(feat):
               geom = QgsGeometry(feat.geometry())

           id = feat.id()+p

           if geom.isMultipart():
               multi_polygon = geom.asMultiPolygon()
               for polygon in multi_polygon:
                   for ring in polygon:
                       self.plainTextEdit.appendPlainText("%s 0 0" % (n))
                       for v in ring:
                           self.plainTextEdit.appendPlainText("%s %s" % (round(v.x(),prec), round(v.y(),prec)))
                           pn += 1
                       self.plainTextEdit.appendPlainText("END")
                       n += 1
           else:
               polygon = geom.asPolygon()
               for ring in polygon:
                   self.plainTextEdit.appendPlainText("%s 0 0" % (n))
                   for v in ring:
                       self.plainTextEdit.appendPlainText("%s %s" % (round(v.x(),prec), round(v.y(),prec)))
                       pn += 1
                   self.plainTextEdit.appendPlainText("END")
                   n += 1
               if pn>=10000:
                   QMessageBox.information(self,
                                           "Too many points",
                                           "Polygon No. %s contains to many points to read into GeoBUGS.\nSimplifying of polygon can solve this problem." % (id),
                                           buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)

           self.progressBar.setValue(100*id/self.polynum)
        self.plainTextEdit.appendPlainText("END")


    def convSplus(self, prec):
        for i in range(0, self.polynum):
            j = i + 1
            self.plainTextEdit.appendPlainText("%s area%s" % (j, j))

        self.plainTextEdit.appendPlainText("")
        mod = min(self.ids)
        p = 1
        if mod==1:
            p = 0

        for ne in range(mod, self.polynum + mod):
            pn = 1
            feat = QgsFeature()
            geom = QgsGeometry()

            fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
            if fiter.nextFeature(feat):
                geom = QgsGeometry(feat.geometry())

            id = feat.id()+p

            if geom.isMultipart():
                multi_polygon = geom.asMultiPolygon()
                for polygon in multi_polygon:
                    for ring in polygon:
                        for v in ring:
                            self.plainTextEdit.appendPlainText(
                                "area%s %s %s" % (id, round(v.x(), prec), round(v.y(), prec)))
                            pn += 1
                        self.plainTextEdit.appendPlainText("NA NA NA")
            else:
                polygon = geom.asPolygon()
                for ring in polygon:
                    for v in ring:
                        self.plainTextEdit.appendPlainText(
                            "area%s %s %s" % (id, round(v.x(), prec), round(v.y(), prec)))
                        pn += 1
                    self.plainTextEdit.appendPlainText("NA NA NA")

            if pn >= 10000:
                QMessageBox.information(self,
                                        "Too many points",
                                        "Polygon No. %s contains to many points to read into GeoBUGS.\nSimplifying of polygon can solve this problem." % (id),
                                        buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)

            self.progressBar.setValue(100 * id / self.polynum)

        self.plainTextEdit.appendPlainText("END")

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

from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.gui import *

from splusimport_dialog import Ui_SPlusImport


class Dialog(QDialog, Ui_SPlusImport):
    def __init__(self, iface):
        """Constructor for the dialog.
        
        Args:
          iface: QgsInterface instance.
        """
        
        QDialog.__init__(self, iface.mainWindow())                               

        self.setupUi(self)

        self.settings = QSettings()
        self.enc = self.settings.value('/Processing/encoding', 'System')

        self.connect(self.buttonBox, SIGNAL('rejected()'), self.reject)
        self.connect(self.buttonBox, SIGNAL('accepted()'), self.accept)
        self.toolButton.clicked.connect(self.fileSource)
        self.toolButton_3.clicked.connect(self.fileDest)


    def fileSource(self):
        splusfile = QFileDialog.getOpenFileName(self, 'Open file', QDir.currentPath(), "S-plus file (*.map *.txt)")
        self.lineEdit.setText(splusfile)


    def fileDest(self):
        oFD = QgsEncodingFileDialog(self, self.tr("Save As"), QDir.currentPath(), "Shape files (*.shp)", self.enc)
        oFD.setFileMode(QFileDialog.AnyFile)
        oFD.setAcceptMode(QFileDialog.AcceptSave)
        oFD.setConfirmOverwrite(True)
        self.enc = oFD.encoding()

        if oFD.exec_()==QDialog.Accepted:
            files = oFD.selectedFiles()
            fn = unicode(files[0])
            fi = QFileInfo(fn)
            if fi.completeSuffix()=='':
                fn+='.shp'
            elif fi.completeSuffix()=='shp':
                fn.replace(fi.completeSuffix(), "shp")

            self.lineEdit_2.setText(fn)


    def accept(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        splusfile = self.lineEdit.text()
        output = self.lineEdit_2.text()

        if splusfile=="" or output=="":
            return

        srs = QgsCoordinateReferenceSystem('4326')

        map = QFile(splusfile)
        bool = map.open(QIODevice.ReadOnly)
        stream = QTextStream(map)
        sep = ":"

        line = str(stream.readLine())
        slen = 0
        featnum = int(line.strip().replace(' ', '').split(sep)[1])

        sep = '\t'

        for i in range(0, featnum):
            line = str(stream.readLine())
            chunk = line.strip().replace(' ', '').split(sep)[1]
            if slen<len(chunk):
                slen = len(chunk)

        id = ''
        feats = ''
        idLst = []
        featLst = []
        p1 = QgsPoint()
        p2 = QgsPoint()
        pi = 0

        while not stream.atEnd():
            line = str(stream.readLine())
            lst = line.strip().replace(' ', '').split(sep)
            if len(lst)==3:
                if line!="NA\tNA\tNA":
                    if pi==0:
                        p1.setX(float(lst[1]))
                        p1.setY(float(lst[2]))
                    feats+= '%s %s, ' % (float(lst[1]), float(lst[2]))
                    id = lst[0]
                    pi+=1
                    p2.setX(float(lst[1]))
                    p2.setY(float(lst[2]))
                elif line=="NA\tNA\tNA":
                    if p1!=p2:
                        feats+= '%s %s, ' % (p1.x(), p1.y())
                    idLst.append(id)
                    qs = feats[:-2]
                    featLst.append(qs)
                    feats = ''
                    pi = 0

        prev = ''
        id = ''
        idGrouped = []
        n = 1
        for i in range(0, len(idLst)):
            if idLst[i]==prev:
                id+=', %s' % (i)
            else:
                idGrouped.append(id)
                id = '%s' % (i)
                if i==(len(idLst)-1):
                    idGrouped.append(id)
                n+=1
            prev = idLst[i]

        fields = QgsFields()
        fields.append(QgsField('id', QVariant.Int, '', 10, 0))
        wrt = QgsVectorFileWriter(output, self.enc, fields, QGis.WKBPolygon, srs)

        sep = ","

        for i in range(0, featnum):
            ii = i+1
            wkt = ''
            sor = idGrouped[ii]
            sorlst = sor.strip().replace(' ', '').split(sep)
            chunk = ''
            if len(sorlst)==1:
                az = int(sorlst[0])
                chunk = featLst[az]
                wkt = 'POLYGON((%s))' % (chunk)
            elif len(sorlst)==2:
                for j in range(0, len(sorlst)):
                    az = int(sorlst[j])
                    chunk+= "%s), (" % featLst[az]
                wkt = "POLYGON((%s))" % chunk[:-4]
            elif len(sorlst)>2:
                for j in range(0, len(sorlst)):
                    az = int(sorlst[j])
                    chunk+= "%s), (" % featLst[az]
                wkt = "MULTIPOLYGON(((%s)))" % chunk[:-4]
            geom = QgsGeometry(QgsGeometry.fromWkt(wkt))
            feat = QgsFeature()
            feat.setFields(fields)
            feat.setGeometry(geom)
            feat['id'] = ii
            wrt.addFeature(feat)

        del wrt

        QDialog.accept(self)

        QApplication.restoreOverrideCursor()

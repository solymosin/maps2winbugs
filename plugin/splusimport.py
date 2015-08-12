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

from PyQt4.QtCore import SIGNAL, Qt, QModelIndex, QDir, QFileInfo, QSettings
from PyQt4.QtGui import QDialog, QFileDialog, QApplication, QStandardItemModel, QAbstractItemView, QItemSelectionModel
from qgis.core import QGis, QgsFeature, QgsGeometry, QgsFeatureRequest, QgsVectorLayerCache
from qgis.gui import QgsRubberBand, QgsEncodingFileDialog

from splusimport_dialog import Ui_SPlusImport


class Dialog(QDialog, Ui_SPlusImport):
    def __init__(self, iface):
        """Constructor for the dialog.
        
        Args:
          iface: QgsInterface instance.
        """
        
        QDialog.__init__(self, iface.mainWindow())                               

        self.setupUi(self)

        self.connect(self.buttonBox, SIGNAL('rejected()'), self.reject)
        self.connect(self.buttonBox, SIGNAL('accepted()'), self.accept)
        self.toolButton.clicked.connect(self.fileSource)
        self.toolButton_3.clicked.connect(self.fileDest)


    def fileSource(self):
        splusfile = QFileDialog.getOpenFileName(self, 'Open file', QDir.currentPath(), "S-plus file (*.map *.txt)")
        self.lineEdit.setText(splusfile)


    def fileDest(self):
        settings = QSettings()
        enc = settings.value('/Processing/encoding', 'System')

        oFD = QgsEncodingFileDialog(self, self.tr("Save As"), QDir.currentPath(), "Shape files (*.shp)", enc)
        oFD.setFileMode(QFileDialog.AnyFile)
        oFD.setAcceptMode(QFileDialog.AcceptSave)
        oFD.setConfirmOverwrite(True)

        if oFD.exec_()==QDialog.Accepted:
            files = oFD.selectedFiles()
            encoding = unicode(oFD.encoding())
            fn = unicode(files[0])
            fi = QFileInfo(fn)
            if fi.completeSuffix()=='':
                fn+='.shp'
            elif fi.completeSuffix()=='shp':
                fn.replace(fi.completeSuffix(), "shp")

            self.lineEdit_2.setText(fn)


    def accept(self):
        k = 1

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 maps2WinBUGS
                                 A QGIS plugin
 a tool to facilitate data processing for
Bayesian spatial modeling
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

from PyQt4.QtCore import SIGNAL, Qt, QFile, QIODevice, QTextStream, QObject, QModelIndex
from PyQt4.QtGui import QDialog, QProgressDialog, QFileDialog, QMessageBox, QApplication, QTextCursor, QStandardItemModel, QAbstractItemView, QItemSelectionModel
from qgis.core import QGis, QgsVectorLayer, QgsFeature, QgsGeometry, QgsVectorDataProvider, QgsFields, QgsField, QgsFeatureRequest, QgsPoint

from xdist_dialog import Ui_xDist


class Dialog(QDialog, Ui_xDist):         
    def __init__(self):
        """Constructor for the dialog.
        
        """
        
        QDialog.__init__(self)                               
                        
        self.setupUi(self)
        
        self.pushCancel.clicked.connect(self.reject)
        self.pushOK.clicked.connect(self.accept)    



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

from PyQt4.QtCore import SIGNAL, Qt, QFile, QIODevice, QTextStream, QObject, QModelIndex
from PyQt4.QtGui import QDialog, QProgressDialog, QFileDialog, QMessageBox, QApplication, QTextCursor, QStandardItemModel, QAbstractItemView, QItemSelectionModel,  QPlainTextEdit
from qgis.core import QGis, QgsVectorLayer, QgsFeature, QgsGeometry, QgsVectorDataProvider, QgsFields, QgsField, QgsFeatureRequest, QgsPoint, QgsVectorLayerCache
from qgis.gui import QgsMapCanvas, QgsRubberBand

from nbEditor_dialog import Ui_nbEditor_dialog
import editor
import xdist

class Dialog(QDialog, Ui_nbEditor_dialog):         
    def __init__(self, iface, ml, mc):
        """Constructor for the dialog.
        
        Args:
          iface: QgsInterface instance.
        """
        
        QDialog.__init__(self, iface.mainWindow())                               
                        
        self.setupUi(self)
        
        self.ml = ml
        self.mCanvas = mc         
        self.mRubberBand = QgsRubberBand(self.mCanvas, True)
        self.mRubberBand.reset(QGis.Polygon)
        self.mRubberBand.setColor(Qt.red)
        self.mRubberBand.setWidth(2)
        self.ids = []
        
        self.ini(0)
        
        self.pushCancel.clicked.connect(self.close)
        self.pushOK.clicked.connect(self.convert)
        self.comboBox.addItems(['','Intersections','Touches','Within distance']) 
        
        self.comboBox.currentIndexChanged.connect(self.nbMethod)         
        self.ml.selectionChanged.connect(self.map2tab)
        
        
    def ini(self, n):
        self.model = QStandardItemModel(n, 1)
        self.tableView.setModel(self.model)
        self.model.setHeaderData(0, Qt.Horizontal, 'Neighbouring IDs')
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)        
        self.selectionModel = QItemSelectionModel(self.model)
        self.tableView.setSelectionModel(self.selectionModel)
        self.tableView.horizontalHeader().setStretchLastSection(True)    
        self.tableView.selectionModel().selectionChanged.connect(self.tab2map)
        self.progressBar.setValue(0)


    def settings(self):
        self.mod = min(self.ids)
        self.p = 1
        if self.mod==1:
            self.p = 0


    def map2tab(self):
        s = ''
        idx = self.tableView.selectionModel().selectedIndexes()[0]
        ts = str(self.model.itemData(idx)[0])
        
        for fid in sorted(self.ml.selectedFeaturesIds()):
            s += '%s,' % str(int(fid)+self.p)                   
 
        s = s[:-1]
         
        if s!=ts:
            self.model.setData(idx, s)
         
        # in order to handle the symmetry
        if len(s)>len(ts):
             iLst = s.strip().replace(' ', '').split(',')
             jLst = ts.strip().replace(' ', '').split(',')
        else:
             iLst = ts.strip().replace(' ', '').split(',')
             jLst = s.strip().replace(' ', '').split(',')
              
        cent = str(idx.row()+self.p)
        dLst = list(set(iLst)-set(jLst))
          
        for d in dLst:              
            row = int(d)-self.p
            sor = str(self.model.itemData(self.model.index(row, 0))[0])
            eLst = sor.strip().replace(' ', '').split(',')            
            res = ''
            if cent in set(eLst):
                ii = eLst.index(cent)                
                del eLst[ii]
                eLst = sorted(map(int, eLst))                
                for e in eLst:
                    res += '%s,' % e
                res = res[:-1]
            else:
                u = sor + ',%s' % cent
                eLst = sorted(map(int, u.strip().replace(' ', '').split(',')))
                for e in eLst:
                    res += '%s,' % e
                res = res[:-1]                 
                               
            self.model.setData(self.model.index(row, 0, QModelIndex()), res)
                   
                
    def nbWithinDist(self):
        dlg = xdist.Dialog()
        dlg.setModal(True)
        dlg.setWindowTitle("Between two objects")
                
        if dlg.exec_() == QDialog.Accepted:
            lDist = float(dlg.lineEdit.text())
            if lDist==0:
                return

            feat = QgsFeature()
            provider = self.ml.dataProvider()
            e = provider.featureCount()

            self.settings()

            for ne in range(self.mod, e + self.mod):
                feat = QgsFeature()
                geom = QgsGeometry()
                fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
                if fiter.nextFeature(feat):
                    geom = QgsGeometry(feat.geometry())

                neighbours = self.hdist(feat, lDist)
                row = feat.id()-self.mod
                self.model.setData(self.model.index(row, 0, QModelIndex()), neighbours)
                self.progressBar.setValue(100*ne/e)


    def hdist(self, feata, lDist):
        geoma = QgsGeometry(feata.geometry()) 
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        feats = provider.getFeatures()
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, provider.featureCount())) 
        ne = 0              
        neighbours = ""
        while feats.nextFeature(feat):
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)                       
            geomb = QgsGeometry(feat.geometry())            
            if feata.id()!=feat.id():
                if geoma.distance(geomb)<=lDist:
                    neighbours = neighbours + '%s,' % (feat.id()+self.p)
        return neighbours[:-1]            
    
    
    def tab2map(self):        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        
        self.ml.selectionChanged.disconnect(self.map2tab)
        
        idx = self.tableView.selectionModel().selectedIndexes()[0]
        featureId = idx.row() + self.p
        
        s = self.model.itemData(idx)
        lst = s[0].strip().replace(' ', '').split(',')
        
        self.ml.removeSelection()
        
        for sid in lst:
            self.ml.select(int(sid)-self.p)
              
        provider = self.ml.dataProvider()        
        
        feat = QgsFeature()
        layer = QgsVectorLayerCache(self.ml, provider.featureCount())
        layer.featureAtId(idx.row()+self.mod, feat)
        geom = QgsGeometry(feat.geometry())   
        
        self.mRubberBand.setToGeometry(geom, self.ml)
        self.mRubberBand.show()
        
        self.ml.selectionChanged.connect(self.map2tab)
        
        QApplication.restoreOverrideCursor()        
        
        
    def closeEvent(self,event):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        self.ml.selectionChanged.disconnect(self.map2tab)
        self.ml.removeSelection()
        self.mRubberBand.hide()
        self.close()

        QApplication.restoreOverrideCursor()

        
    def convert(self):
        dlg = editor.Dialog()
        dlg.setModal(True)
        dlg.setWindowTitle("Neighbour list in BUGS format")
        num = ""
        adj = ""
        sumNumNeigh = 0
        for row in range(0, self.model.rowCount()):
            ts = self.model.itemData(self.model.index(row, 0))
            lst = ts[0].strip().replace(' ', '').split(',')
            num += '%s, ' % len(lst)
            sumNumNeigh += len(lst)
            lst.reverse()
            sor = ', '.join(lst) + ','
            adj = adj + str(sor) + '\n' 
        
        num = num[:-2]
        adj = adj[:-2]
        
        nblist = 'list(\nnum = c(%s),\nadj = c(%s),\nsumNumNeigh=%s)' % (num, adj, sumNumNeigh)
        dlg.plainTextEdit.appendPlainText(nblist)
        
        dlg.exec_()                


    def nbMethod(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        self.ml.selectionChanged.disconnect(self.map2tab)
        self.model.removeRows(0, self.model.rowCount(QModelIndex()), QModelIndex())
        n = self.ml.dataProvider().featureCount()
        self.ini(n)

        self.ids = []

        provider = self.ml.dataProvider()
        feats = provider.getFeatures()
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, n))
        ne = 0
        feat = QgsFeature()
        while feats.nextFeature(feat):
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)
            self.ids.append(feat.id())

        if self.comboBox.currentText()=="Touches":            
            if self.ml.geometryType()==0:
                return
            else:
                self.nbTouches()
        if self.comboBox.currentText()=="Intersections":
            if self.ml.geometryType()==0:
                return
            else:
                self.nbIntersects()
        if self.comboBox.currentText()=="Within distance":
            self.nbWithinDist()

        self.ml.selectionChanged.connect(self.map2tab)

        QApplication.restoreOverrideCursor()
        
            
    def nbTouches(self):                                
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        e = provider.featureCount()

        self.settings()

        for ne in range(self.mod, e + self.mod):
            feat = QgsFeature()
            geom = QgsGeometry()
            fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
            if fiter.nextFeature(feat):
                geom = QgsGeometry(feat.geometry())

            neighbours = self.htouch(feat)
            row = feat.id()-self.mod    
            self.model.setData(self.model.index(row, 0, QModelIndex()), neighbours)
            self.progressBar.setValue(100*ne/e)

         
    def htouch(self, feata):
        geoma = QgsGeometry(feata.geometry()) 
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        feats = provider.getFeatures()
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, provider.featureCount())) 
        ne = 0              
        neighbours = ""
        while feats.nextFeature(feat):
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)                       
            geomb = QgsGeometry(feat.geometry())
            if feata.id()!=feat.id():
                if geoma.touches(geomb)==True:
                    neighbours = neighbours + '%s,' % (feat.id()+self.p)                
        return neighbours[:-1]

    
    def nbIntersects(self):
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        e = provider.featureCount()

        self.settings()

        for ne in range(self.mod, e + self.mod):
            feat = QgsFeature()
            geom = QgsGeometry()
            fiter = self.ml.getFeatures(QgsFeatureRequest(ne))
            if fiter.nextFeature(feat):
                geom = QgsGeometry(feat.geometry())

            neighbours = self.hintersect(feat)
            row = feat.id()-self.mod
            self.model.setData(self.model.index(row, 0, QModelIndex()), neighbours)
            self.progressBar.setValue(100*ne/e)


    def hintersect(self, feata):
        geoma = QgsGeometry(feata.geometry())  
        feat = QgsFeature()
        provider = self.ml.dataProvider()
        feats = provider.getFeatures()
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, provider.featureCount())) 
        ne = 0              
        neighbours = ""
        while feats.nextFeature(feat):
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)                       
            geomb = QgsGeometry(feat.geometry())
            if feata.id()!=feat.id():
                if geoma.intersects(geomb)==True:
                    neighbours = neighbours + '%s,' % (feat.id()+self.p)
        return neighbours[:-1]
    

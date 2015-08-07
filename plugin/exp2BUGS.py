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
from PyQt4.QtGui import QDialog, QProgressDialog, QFileDialog, QMessageBox, QApplication, QTextCursor
from qgis.core import QGis, QgsVectorLayer, QgsFeature, QgsGeometry, QgsVectorDataProvider, QgsFields, QgsField, QgsFeatureRequest, QgsPoint

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
        
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.close)
        
        self.comboBox.addItems(['','ArcInfo','S-Plus']) 
        
        self.comboBox.currentIndexChanged.connect(self.formatSelect)                    
        
        
    def control(self):
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
        
        
    def cintlen(self, num):
        nulls = 0
        darab = num.partition('.')
        if len(darab)>2:
            hossz = len(darab[0])
            sdec = darab[2]
            if float(sdec)<0.1:
                self.kicsi +=1
            h = len(sdec)+1
            for x in range(1, h): 
                if float(sdec[-x:])==0:
                    nulls = x
            if nulls<self.minull:
                self.minull=nulls
            if hossz>self.intlen:
                self.intlen=hossz 
            self.mind +=1           
        #float(s.partition('.')[2][-1:])==0
        
        
    def formatSelect(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.control()        
        
        dh = 0
        prec = (11-self.intlen)-self.minull
        scale = 0
        
        if (float(self.kicsi)/float(self.mind))>0.7:
            prec = 0
        
        if self.comboBox.currentText()=='':
            return
        elif self.comboBox.currentText()=='ArcInfo':
            self.convArcInfo(prec)
        elif self.comboBox.currentText()=='S-Plus':
            self.convSplus(prec)
        
        self.plainTextEdit.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
        
        if prec<=3:
            scale = pow(10,(prec-1))
        if prec>=4:
            scale = pow(10,4)
        if (float(self.kicsi)/float(self.mind))>0.7:
            scale = pow(10,0)
        
        self.plainTextEdit.insertPlainText('map:%s\n\nXscale:%s\nYscale:%s\n\n' % (self.polynum, scale, scale))
        
        QApplication.restoreOverrideCursor()

    def save(self):
        fileName = QFileDialog.getSaveFileName(self, caption='Save As...')
        try:
            file = QFile(fileName + '.txt')
            file.open( QIODevice.WriteOnly | QIODevice.Text )
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
            j = i+1
            self.plainTextEdit.appendPlainText("%s area%s" % (j,j))
#             
        self.plainTextEdit.appendPlainText("\nregions")  
        
        provider = self.ml.dataProvider()
        feat = QgsFeature()
        i = 1
        n = 1        
        ne = 0
        feats = provider.getFeatures()        
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, self.polynum))        
        while feats.nextFeature(feat):            
             ne += 1
             self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)           
             geom = QgsGeometry(feat.geometry())                     
             if geom.isMultipart():                
                 multi_polygon = geom.asMultiPolygon()
                 for polygon in multi_polygon:
                     for ring in polygon:
                         self.plainTextEdit.appendPlainText("%s area%s" % (n,i))
                         n = n+1                        
             else:
                 polygon = geom.asPolygon()                
                 for ring in polygon:
                     self.plainTextEdit.appendPlainText("%s area%s" % (n,i))
                     n = n+1
             i = i+1
              
        self.plainTextEdit.appendPlainText("END")
        
        feats = provider.getFeatures()
        nu = 1
        n = 1     
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, self.polynum)) 
        ne = 0                
        while feats.nextFeature(feat):
            pn = 1
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)           
            geom = QgsGeometry(feat.geometry())      
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
                                        "Polygon No. %s contains to many points to read into GeoBUGS.\nSimplifying of polygon can solve this problem." % (nu), 
                                        buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)
		
            self.progressBar.setValue(100*nu/self.polynum)            
        
            nu += 1
            
        self.plainTextEdit.appendPlainText("END")


    def convSplus(self, prec):                                                      
        for i in range(0, self.polynum):
            j = i+1
            self.plainTextEdit.appendPlainText("%s area%s" % (j,j))

        self.plainTextEdit.appendPlainText("")  
        provider = self.ml.dataProvider()
        feat = QgsFeature()
        feats = provider.getFeatures()  
        self.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
        self.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, self.polynum)) 
        ne = 0
        nu = 1                
        while feats.nextFeature(feat):
            pn = 1
            ne += 1
            self.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)           
            geom = QgsGeometry(feat.geometry())      
            if geom.isMultipart():
                multi_polygon = geom.asMultiPolygon()
                for polygon in multi_polygon:                    
                    for ring in polygon:
                        for v in ring:
                            self.plainTextEdit.appendPlainText("area%s %s %s" % (nu, round(v.x(),prec), round(v.y(),prec)))
                            pn += 1                        
                        self.plainTextEdit.appendPlainText("NA NA NA")                     
            else:
                polygon = geom.asPolygon()                
                for ring in polygon:
                    for v in ring:
                        self.plainTextEdit.appendPlainText("area%s %s %s" % (nu, round(v.x(),prec), round(v.y(),prec)))
                        pn += 1
                    self.plainTextEdit.appendPlainText("NA NA NA")
        
            if pn>=10000:
                QMessageBox.information(self, 
                                        "Too many points", 
                                        "Polygon No. %s contains to many points to read into GeoBUGS.\nSimplifying of polygon can solve this problem." % (nu), 
                                        buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)
					
            self.progressBar.setValue(100*nu/self.polynum)        
            nu += 1
            
        self.plainTextEdit.appendPlainText("END")
                

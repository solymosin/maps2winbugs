# -*- coding: utf-8 -*-
"""
/***************************************************************************
 maps2WinBUGS
                                 A QGIS plugin  a tool to facilitate data processing for Bayesian spatial modeling
                              -------------------
        begin                : 2015-07-31
        git sha              : $Format:%H$
        copyright        : (C) 2015 by Norbert Solymosi
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

from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, Qt, QSettings, QCoreApplication
from qgis.core import QgsMapLayerRegistry, QgsFeature, QgsGeometry, QgsFeatureRequest, QgsPoint

from plugin import exp2BUGS
from plugin import nbEditor
from plugin import xabout
from plugin import attr2BUGS
from plugin import editor
from plugin import splusimport


import resources_rc
import os.path

class maps2WinBUGS:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        self.mCanvas = self.iface.mapCanvas()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'maps2winbugs_{}.qm'.format(locale))
        self.vers = '2.25'

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('maps2winbugs', message)


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.actBUGS = QAction(
            QIcon(':/plugins/maps2WinBUGS/images/icon01.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'Map to BUGS'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actBUGS)
        self.actBUGS.triggered.connect(self.exp2GeoBUGS)

        self.actCNTR = QAction(
            QIcon(':/plugins/maps2WinBUGS/images/icon05.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'Centroids to BUGS'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actCNTR)
        self.actCNTR.triggered.connect(self.cntr2bugs)

        self.actATTR = QAction(
            QIcon(':/plugins/maps2WinBUGS/images/icon03.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'Attributes to BUGS'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actATTR)
        self.actATTR.triggered.connect(self.attr2bugs)

        self.actNEIGH = QAction(
            QIcon(':/plugins/maps2WinBUGS/images/icon02.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'Neighbouring'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actNEIGH)
        self.actNEIGH.triggered.connect(self.Neighbouring)

        self.actSPLUS = QAction(
            QIcon(':/plugins/maps2WinBUGS/images/icon06.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'Import S-Plus map'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actSPLUS)
        self.actSPLUS.triggered.connect(self.importSplus)
            
        self.actAbout = QAction(
            QIcon(':/plugins/maps2WinBUGS/images/icon04.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'About'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actAbout)
        self.actAbout.triggered.connect(self.about)   
        
        self.toolbar = self.iface.addToolBar(
            QCoreApplication.translate('maps2winbugs',
                                       'maps2WinBUGS'))
        self.toolbar.setObjectName(
            QCoreApplication.translate('maps2winbugs',
                                       'maps2WinBUGS'))

        # self.toolbar.addAction(self.actATTR)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu('&maps2WinBUGS', self.actBUGS)
        del self.toolbar
       
    
    def  checklayer(self):
        if QgsMapLayerRegistry.instance().count()==0:
            QMessageBox.warning(self.iface.mainWindow(), 
                                                    "Warning", 
                                                    "Please add a vector layer.", 
                                                    buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)               
            return
                
        mLayer = self.iface.activeLayer()
        if mLayer is None:
            QMessageBox.warning(self.iface.mainWindow(), 
                                                    "Warning", 
                                                    "Please select an input layer.", 
                                                    buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)         
            return

        if mLayer.type()!=0:
            QMessageBox.warning(self.iface.mainWindow(), 
                                                    "Warning", 
                                                    "Please select a vector layer.", 
                                                    buttons=QMessageBox.Ok, defaultButton=QMessageBox.NoButton)               
            return        
            
        return mLayer


    def importSplus(self):
        dlg = splusimport.Dialog(self.iface)
        dlg.setModal(True)
        dlg.setWindowTitle('Import S-Plus map')

        dlg.lineEdit.setText('/home/sn/Desktop/Belgium.txt')
        dlg.lineEdit_2.setText('/home/sn/Desktop/be.shp')

        dlg.exec_()


    def cntr2bugs(self):
        mLayer = self.checklayer()
        if mLayer is not None:
            QApplication.setOverrideCursor(Qt.WaitCursor)

            dlg = editor.Dialog()
            dlg.setModal(True)
            dlg.setWindowTitle("Centroids in BUGS format")

            provider = mLayer.dataProvider()
            e = provider.featureCount()

            ids = []
            x = "x = c("
            y = "y = c("

            feats = provider.getFeatures()
            dlg.emit(SIGNAL("runStatus(PyQt_PyObject)"), 0)
            dlg.emit(SIGNAL("runRange(PyQt_PyObject)"), (0, e))
            ne = 0
            feat = QgsFeature()
            while feats.nextFeature(feat):
                ne += 1
                dlg.emit(SIGNAL("runStatus(PyQt_PyObject)"), ne)
                ids.append(feat.id())

            mod = min(ids)

            for ne in range(mod, e + mod):
                feat = QgsFeature()
                pt = QgsPoint()
                fiter = mLayer.getFeatures(QgsFeatureRequest(ne))
                if fiter.nextFeature(feat):
                    pt = QgsGeometry(feat.geometry().centroid()).asPoint()
                    # pt = QgsGeometry(geom.centroid()).asPoint()

                x += '%s, ' % pt.x()
                y += '%s, ' % pt.y()

            dlg.plainTextEdit.appendPlainText(x[:-2]+')')
            dlg.plainTextEdit.appendPlainText(y[:-2]+')')

            QApplication.restoreOverrideCursor()

            dlg.exec_()


    def Neighbouring(self):
        mLayer = self.checklayer()
        if mLayer is not None:
            self.nbDialog = nbEditor.Dialog(self.iface, mLayer, self.mCanvas)
            self.nbDialog.show()     
                

    def exp2GeoBUGS(self):
        mLayer = self.checklayer()
        if mLayer is not None:
            self.exp2BUGSDialog = exp2BUGS.Dialog(self.iface, mLayer)
            self.exp2BUGSDialog.exec_()


    def about(self):         
        dlg = xabout.Dialog()
        dlg.setWindowTitle('About')
        dlg.plainTextEdit.appendPlainText(u'maps2WinBUGS ' + self.vers +'\n')
        dlg.plainTextEdit.appendPlainText(u"Developed by\n\tSolymosi Norbert\n\tsolymosi.norbert@gmail.com\n")
        dlg.plainTextEdit.appendPlainText(u"Contributors:\n\tWagner, Sara E. \n\tAllepuz, Alberto\n\tMaróti-Agóts Ákos")
        dlg.plainTextEdit.appendPlainText(u"\n\nIcons came from www.flaticon.com")
        dlg.exec_()


    def attr2bugs(self):
        mLayer = self.checklayer()
        if mLayer is not None:
            self.attrDlg = attr2BUGS.Dialog(self.iface, mLayer)
            self.attrDlg.exec_()

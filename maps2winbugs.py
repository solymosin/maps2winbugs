# -*- coding: utf-8 -*-
"""
/***************************************************************************
 map2WinBUGS
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

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.gui import *
from qgis.core import QgsMapLayerRegistry

from plugin import exp2BUGS

import resources_rc
import os.path

class map2WinBUGS:
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
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'maps2winbugs_{}.qm'.format(locale))

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
            QIcon(':/plugins/map2WinBUGS/images/icon01.png'),
            QCoreApplication.translate(
                'maps2winbugs',
                'Export to GeoBUGS'),
            self.iface.mainWindow())
        self.iface.addPluginToMenu('&maps2WinBUGS', self.actBUGS)
        self.actBUGS.triggered.connect(self.exp2GeoBUGS)
        

        self.toolbar = self.iface.addToolBar(
            QCoreApplication.translate('maps2winbugs',
                                       'maps2WinBUGS'))
        self.toolbar.setObjectName(
            QCoreApplication.translate('maps2winbugs',
                                       'maps2WinBUGS'))

#         self.toolbar.addAction(self.actBUGS)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu('&maps2WinBUGS', self.actBUGS)
        del self.toolbar


    def exp2GeoBUGS(self):
        if QgsMapLayerRegistry.instance().count()==0:
            return
        
        mLayer = self.iface.activeLayer()
        if mLayer.type()!=0:
            return
                  
        self.exp2BUGSDialog = exp2BUGS.Dialog(self.iface, mLayer)
        self.exp2BUGSDialog.exec_()



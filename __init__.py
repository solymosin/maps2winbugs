# -*- coding: utf-8 -*-
"""
/***************************************************************************
 map2WinBUGS
                                 A QGIS plugin
 a tool to facilitate data processing for
Bayesian spatial modeling
                             -------------------
        begin                : 2015-07-31
        copyright            : (C) 2015 by Norbert Solymosi
        email                : solymosi.norbert@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load map2WinBUGS class from file map2WinBUGS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .maps2winbugs import map2WinBUGS
    return map2WinBUGS(iface)

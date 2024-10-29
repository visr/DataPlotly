"""
/***************************************************************************
 DataPlotly
                                 A QGIS plugin
 D3 Plots for QGIS
                              -------------------
        begin                : 2022-08-20
        git sha              : $Format:%H$
        copyright            : (C) 2022 by matteo ghetta
        email                : matteo.ghetta@gmail.com
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


from qgis.PyQt.QtGui import QIcon

import os

from .dataplotly_generic_plot import DataPlotlyProcessingPlot


class DataPlotlyProcessingScatterPlot(DataPlotlyProcessingPlot):
    """
    Create a scatter with DataPlotly plugin
    """

    # constructor
    def __init__(self, ):
        super().__init__(plot_type='scatter')

    def name(self):
        return 'scatterplot'

    def displayName(self):
        return 'Scatter Plot'

    def icon(self):
        return QIcon(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "core",
                "plot_types",
                "icons",
                "scatterplot.svg",
            )
        )

    def createInstance(self):
        return DataPlotlyProcessingScatterPlot()

    def initAlgorithm(self, config=None):

        # create the parameters list
        parameters = self.create_parameter_dictionary(self.plot_type)

        # loop and fill the parameters
        for param in parameters:
            self.addParameter(param)

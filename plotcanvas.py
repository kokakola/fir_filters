# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from numpy import sin, cos, pi, arange, absolute, sqrt

import random

class PlotCanvas(FigureCanvas):

	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)

		FigureCanvas.__init__(self, fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)


	def plot(self, w, h, nyq_rate):

		print ('halo')

		ax = self.figure.add_subplot(111)
		ax.plot((w/pi)*nyq_rate, absolute(h), 'r-')
		ax.set_title('PyQt Matplotlib Example')

		self.draw()


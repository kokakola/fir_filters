import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from numpy import pi, absolute
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random

 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def plot_grap_1(self, w, h, nyq_rate):
        ax = self.figure.add_subplot(111)

        ax.plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
        ax.set_title('Freq. responce')
        ax.set_xlabel('Freq. (Hz)'), ax.set_ylabel('Gain')
        
        self.draw()

    def plot_grap_2(self, taps):
        ax = self.figure.add_subplot(111)

        ax.plot(taps, 'bo-', linewidth=2)
        ax.set_title('Filter coefficient %d' % len(taps))

        self.draw()

# -*- coding: utf-8 -*-

#git init
#git add *
#git commit -m "continue pyqt5 and first filters"
#git push origin master

import sys

from filters_config import Filter
from plotcanvas import PlotCanvas
from test_canvas_2 import ThreadSample, MatplotlibWidget

from gen_main import gen_main
from gen_tb import gen_tb

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QComboBox,
							QLineEdit, QInputDialog, QPushButton, QAction, QMainWindow)
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QIntValidator
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class MyWindow(QWidget):

	title = '¯\_(ツ)_/¯'
	width, height = 800, 600

	data_w, data_h, nyq_rate = 0, 0, 0 #plot figure and so on

	cutoff_freq_list = []
	fromFreq_var, toFreq_var = 0, 0
	filter_type, sample_freq, taps_num = 0, 0, 0


	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.resize(self.width, self.height)
		self.setWindowTitle(self.title)

		self.combo(self)
		self.sampleFreq(self)
		self.tapsNum(self)

		self.fromFreq(self)
		self.toFreq(self)

		self.generate_button(self)

		self.drawPlot(self)

		#self.show()


	def paintEvent(self, e):
		qp = QPainter()
		size = self.size()

		qp.begin(self)
		self.backgroundColor(qp, size)

		#if self.filter_type == 'Low-pass':
		#	print ('%s' % self.filter_type)

		#self.generate(size)
		#print (self.filter_type, self.samplef, self.tapsn)
		qp.end()


	def backgroundColor(self, qp, size):
		qp.setBrush(QColor(210, 210, 210))
		qp.drawRect(0, 0, size.width(), size.height())


	def sampleFreq(self, text):

		sample_freq = 0
		def on_click():
			self.sample_freq = float(self.samplef.text())
			self.samplef = self.sample_freq
			print (self.sample_freq)

		self.lbl = QLabel("Sampling freq.(Hz)", self)
		self.lbl.move(190, 12)

		self.samplef = QLineEdit(self)
		#self.le.setValidator(QIntValidator(1, 65536, self))
		self.samplef.move(190, 30)
		self.samplef.resize(125, 23)

		self.button = QPushButton('Set', self)
		self.button.move(320, 30)
		self.button.resize(40, 23)

		self.button.clicked.connect(on_click)
		#return sample_freq


	def tapsNum(self, text):

		def on_click():
			self.taps_num = int(self.num_taps.text())
			print (self.taps_num)

		self.lbl = QLabel("Numbers of taps", self)
		self.lbl.move(390, 12)

		self.num_taps = QLineEdit(self)
		self.num_taps.setValidator(QIntValidator(1, 40000, self))
		self.num_taps.move(390, 30)
		self.num_taps.resize(125, 23)

		self.button = QPushButton('Set', self)
		self.button.move(520, 30)
		self.button.resize(40, 23)

		self.button.clicked.connect(on_click)


	def toFreq(self, text):

		def on_click():
			self.toFreq_var = float(self.tofreq.text())
			print (self.toFreq_var)
			#self.cutoff_freq_list.append(self.taps.text())
			#print (self.cutoff_freq_list)

		self.lbl = QLabel("to Freq.", self)
		self.lbl.move(32, 130)

		self.tofreq = QLineEdit(self)
		self.tofreq.move(30, 148)
		self.tofreq.resize(125, 23)

		self.button = QPushButton('Set', self)
		self.button.move(160, 148)
		self.button.resize(40, 23)

		self.button.clicked.connect(on_click)


	def fromFreq(self, text):

		def on_click():
			self.fromFreq_var = float(self.fromfreq.text())
			print (self.fromFreq_var)
			#self.cutoff_freq_list.append(self.taps.text())
			#print (self.cutoff_freq_list)

		self.lbl = QLabel("from Freq.", self)
		self.lbl.move(32, 80)

		self.fromfreq = QLineEdit(self)
		self.fromfreq.move(30, 98)
		self.fromfreq.resize(125, 23)

		self.button = QPushButton('Set', self)
		self.button.move(160, 98)
		self.button.resize(40, 23)

		self.button.clicked.connect(on_click)


	def combo(self, text):

		self.lbl = QLabel("Choose type of filter", self)
		self.lbl.move(30, 12)

		def onActivated(text):
			self.filter_type = text
		
		combo = QComboBox(self)
		combo.addItems(["–", "Low-pass", "Band-pass", "High-pass"])
		combo.activated[str].connect(onActivated)
		combo.move(25, 30)


	def cutoff_low_pass(self):
		self.lbl = QLabel("Cutoff freq.(Hz)", self)
		self.lbl.move(30, 40)

		#self.cutoff_freq = QLineEdit(self)
		#self.cutoff_freq.setValidator(QIntValidator(1, 5000, self))
		#self.cutoff_freq.move()


	def click_generate_button(self, mode):
		if mode == 'Low-pass':
			low_pass_filter, self.data_w, self.data_h, self.nyq_rate = Filter().low_pass(
				self.sample_freq,
				self.taps_num,
				self.toFreq_var)

			tbFile = gen_tb(self.taps_num, low_pass_filter)

		elif mode == 'Band-pass':
			band_pass_filter, self.data_w, self.data_h, self.nyq_rate = Filter().band_pass(
				self.sample_freq,
				self.taps_num,
				self.fromFreq_var,
				self.toFreq_var)

			tbFile = gen_tb(self.taps_num, band_pass_filter)

		elif mode == 'High-pass':
			high_pass_filter, self.data_w, self.data_h, self.nyq_rate = Filter().high_pass(
				self.sample_freq,
				self.taps_num,
				self.fromFreq_var)

			tbFile = gen_tb(self.taps_num, high_pass_filter)


	def drawPlot(self, mode):

		return 0


	def generate_button(self, size):

		self.button = QPushButton('Generate!', self)
		self.button.move(465, 60)
		self.button.resize(100, 40)

		self.button.clicked.connect(lambda: self.click_generate_button(self.filter_type))
		self.button.clicked.connect(lambda: self.drawPlot('mode'))

		print (self.data_w, self.data_h, self.nyq_rate)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	ex = MyWindow()
	ex.show()
	
	sys.exit(app.exec_())

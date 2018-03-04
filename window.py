# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QComboBox,
							QLineEdit, QInputDialog, QPushButton, QAction)
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QIntValidator
from PyQt5.QtCore import Qt, pyqtSlot

class Example(QWidget):

	title = 'BURAN'
	width, height = 700, 500
	filter_type, samplef, tapsn = 0, 0, 0

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.resize(self.width, self.height)
		self.setWindowTitle(self.title)

		self.combo(self)
		self.sampleFreq(self)
		self.tapsNum(self)

		self.show()


	def paintEvent(self, e):
		qp = QPainter()
		size = self.size()

		qp.begin(self)
		self.backgroundColor(qp, size)
		#print (self.filter_type, self.samplef, self.tapsn)
		qp.end()


	def backgroundColor(self, qp, size):
		qp.setBrush(QColor(210, 210, 210))
		qp.drawRect(0, 0, size.width(), size.height())


	def sampleFreq(self, text):

		sample_freq = 0
		def on_click():
			sample_freq = self.samplef.text()
			self.samplef = sample_freq
			print (sample_freq)

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

		num_taps = 0
		def on_click():
			num_taps = self.taps.text()
			self.tapsn = num_taps
			print (num_taps)

		self.lbl = QLabel("Numbers of taps", self)
		self.lbl.move(390, 12)

		self.taps = QLineEdit(self)
		self.taps.setValidator(QIntValidator(1, 40000, self))
		self.taps.move(390, 30)
		self.taps.resize(125, 23)

		self.button = QPushButton('Set', self)
		self.button.move(520, 30)
		self.button.resize(40, 23)

		self.button.clicked.connect(on_click)


	def combo(self, text):

		self.lbl = QLabel("Choose type of filter", self)
		self.lbl.move(30, 12)

		def onActivated(text):
			filter_type = text
			print (text)
		
		combo = QComboBox(self)
		combo.addItems(["Low-pass", "Band-pass", "High-pass"])
		combo.activated[str].connect(onActivated)
		combo.move(25, 30)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

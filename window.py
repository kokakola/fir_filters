# -*- coding: utf-8 -*-

import sys
import os

import time
import datetime

from filters_config import Filter
from test_canvas import PlotCanvas
from gen_main import gen_main
from gen_tb import gen_tb

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

	title = '¯\_(ツ)_/¯'
	width, height = 900, 600

	filter_type = ''
	console_log = 	(str('%s' % (datetime.datetime.now().strftime('%H:%M:%S'))) + 
					' | Start program\n')

	sampleFreq, tapsNum, fromFreq, toFreq = 0, 0, 0, 0
	data_w, data_h, nyq_rate = 0, 0, 0
	text_in_tab = 'text text'
	text_verilog_rtl, text_verilog_tb = '', ''


	def setupUi(self, MainWindow):

		MainWindow.setObjectName("MainWindow")
		MainWindow.setWindowTitle(self.title)
		MainWindow.resize(self.width, self.height)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")

		self.gridLayout_4 = QtWidgets.QGridLayout()
		self.gridLayout_4.setHorizontalSpacing(3)
		self.gridLayout_4.setVerticalSpacing(6)
		self.gridLayout_4.setObjectName("gridLayout_4")

		self.label_sampling_freq = QtWidgets.QLabel('Sampling freq.(Hz)', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_sampling_freq.sizePolicy().hasHeightForWidth())
		self.label_sampling_freq.setSizePolicy(sizePolicy)
		self.label_sampling_freq.setObjectName("label_sampling_freq")
		self.gridLayout_4.addWidget(self.label_sampling_freq, 1, 0, 1, 1)

		self.label_taps_number = QtWidgets.QLabel('Taps numbers', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_taps_number.sizePolicy().hasHeightForWidth())
		self.label_taps_number.setSizePolicy(sizePolicy)
		self.label_taps_number.setObjectName("label_taps_number")
		self.gridLayout_4.addWidget(self.label_taps_number, 2, 0, 1, 1)

		self.lineEdit_sample_freq = QtWidgets.QLineEdit('0', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_sample_freq.sizePolicy().hasHeightForWidth())
		self.lineEdit_sample_freq.setSizePolicy(sizePolicy)
		self.lineEdit_sample_freq.setObjectName("lineEdit_sample_freq")
		self.gridLayout_4.addWidget(self.lineEdit_sample_freq, 1, 1, 1, 1)

		self.lineEdit_to_freq = QtWidgets.QLineEdit('0', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_to_freq.sizePolicy().hasHeightForWidth())
		self.lineEdit_to_freq.setSizePolicy(sizePolicy)
		self.lineEdit_to_freq.setObjectName("lineEdit_to_freq")
		self.gridLayout_4.addWidget(self.lineEdit_to_freq, 4, 1, 1, 1)

		self.lineEdit_from_freq = QtWidgets.QLineEdit('0', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_from_freq.sizePolicy().hasHeightForWidth())
		self.lineEdit_from_freq.setSizePolicy(sizePolicy)
		self.lineEdit_from_freq.setObjectName("lineEdit_from_freq")
		self.gridLayout_4.addWidget(self.lineEdit_from_freq, 3, 1, 1, 1)

		self.label_from_freq = QtWidgets.QLabel('from Freq.', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_from_freq.sizePolicy().hasHeightForWidth())
		self.label_from_freq.setSizePolicy(sizePolicy)
		self.label_from_freq.setObjectName("label_from_freq")
		self.gridLayout_4.addWidget(self.label_from_freq, 3, 0, 1, 1)

		self.pushButton_generate = QtWidgets.QPushButton('Generate', self.centralwidget)
		self.pushButton_generate.setObjectName("pushButton_generate")
		self.gridLayout_4.addWidget(self.pushButton_generate, 5, 1, 1, 1)

		self.label_to_freq = QtWidgets.QLabel('to Freq.', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_to_freq.sizePolicy().hasHeightForWidth())
		self.label_to_freq.setSizePolicy(sizePolicy)
		self.label_to_freq.setObjectName("label_to_freq")
		self.gridLayout_4.addWidget(self.label_to_freq, 4, 0, 1, 1)

		self.lineEdit_taps_number = QtWidgets.QLineEdit('0', self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_taps_number.sizePolicy().hasHeightForWidth())
		self.lineEdit_taps_number.setSizePolicy(sizePolicy)
		self.lineEdit_taps_number.setObjectName("lineEdit_taps_number")
		self.gridLayout_4.addWidget(self.lineEdit_taps_number, 2, 1, 1, 1)

		self.type_of_filter = QtWidgets.QComboBox(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.type_of_filter.sizePolicy().hasHeightForWidth())
		self.type_of_filter.setSizePolicy(sizePolicy)
		self.type_of_filter.setObjectName("type_of_filter")
		self.type_of_filter.addItems(["", "Low-pass", "Band-pass", "High-pass"])

		self.gridLayout_4.addWidget(self.type_of_filter, 0, 0, 1, 1)
		self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
		self.gridLayout_3 = QtWidgets.QGridLayout()
		self.gridLayout_3.setContentsMargins(7, -1, 7, -1)
		self.gridLayout_3.setObjectName("gridLayout_3")

		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
		self.tabWidget.setSizePolicy(sizePolicy)
		self.tabWidget.setMinimumSize(QtCore.QSize(530, 0))
		self.tabWidget.setStyleSheet("")
		self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
		self.tabWidget.setObjectName("tabWidget")

		self.grap1 = QtWidgets.QWidget()
		self.grap1.setObjectName("grap1")
		self.tabWidget.addTab(self.grap1, "График 1")
		self.graphic_in_tab_1 = PlotCanvas()
		self.label_in_tab_1 = QtWidgets.QLabel(self.text_in_tab)
		layout_123 = QtWidgets.QHBoxLayout()
		layout_123.addWidget(self.graphic_in_tab_1)
		self.grap1.setLayout(layout_123)

		self.grap2 = QtWidgets.QWidget()
		self.grap2.setObjectName("grap2")
		self.tabWidget.addTab(self.grap2, "График 2")
		self.graphic_in_tab_2 = PlotCanvas()
		layout_tab_2 = QtWidgets.QHBoxLayout()
		layout_tab_2.addWidget(self.graphic_in_tab_2)
		self.grap2.setLayout(layout_tab_2)

		self.textEditorRTL = QtWidgets.QTextEdit()
		self.grap_editor = QtWidgets.QWidget()
		self.grap_editor.setObjectName("grap_editor")
		self.tabWidget.addTab(self.grap_editor, "RTL")
		layout_tab_editor = QtWidgets.QHBoxLayout()
		layout_tab_editor.addWidget(self.textEditorRTL)
		self.grap_editor.setLayout(layout_tab_editor)

		self.textEditorTestBench = QtWidgets.QTextEdit()
		self.edit_tb = QtWidgets.QWidget()
		self.edit_tb.setObjectName("testbench_editor")
		self.tabWidget.addTab(self.edit_tb, "TestBench")
		layout_tab_edit_tb = QtWidgets.QHBoxLayout()
		layout_tab_edit_tb.addWidget(self.textEditorTestBench)
		self.edit_tb.setLayout(layout_tab_edit_tb)

		self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
		self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 2, 1)
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setContentsMargins(7, 7, 7, 7)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.tabWidget.setCurrentIndex(0)

		self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
		self.scrollArea.setSizePolicy(sizePolicy)
		self.scrollArea.setMinimumSize(QtCore.QSize(0, 120))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")

		self.scrollAreaWidgetContents_2 = QtWidgets.QLabel()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 793, 118))
		self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
		self.scrollAreaWidgetContents_2.setText(self.console_log)

		self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
		self.verticalLayout_3.addWidget(self.scrollArea)
		self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 2)

		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)

		self.pushButton_set = QtWidgets.QPushButton('Set', self.centralwidget)
		self.pushButton_set.setObjectName("pushButton_set")
		self.gridLayout_4.addWidget(self.pushButton_set, 5, 0, 1, 1)

		def on_set_click():

			self.sampleFreq = float(self.lineEdit_sample_freq.text())
			self.tapsNum = int(self.lineEdit_taps_number.text())

			if self.filter_type == 'Low-pass':
				self.toFreq = float(self.lineEdit_to_freq.text())

			elif self.filter_type == 'High-pass':
				self.fromFreq = float(self.lineEdit_from_freq.text())

			elif self.filter_type == 'Band-pass':
				self.fromFreq = float(self.lineEdit_from_freq.text())
				self.toFreq = float(self.lineEdit_to_freq.text())

			#self.fromFreq = float(self.lineEdit_from_freq.text())
			#self.toFreq = float(self.lineEdit_to_freq.text())

			print ('set click')

		self.pushButton_set.clicked.connect(on_set_click)

		def on_generate_click():

			if self.filter_type == 'Low-pass':

				#print (self.sampleFreq, self.tapsNum, self.fromFreq, self.toFreq)

				low_pass_filter, self.data_w, self.data_h, self.nyq_rate, taps_numbers = Filter().low_pass(
					self.sampleFreq,
					self.tapsNum,
					self.toFreq)

				self.graphic_in_tab_1.plot_grap_1(self.data_w, self.data_h, self.nyq_rate)
				self.graphic_in_tab_2.plot_grap_2(taps_numbers)

				tbFile = gen_tb(self.tapsNum, low_pass_filter)
				self.textEditorTestBench.setText(tbFile.returnText())

				rtlFile = gen_main()
				self.textEditorRTL.setText(rtlFile.returnText())

				#print (low_pass_filter)

			elif self.filter_type == 'Band-pass':

				#print (self.sampleFreq, self.tapsNum, self.fromFreq, self.toFreq)

				band_pass_filter, self.data_w, self.data_h, self.nyq_rate, taps_numbers = Filter().band_pass(
					self.sampleFreq,
					self.tapsNum,
					self.fromFreq,
					self.toFreq)

				self.graphic_in_tab_1.plot_grap_1(self.data_w, self.data_h, self.nyq_rate)
				self.graphic_in_tab_2.plot_grap_2(taps_numbers)

				tbFile = gen_tb(self.tapsNum, band_pass_filter)
				self.textEditorTestBench.setText(tbFile.returnText())

				rtlFile = gen_main()
				self.textEditorRTL.setText(rtlFile.returnText())

				#print (band_pass_filter)

			elif self.filter_type == 'High-pass':

				#print (self.sampleFreq, self.tapsNum, self.fromFreq, self.toFreq)

				high_pass_filter, self.data_w, self.data_h, self.nyq_rate, taps_numbers = Filter().high_pass(
					self.sampleFreq,
					self.tapsNum,
					self.fromFreq)

				self.graphic_in_tab_1.plot_grap_1(self.data_w, self.data_h, self.nyq_rate)
				self.graphic_in_tab_2.plot_grap_2(taps_numbers)

				tbFile = gen_tb(self.tapsNum, high_pass_filter)
				self.textEditorTestBench.setText(tbFile.returnText())

				rtlFile = gen_main()
				self.textEditorRTL.setText(rtlFile.returnText())

				#print (high_pass_filter)

			print ('generate click')

		self.pushButton_generate.clicked.connect(on_generate_click)

		def onActivated(text):
			self.filter_type = text
			self.console_log += (str('{:>10}'.format('%s' % (datetime.datetime.now().strftime('%H:%M:%S')))) +
								str('{:>10}'.format('%s' % str('| Choose type of filter: ' + self.filter_type + '\n'))))
			
			print ('choose filter')
			
			if self.filter_type == 'Low-pass':
				self.lineEdit_from_freq.setText('минимум')
				self.lineEdit_to_freq.setText('0')

				self.lineEdit_from_freq.setReadOnly(True)
				self.lineEdit_to_freq.setReadOnly(False)

			elif self.filter_type == 'High-pass':
				self.lineEdit_from_freq.setText('0')
				self.lineEdit_to_freq.setText('максимум')

				self.lineEdit_from_freq.setReadOnly(False)
				self.lineEdit_to_freq.setReadOnly(True)

			elif self.filter_type == 'Band-pass':
				self.lineEdit_from_freq.setText('0')
				self.lineEdit_to_freq.setText('0')

				self.lineEdit_from_freq.setReadOnly(False)
				self.lineEdit_to_freq.setReadOnly(False)


			self.scrollAreaWidgetContents_2.setText(self.console_log)
			self.scrollArea.verticalScrollBar().setSliderPosition(self.scrollArea.verticalScrollBar().maximum())	

		self.type_of_filter.activated[str].connect(onActivated)

		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

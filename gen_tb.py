# -*- coding: utf-8 -*-

import datetime
import getpass

from time import strftime

class gen_tb:
	def __init__(self):
		self.fileName = 'test_file_tb.v'
		self.newFile()

	#описание к файлу
	def startDesc(self, f):
		f.write('//\n// Description of \"%s\"' % self.fileName)
		f.write('\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S'))
		f.write('\n// Author: %s\n//\n' % getpass.getuser())
		f.write('\n`timescale 1ns / 1ns\n\n')

	#описание модуля
	def moduleDesc(self, f):
		f.write('module %s ();\n\n' % self.fileName[:-2])

	#описание клока
	def clockDesc(self, f, startTime, periodTime):
		clkName = 'tb_clk'
		f.write('reg %s;\ninitial %s = %d;\n' % (clkName, clkName, startTime))
		f.write('always\n\t#%d %s = ~%s;\n\n' % (periodTime, clkName, clkName))

	#описание переменных
	def variableDesc(self, f, last_time, current_time, angle, freq):
		f.write('real PI=3.14159265358979323846;\n')
		f.write('real last_time = %d;\n' % last_time)	#sec
		f.write('real current_time = %d;\n' % current_time)	#sec
		f.write('real angle = %d;\n' % angle)	#sec
		f.write('real frequency = %d;\n' % freq)
		f.write('integer freq_x100kHz = %d;\n' % 0)
		f.write('reg signed [15:0]sin16;\n')	#TODO

	def funcSin(self, f):
		y, y3, y5, y7 = 1.570794, 0.645962, 0.079692, 0.004681712

		f.write('\nfunction real sin;\ninput x;\nreal x;\n')
		f.write('real x, y, y2, y3, y5, y7, sum, sign;\n')
		f.write('\tbegin\n\t\tsign = %.1f;\n\t\tx1 = x;\n' % 1)
		f.write('\t\tif (x1<0)\n\t\tbegin\n\t\t\tx1 = -x1;\n')
		f.write('\t\t\tsign = %.1f;\n\t\tend\n' % -1)
		f.write('\t\twhile (x1 > PI/2.0)\n\t\tbegin\n')
		f.write('\t\t\tx1 = x1 - PI;\n\t\t\tsign = %.1f*sign;\n\t\tend\n' % -1)
		f.write('\t\ty = x1*2/PI;\n\t\ty2 = y*y;\n\t\ty3 = y*y2;\n')
		f.write('\t\ty5 = y3*y2;\n\t\ty7 = y5*y2;\n')
		f.write('\t\tsum = %.6f*%s - %.6f*%s + %.6f*%s - %.9f*%s;\n' % 
			(y, 'y', y3, 'y3', y5, 'y5', y7, 'y7'))
		f.write('\t\tsin = sign*sum;\n')
		f.write('\tend\nendfunction\n')

	#главный метод с вызовом остальных методов
	def newFile(self):
		f = open(self.fileName, 'w')
		self.startDesc(f)
		self.moduleDesc(f)
		self.clockDesc(f, 0, 25)
		self.variableDesc(f, 0, 0, 0, 100)
		self.funcSin(f)
		f.close()

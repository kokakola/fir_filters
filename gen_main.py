# -*- coding: utf-8 -*-

import datetime
import getpass

from time import strftime

class gen_main:
	def __init__(self):
		self.fileName = 'test_file.v'
		self.newFile()

	#описание к файлу
	def startDesc(self, f):
		f.write('//\n// Description of \"%s\"' % self.fileName)
		f.write('\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S'))
		f.write('\n// Author: %s\n//\n\n' % getpass.getuser())

	#описание модуля
	def moduleDesc(self, f):
		f.write('module %s (\n\tclk,\n\tcoefs,\n\tin,\n\tout\n);\n' % self.fileName[:-2])

	#описание параметров
	def paramDesc(self ,f):
		p, l = 'parameter', 'localparam'
		f.write('\n%s IWIDTH = %d;\n' % (p, 16))
		f.write('%s CWIDTH = %d;\n' % (p, 16))
		f.write('%s TAPS = %d;\n' % (p, 2))
		f.write('%s MWIDTH = (IWIDTH+CWIDTH);\n' % l)
		f.write('%s RWIDTH = (MWIDTH+TAPS-1);\n' % l)

	def generDesc(self, f):
		f.write('\ngenvar i;\ngenerate\n')
		f.write('\tfor(i=0; i<TAPS; i=i+1)\n')
		f.write('\tbegin:tap\n\t\treg [IWIDTH-1:0] r=0;\n')

		f.write('\t\tif(i==0)\n\t\tbegin\n\t\t\talways @(posedge clk)\n')
		f.write('\t\t\tr <= in;\n\t\tend\n\t\telse\n\t\tbegin\n')
		f.write('\t\t\talways @(posedge clk)\n\t\t\t\ttap[i].r <= tap[i-1].r;\n')
		f.write('\t\tend\n\n\t\twire [CWIDTH-1:0]c;\n')
		f.write('\t\tassign c = coefs[((TAPS-1-i)*%d+CWIDTH-1):(TAPS-1-i)*%d];\n' % (32, 8))
		f.write('\n\t\treg[MWIDTH-1:0]m;\n\t\talways @(posedge clk)\n')
		f.write('\t\t\tm <= $signed(r) * $signed(c);\n')
		f.write('\n\t\treg [MWIDTH-1+i:0]a;\n')

		f.write('\t\tif(i==0)\n\t\tbegin\n\t\t\talways @*\n')
		f.write('\t\t\t\ttap[i].a = $signed(tap[i].m);\n\t\tend')
		f.write('\t\telse\n\t\tbegin\n\t\t\talways @*\n')
		f.write('\t\t\t\ttap[i].a = $signed(tap[i].m) + $signed(tap[i-1].a);\n')
		f.write('\t\tend\n\tend\nendgenerate\n')

	def resultDesc(self, f):
		f.write('\nreg [RWIDTH-1:0]result;\n')
		f.write('always @(posedge clk)\n\tresult <= tap[TAPS-1].a;\n')
		f.write('\nassign out = result;\n')
		f.write('\nendmodule\n')

	#главный метод с вызовом остальных методов
	def newFile(self):
		f = open(self.fileName, 'w')
		self.startDesc(f)
		self.moduleDesc(f)
		self.paramDesc(f)
		self.generDesc(f)
		self.resultDesc(f)
		f.close()

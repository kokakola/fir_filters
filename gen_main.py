# -*- coding: utf-8 -*-

import re
import datetime
import getpass

from time import strftime

class gen_main:

	main_text = ''
	import_text = ''

	def __init__(self):
		self.fileName = 'test_file.v'


	def startDesc(self):

		self.main_text += (('//\n// Description of \"%s\"' % self.fileName) +
							('\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S')) +
							('\n// Author: %s\n//\n\n' % getpass.getuser()))


	def moduleDesc(self):
		#f.write('module %s (\n\tclk,\n\tcoefs,\n\tin,\n\tout\n);\n' % self.fileName[:-2])

		self.main_text += 'module %s (\n\tclk,\n\tcoefs,\n\tin,\n\tout\n);\n' % self.fileName[:-2]


	def paramDesc(self):
		p, l = 'parameter', 'localparam'

		self.main_text += '\n%s IWIDTH = %d;\n' % (p, 16) + \
						'%s CWIDTH = %d;\n' % (p, 16) + '%s TAPS = %d;\n' % (p, 2) + \
						'%s MWIDTH = (IWIDTH+CWIDTH);\n' % l + \
						'%s RWIDTH = (MWIDTH+TAPS-1);\n' % l


	def generDesc(self):

		self.main_text += '\ngenvar i;\ngenerate\n' + \
						'\tfor(i=0; i<TAPS; i=i+1)\n' + \
						'\tbegin:tap\n\t\treg [IWIDTH-1:0] r=0;\n'


		self.main_text += '\t\tif(i==0)\n\t\tbegin\n\t\t\talways @(posedge clk)\n' + \
						'\t\t\tr <= in;\n\t\tend\n\t\telse\n\t\tbegin\n' + \
						'\t\t\talways @(posedge clk)\n\t\t\t\ttap[i].r <= tap[i-1].r;\n' + \
						'\t\tend\n\n\t\twire [CWIDTH-1:0]c;\n' + \
						'\t\tassign c = coefs[((TAPS-1-i)*%d+CWIDTH-1):(TAPS-1-i)*%d];\n' % (32, 8) + \
						'\n\t\treg[MWIDTH-1:0]m;\n\t\talways @(posedge clk)\n' + \
						'\t\t\tm <= $signed(r) * $signed(c);\n' + \
						'\n\t\treg [MWIDTH-1+i:0]a;\n'


		self.main_text += '\t\tif(i==0)\n\t\tbegin\n\t\t\talways @*\n' + \
						'\t\t\t\ttap[i].a = $signed(tap[i].m);\n\t\tend' + \
						'\t\telse\n\t\tbegin\n\t\t\talways @*\n' + \
						'\t\t\t\ttap[i].a = $signed(tap[i].m) + $signed(tap[i-1].a);\n' + \
						'\t\tend\n\tend\nendgenerate\n'


	def resultDesc(self):

		self.main_text += '\nreg [RWIDTH-1:0]result;\n' + \
						'always @(posedge clk)\n\tresult <= tap[TAPS-1].a;\n' + \
						'\nassign out = result;\n' + '\nendmodule\n'


	def newFile(self):

		self.startDesc()
		self.moduleDesc()
		self.paramDesc()
		self.generDesc()
		self.resultDesc()


	def saveFile(self):
		f = open(self.fileName, 'w')
		if self.import_text != '':
			f.write(self.main_text)
		else:
			f.write(self.import_text)
		f.close()


	def resetText(self):
		self.main_text = ''
		return self.main_text


	def readFile(self, directory):

		f = open(directory, 'r')
		for i in f:
			self.import_text += i


	def returnImportText(self):
		return self.import_text


	def returnText(self):
		self.main_text = re.sub('\t', '    ', self.main_text)
		return self.main_text

# -*- coding: utf-8 -*-

import re
import datetime
import getpass

from time import strftime

class gen_main:

	main_text = ''

	def __init__(self):
		self.fileName = 'test_file.v'


	def startDesc(self):
		#f.write('//\n// Description of \"%s\"' % self.fileName)
		#f.write('\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S'))
		#f.write('\n// Author: %s\n//\n\n' % getpass.getuser())

		self.main_text += (('//\n// Description of \"%s\"' % self.fileName) +
							('\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S')) +
							('\n// Author: %s\n//\n\n' % getpass.getuser()))


	def moduleDesc(self):
		#f.write('module %s (\n\tclk,\n\tcoefs,\n\tin,\n\tout\n);\n' % self.fileName[:-2])

		self.main_text += 'module %s (\n\tclk,\n\tcoefs,\n\tin,\n\tout\n);\n' % self.fileName[:-2]


	def paramDesc(self):
		p, l = 'parameter', 'localparam'
		#f.write('\n%s IWIDTH = %d;\n' % (p, 16))
		#f.write('%s CWIDTH = %d;\n' % (p, 16))
		#f.write('%s TAPS = %d;\n' % (p, 2))
		#f.write('%s MWIDTH = (IWIDTH+CWIDTH);\n' % l)
		#f.write('%s RWIDTH = (MWIDTH+TAPS-1);\n' % l)

		self.main_text += '\n%s IWIDTH = %d;\n' % (p, 16) + \
						'%s CWIDTH = %d;\n' % (p, 16) + '%s TAPS = %d;\n' % (p, 2) + \
						'%s MWIDTH = (IWIDTH+CWIDTH);\n' % l + \
						'%s RWIDTH = (MWIDTH+TAPS-1);\n' % l


	def generDesc(self):
		#f.write('\ngenvar i;\ngenerate\n')
		#f.write('\tfor(i=0; i<TAPS; i=i+1)\n')
		#f.write('\tbegin:tap\n\t\treg [IWIDTH-1:0] r=0;\n')

		self.main_text += '\ngenvar i;\ngenerate\n' + \
						'\tfor(i=0; i<TAPS; i=i+1)\n' + \
						'\tbegin:tap\n\t\treg [IWIDTH-1:0] r=0;\n'

		#f.write('\t\tif(i==0)\n\t\tbegin\n\t\t\talways @(posedge clk)\n')
		#f.write('\t\t\tr <= in;\n\t\tend\n\t\telse\n\t\tbegin\n')
		#f.write('\t\t\talways @(posedge clk)\n\t\t\t\ttap[i].r <= tap[i-1].r;\n')
		#f.write('\t\tend\n\n\t\twire [CWIDTH-1:0]c;\n')
		#f.write('\t\tassign c = coefs[((TAPS-1-i)*%d+CWIDTH-1):(TAPS-1-i)*%d];\n' % (32, 8))
		#f.write('\n\t\treg[MWIDTH-1:0]m;\n\t\talways @(posedge clk)\n')
		#f.write('\t\t\tm <= $signed(r) * $signed(c);\n')
		#f.write('\n\t\treg [MWIDTH-1+i:0]a;\n')

		self.main_text += '\t\tif(i==0)\n\t\tbegin\n\t\t\talways @(posedge clk)\n' + \
						'\t\t\tr <= in;\n\t\tend\n\t\telse\n\t\tbegin\n' + \
						'\t\t\talways @(posedge clk)\n\t\t\t\ttap[i].r <= tap[i-1].r;\n' + \
						'\t\tend\n\n\t\twire [CWIDTH-1:0]c;\n' + \
						'\t\tassign c = coefs[((TAPS-1-i)*%d+CWIDTH-1):(TAPS-1-i)*%d];\n' % (32, 8) + \
						'\n\t\treg[MWIDTH-1:0]m;\n\t\talways @(posedge clk)\n' + \
						'\t\t\tm <= $signed(r) * $signed(c);\n' + \
						'\n\t\treg [MWIDTH-1+i:0]a;\n'

		#f.write('\t\tif(i==0)\n\t\tbegin\n\t\t\talways @*\n')
		#f.write('\t\t\t\ttap[i].a = $signed(tap[i].m);\n\t\tend')
		#f.write('\t\telse\n\t\tbegin\n\t\t\talways @*\n')
		#f.write('\t\t\t\ttap[i].a = $signed(tap[i].m) + $signed(tap[i-1].a);\n')
		#f.write('\t\tend\n\tend\nendgenerate\n')

		self.main_text += '\t\tif(i==0)\n\t\tbegin\n\t\t\talways @*\n' + \
						'\t\t\t\ttap[i].a = $signed(tap[i].m);\n\t\tend' + \
						'\t\telse\n\t\tbegin\n\t\t\talways @*\n' + \
						'\t\t\t\ttap[i].a = $signed(tap[i].m) + $signed(tap[i-1].a);\n' + \
						'\t\tend\n\tend\nendgenerate\n'


	def resultDesc(self):
		#f.write('\nreg [RWIDTH-1:0]result;\n')
		#f.write('always @(posedge clk)\n\tresult <= tap[TAPS-1].a;\n')
		#f.write('\nassign out = result;\n')
		#f.write('\nendmodule\n')

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
		f.write(self.main_text)
		f.close()


	def returnText(self):
		self.main_text = re.sub('\t', '    ', self.main_text)
		return self.main_text

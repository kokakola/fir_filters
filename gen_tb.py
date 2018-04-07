# -*- coding: utf-8 -*-

import re
import datetime
import getpass

from time import strftime

class gen_tb:

	clkName = 'tb_clk'
	set_freq = 'set_freq'
	main_text = ''

	def __init__(self):
		self.fileName = 'test_file_tb.v'

	def genFile(self, taps_num, taps_list):
		self.taps_num = taps_num
		self.taps_list = taps_list
		self.newFile()


	#описание к файлу
	def startDesc(self):
		#f.write('//\n// Description of \"%s\"' % self.fileName)
		#f.write('\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S'))
		#f.write('\n// Author: %s\n//\n' % getpass.getuser())
		#f.write('\n`timescale 1ns / 1ns\n\n')

		self.main_text += '//\n// Description of \"%s\"' % self.fileName + \
					'\n// Date: %s' % datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S') + \
					'\n// Author: %s\n//\n' % getpass.getuser() + \
					'\n`timescale 1ns / 1ns\n\n'

		#f.write(self.main_text)


	#описание модуля
	def moduleDesc(self):
		#f.write('module %s ();\n\n' % self.fileName[:-2])

		self.main_text += 'module %s ();\n\n' % self.fileName[:-2]


	#описание клока
	def clockDesc(self, startTime, periodTime):
		#f.write('reg %s;\ninitial %s = %d;\n' % (self.clkName, self.clkName, startTime))
		#f.write('always\n\t#%d %s = ~%s;\n\n' % (periodTime, self.clkName, self.clkName))

		self.main_text += 'reg %s;\ninitial %s = %d;\n' % (self.clkName, self.clkName, startTime) + \
						'always\n\t#%d %s = ~%s;\n\n' % (periodTime, self.clkName, self.clkName)


	#описание переменных
	def variableDesc(self, last_time, current_time, angle, freq):
		#f.write('real PI=3.14159265358979323846;\n')
		#f.write('real last_time = %d;\n' % last_time)	#sec
		#f.write('real current_time = %d;\n' % current_time)	#sec
		#f.write('real angle = %d;\n' % angle)	#sec
		#f.write('real frequency = %d;\n' % freq)
		#f.write('integer freq_x100kHz = %d;\n' % 0)
		#f.write('reg signed [15:0]sin16;\n')	#TODO

		self.main_text += 'real PI=3.14159265358979323846;\n' + \
						'real last_time = %d;\n' % last_time + \
						'real current_time = %d;\n' % current_time + \
						'real angle = %d;\n' % angle + \
						'real frequency = %d;\n' % freq + \
						'integer freq_x100kHz = %d;\n' % 0 + \
						'reg signed [15:0]sin16;\n'


	def funcSin(self):
		y, y3, y5, y7 = 1.570794, 0.645962, 0.079692, 0.004681712

		#f.write('\nfunction real sin;\ninput x;\nreal x;\n')
		#f.write('real x, y, y2, y3, y5, y7, sum, sign;\n')
		#f.write('\tbegin\n\t\tsign = %.1f;\n\t\tx1 = x;\n' % 1)
		#f.write('\t\tif (x1<0)\n\t\tbegin\n\t\t\tx1 = -x1;\n')
		#f.write('\t\t\tsign = %.1f;\n\t\tend\n' % -1)
		#f.write('\t\twhile (x1 > PI/2.0)\n\t\tbegin\n')
		#f.write('\t\t\tx1 = x1 - PI;\n\t\t\tsign = %.1f*sign;\n\t\tend\n' % -1)
		#f.write('\t\ty = x1*2/PI;\n\t\ty2 = y*y;\n\t\ty3 = y*y2;\n')
		#f.write('\t\ty5 = y3*y2;\n\t\ty7 = y5*y2;\n')
		#f.write('\t\tsum = %.6f*%s - %.6f*%s + %.6f*%s - %.9f*%s;\n' % 
		#	(y, 'y', y3, 'y3', y5, 'y5', y7, 'y7'))
		#f.write('\t\tsin = sign*sum;\n')
		#f.write('\tend\nendfunction\n')

		self.main_text += '\nfunction real sin;\ninput x;\nreal x;\n' + \
						'real x, y, y2, y3, y5, y7, sum, sign;\n' + \
						'\tbegin\n\t\tsign = %.1f;\n\t\tx1 = x;\n' % 1 + \
						'\t\tif (x1<0)\n\t\tbegin\n\t\t\tx1 = -x1;\n' + \
						'\t\t\tsign = %.1f;\n\t\tend\n' % -1 + \
						'\t\twhile (x1 > PI/2.0)\n\t\tbegin\n' + \
						'\t\t\tx1 = x1 - PI;\n\t\t\tsign = %.1f*sign;\n\t\tend\n' + \
						'\t\ty = x1*2/PI;\n\t\ty2 = y*y;\n\t\ty3 = y*y2;\n' + \
						'\t\ty5 = y3*y2;\n\t\ty7 = y5*y2;\n' + \
						'\t\tsum = %.6f*%s - %.6f*%s + %.6f*%s - %.9f*%s;\n' % (y, 'y', y3, 'y3', y5, 'y5', y7, 'y7') + \
						'\t\tsin = sign*sum;\n' + \
						'\tend\nendfunction\n'


	def setFreq(self, freq):
		#f.write('\ntask %s;\n' % self.set_freq)
		#f.write('input f;\n')
		#f.write('real f;\n')
		#f.write('begin\n')
		#f.write('\tfrequency = f;\n')
		#f.write('\tfreq_x100kHz = f / %s;\n' % str(freq))
		#f.write('end\n')

		self.main_text += '\ntask %s;\n' % self.set_freq + \
						'input f;\n' + 'real f;\n' + 'begin\n' + \
						'\tfrequency = f;\n' + \
						'\tfreq_x100kHz = f / %s;\n' % str(freq) + 'end\n'


	def posedgeClk(self):
		#f.write('\nalways @(posedge tb_clk)\n')
		#f.write('begin\n')
		#f.write('\tcurrent_time = $realtime;\n')

		#f.write('\tangle = angle + (current_time-last_time)')
		#f.write('*2*PI*frequency / %s;\n' % str(1000000000.0))

		#f.write('\twhile (angle > PI*2.0)\n')
		#f.write('\tbegin\n')
		#f.write('\t\tangle = angle - PI*2.0;\n')
		#f.write('\tend\n')
		#f.write('\tsin16 = 32000 * sin(angle);\n')
		#f.write('\tlast_time = cuttent_time;\n')
		#f.write('end\n')

		self.main_text += '\nalways @(posedge tb_clk)\n' + 'begin\n' + \
						'\tcurrent_time = $realtime;\n' + \
						'\tangle = angle + (current_time-last_time)' + \
						'*2*PI*frequency / %s;\n' % str(1000000000.0) + \
						'\twhile (angle > PI*2.0)\n' + \
						'\tbegin\n' + '\t\tangle = angle - PI*2.0;\n' + \
						'\tend\n' + '\tsin16 = 32000 * sin(angle);\n' + \
						'\tlast_time = cuttent_time;\n' + 'end\n'


	def filterDesc(self, taps_num, taps_list):
		out_name = 'out_lowpass'
		num_taps = taps_num
		dimension = 57

		#f.write('\nwire [%s:0]%s;\n' % (str(dimension), out_name))
		#f.write('fir #( .TAPS(%s)) fir_inst(\n' % num_taps)
		#f.write('\t.clk(%s),\n' % self.clkName)

		self.main_text += '\nwire [%s:0]%s;\n' % (str(dimension), out_name) + \
						'fir #( .TAPS(%s)) fir_inst(\n' % num_taps + \
						'\t.clk(%s),\n' % self.clkName

		#f.write('\t.coefs( {\n')

		self.main_text += '\t.coefs( {\n'

		#TODO: last item (,\n -> \n)
		for i in range(len(taps_list)):
			#f.write('\t\t')
			self.main_text += '\t\t'
			if taps_list[i]>0:
				#f.write('32\'d%s' % str(abs(taps_list[i])) + ',\n')
				self.main_text += '32\'d%s' % str(abs(taps_list[i])) + ',\n'
			elif taps_list[i]<0:
				#f.write('-32\'d%s' % str(abs(taps_list[i])) + ',\n')
				self.main_text += '-32\'d%s' % str(abs(taps_list[i])) + ',\n'
			else:
				#f.write('32\'d0,\n')
				self.main_text += '32\'d0,\n'

		#f.write('\t\t} ),\n')
		self.main_text += '\t\t} ),\n'

		#f.write('\t.in(sin16),\n')
		#f.write('\t.out(%s)\n' % out_name)
		#f.write('\t);\n')

		self.main_text += '\t.in(sin16),\n' + \
						'\t.out(%s)\n' % out_name + \
						'\t);\n'


	def dumpFile(self):
		#f.write('\ninteger i;\n')
		#f.write('real f;\n')
		#f.write('\ninitial\nbegin\n')

		#f.write('\t$dumpfile("%s");\n' % 'out.vcd')
		#f.write('\t$dumpvars(0, testbench);\n')
		#f.write('\tf = 100000;\n')
		#f.write('\tfor (i=0; i<%s; i=i+1)' % str(4000))

		#f.write('\tbegin\n')
		#f.write('\t\t%s(f);\n' % self.set_freq)
		#f.write('\t\t#1000;\n')
		#f.write('\t\tf = f + 1000;\n')
		#f.write('\tend\n')
		#f.write('\t$finish;\n')

		#f.write('end\n')

		#f.write('\nendmodule\n')

		self.main_text += '\ninteger i;\n' + 'real f;\n' + '\ninitial\nbegin\n' + \
						'\t$dumpfile("%s");\n' % 'out.vcd' + \
						'\t$dumpvars(0, testbench);\n' + '\tf = 100000;\n' + \
						'\tfor (i=0; i<%s; i=i+1)' % str(4000) + '\tbegin\n' + \
						'\t\t%s(f);\n' % self.set_freq + '\t\t#1000;\n' + \
						'\t\tf = f + 1000;\n' + '\tend\n' + '\t$finish;\n' + \
						'end\n' + '\nendmodule\n'


	#главный метод с вызовом остальных методов
	def newFile(self):

		self.startDesc()
		self.moduleDesc()
		self.clockDesc(0, 25)
		self.variableDesc(0, 0, 0, 100)
		self.funcSin()
		self.setFreq(100000.0)
		self.posedgeClk()
		self.filterDesc(self.taps_num, self.taps_list)
		self.dumpFile()


	def saveFile(self):
		f = open(self.fileName, 'w')
		f.write(self.main_text)
		f.close()


	def returnText(self):
		self.main_text = re.sub('\t', '    ', self.main_text)
		return self.main_text

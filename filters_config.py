# -*- coding: utf-8 -*-

from scipy import signal

class Filter:

	def __init__(self):
		self.Naming = 'Boris'

	def low_pass(self, sample_freq, taps, cutoff_freq):
		nyq_rate = sample_freq * 0.5
		fire_freq = cutoff_freq / nyq_rate
		taps = signal.firwin(taps, fire_freq)
		print ('Filter class: low_pass filter. Freq = %s' % sample_freq)
		print (taps)
		#return signal.firwin(numtaps, freq)


	def high_pass(self, sample_freq, taps):
		print ('Filter class: high_pass filter. Freq = %s' % sample_freq)
		#return signal.firwin(numtaps, freq, pass_zero=False)


	def band_pass(self, sample_freq, taps):
		print ('Filter class: band_pass filter. Freq = %s' % sample_freq)
		#return signal.firwin(numtaps, [f1, f2], pass_zero=False)

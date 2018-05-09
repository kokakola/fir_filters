# -*- coding: utf-8 -*-

import numpy as np

from numpy import sin, cos, pi, arange, absolute, sqrt
from scipy import signal
from scipy.signal import lfilter, freqz, butter
from pylab import (	plot, figure, clf, show, grid, xlabel, ylabel,
					title, xlim, ylim)


class Filter:

	def __init__(self):
		self.Naming = 'Boris'

	def orderNum(self, sample_freq, cutoff_from, cutoff_to):

		width = (cutoff_to - cutoff_from) / (sample_freq * 0.5)
		ripple_db = 40.0

		N, beta = signal.kaiserord(ripple_db, width)

		#filtered_x = lfilter(taps_result, 1.0, x)

		###
		#delay = 0.5 * (N-1) / sample_freq
		#figure(3), plot(t, x)
		#plot(t-delay, filtered_x, 'r-')
		#plot(t[N-1:]-delay, filtered_x[N-1:], 'g', linewidth=4)
		#xlabel('dont know'), grid(True)
		###

		#show()

		return 'success', N

	def low_pass(self, sample_freq, taps, cutoff_freq):

		nsamples = 400
		t = arange(nsamples) / sample_freq
		x = cos(2*pi*0.5*t) + 0.2*sin(2*pi*2.5*t+0.1) + \
        	0.2*sin(2*pi*15.3*t) + 0.1*sin(2*pi*16.7*t + 0.1) + \
            0.1*sin(2*pi*23.45*t+.8)

		nyq_rate = sample_freq * 0.5
		fire_freq = cutoff_freq / nyq_rate

		try:
			taps_result = signal.firwin(taps, fire_freq)

			taps_int_16 = np.int16(np.rint(taps_result*2**15))
			w, h = freqz(taps_result, worN=8000)

			return 'success', taps_int_16, w, h, nyq_rate, taps_result

		except Exception as e:
			return ('> Error: ' + str(e)), [], 0, 0, 0, 0


	def high_pass(self, sample_freq, taps, cutoff_freq):

		nsamples = 400
		t = arange(nsamples) / sample_freq
		x = cos(2*pi*0.5*t) + 0.2*sin(2*pi*2.5*t+0.1) + \
        	0.2*sin(2*pi*15.3*t) + 0.1*sin(2*pi*16.7*t + 0.1) + \
            0.1*sin(2*pi*23.45*t+.8)

		nyq_rate = sample_freq * 0.5
		fire_freq = cutoff_freq / nyq_rate

		try:
			taps_result = signal.firwin(taps, fire_freq, pass_zero=False)
			
			taps_int_16 = np.int16(np.rint(taps_result*2**15))
			w, h = freqz(taps_result, worN=8000)

			return 'success', taps_int_16, w, h, nyq_rate, taps_result

		except Exception as e:
			return ('> Error: ' + str(e)), [], 0, 0, 0, 0


	def band_pass(self, sample_freq, taps, lowcut, highcut):

		nyq_rate = sample_freq * 0.5
		low = lowcut / nyq_rate
		high = highcut / nyq_rate

		try:
			b, a = butter(5, [low, high], btype='band')
			taps_result = signal.firwin(taps, [low, high], pass_zero=False)
			
			taps_int_16 = np.int16(np.rint(taps_result*2**15))
			w, h = freqz(b, a, worN=2000)

			return 'success', taps_int_16, w, h, nyq_rate, taps_result

		except Exception as e:
			return ('> Error: ' + str(e)), [], 0, 0, 0, 0


	def band_stop(self, samle_freq, taps, lowcut, highcut):

		nyq_rate = samle_freq * 0.5
		low = lowcut / nyq_rate
		high = highcut / nyq_rate

		try:
			b, a = butter(5, [low, high], btype='bandstop')
			taps_result = signal.firwin(taps, [low, high])

			taps_int_16 = np.int16(np.rint(taps_result*2**15))
			w, h = freqz(b, a, worN=2000)

			return 'success', taps_int_16, w, h, nyq_rate, taps_result

		except Exception as e:
			return ('> Error: ' + str(e)), [], 0, 0, 0, 0


	def multi_band(self, sample_freq, taps, lowcut_1, highcut_1, lowcut_2, highcut_2):

		nyq_rate = sample_freq * 0.5

		low_1 = lowcut_1 / nyq_rate
		high_1 = highcut_1 / nyq_rate

		low_2 = lowcut_2 / nyq_rate
		high_2 = highcut_2 / nyq_rate

		try:
			taps_result = signal.firwin(taps, [low_1, high_1, low_2, high_2], pass_zero=False)
			taps_int_16 = np.int16(np.rint(taps_result*2**15))

			return 'success', taps_int_16, 0, 0, nyq_rate, taps_result

		except Exception as e:
			return ('> Error: ' + str(e)), [], 0, 0, 0, 0


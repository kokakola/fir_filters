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

	def low_pass(self, sample_freq, taps, cutoff_freq):

		nsamples = 400
		t = arange(nsamples) / sample_freq
		x = cos(2*pi*0.5*t) + 0.2*sin(2*pi*2.5*t+0.1) + \
        	0.2*sin(2*pi*15.3*t) + 0.1*sin(2*pi*16.7*t + 0.1) + \
            0.1*sin(2*pi*23.45*t+.8)

		nyq_rate = sample_freq * 0.5
		fire_freq = cutoff_freq / nyq_rate

		###
		width = 5.0 / nyq_rate
		ripple_db = 60.0
		N, beta = signal.kaiserord(ripple_db, width)
		print (N)
		###

		taps_result = signal.firwin(taps, fire_freq)

		#print (np.int16(np.rint(taps_result*2**15)))
		taps_int_16 = np.int16(np.rint(taps_result*2**15))
		#print (taps_int_16)

		#print (taps_result)

		filtered_x = lfilter(taps_result, 1.0, x)

		#figure(1), plot(taps_result, 'bo-', linewidth=2)
		#title('Filter coefficient %d' % taps), grid(True)

		#figure(2), clf()
		w, h = freqz(taps_result, worN=8000)
		#plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
		#xlabel('Freq. (Hz)'), ylabel('Gain')
		#title('Freq. responce'), ylim(-0.05, 1.05), grid(True)

		###
		delay = 0.5 * (N-1) / sample_freq
		#figure(3), plot(t, x)
		#plot(t-delay, filtered_x, 'r-')
		#plot(t[N-1:]-delay, filtered_x[N-1:], 'g', linewidth=4)
		#xlabel('dont know'), grid(True)
		###

		#show()

		#print ('Filter class: low_pass filter. Freq = %s' % sample_freq)
		#return signal.firwin(numtaps, freq)

		return taps_int_16, w, h, nyq_rate, taps_result

	def high_pass(self, sample_freq, taps, cutoff_freq):

		nsamples = 400
		t = arange(nsamples) / sample_freq
		x = cos(2*pi*0.5*t) + 0.2*sin(2*pi*2.5*t+0.1) + \
        	0.2*sin(2*pi*15.3*t) + 0.1*sin(2*pi*16.7*t + 0.1) + \
            0.1*sin(2*pi*23.45*t+.8)

		nyq_rate = sample_freq * 0.5
		fire_freq = cutoff_freq / nyq_rate

		###
		#width = 5.0 / nyq_rate
		#ripple_db = 60.0
		#N, beta = signal.kaiserord(ripple_db, width)
		#print (N)
		###

		taps_result = signal.firwin(taps, fire_freq, pass_zero=False)

		taps_int_16 = np.int16(np.rint(taps_result*2**15))
		#print (taps_int_16)

		filtered_x = lfilter(taps_result, 1.0, x)

		#figure(1), plot(taps_result, 'bo-', linewidth=2)
		#title('Filter coefficient %d' % taps), grid(True)

		#figure(2), clf()
		w, h = freqz(taps_result, worN=8000)
		#plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
		#xlabel('Freq. (Hz)'), ylabel('Gain')
		#title('Freq. responce'), ylim(-0.05, 1.05), grid(True)

		#show()

		return taps_int_16, w, h, nyq_rate, taps_result

		#print ('Filter class: high_pass filter. Freq = %s' % sample_freq)
		#return signal.firwin(numtaps, [f1, f2], pass_zero=False)

	def band_pass(self, sample_freq, taps, lowcut, highcut):

		nyq_rate = sample_freq * 0.5
		low = lowcut / nyq_rate
		high = highcut / nyq_rate
		b, a = butter(5, [low, high], btype='band')

		###
		#width = 5.0 / nyq_rate
		#ripple_db = 60.0
		#N, beta = signal.kaiserord(ripple_db, width)
		#print (N)
		###

		taps_result = signal.firwin(taps, [low, high], pass_zero=False)

		taps_int_16 = np.int16(np.rint(taps_result*2**15))
		print (taps_int_16)

		#figure(1), plot(taps_result, 'bo-', linewidth=2)
		#title('Filter coefficient %d' % taps), grid(True)

		#figure(2), clf()
		w, h = freqz(b, a, worN=2000)
		#plot((sample_freq * 0.5 / pi) * w, abs(h))
		#xlabel('Freq. (Hz)'), ylabel('Gain')
		#title('Freq. responce'), ylim(-0.05, 1.05), grid(True)

		#show()

		return taps_int_16, w, h, nyq_rate, taps_result

		#print ('Filter class: band_pass filter. Freq = %s' % sample_freq)
		#return signal.firwin(numtaps, freq, pass_zero=False)


from libs import thinkdsp
from matplotlib import pyplot

cos_signal = thinkdsp.CosSignal(freq=400, amp=1.0, offset=0)
sin_signal = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

mix = sin_signal + cos_signal

mix_wave = mix.make_wave(duration=0.5, start=0, framerate=11025)

#mix_wave.plot()
#pyplot.show()

period = mix.period
segment = mix_wave.segment(start=0, duration=period*3)

segment.plot()
pyplot.show()
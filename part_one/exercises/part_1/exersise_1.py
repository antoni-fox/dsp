from libs import thinkdsp
from matplotlib import pyplot

piano_wave = thinkdsp.read_wave("piano_base.wav")
piano_spectrum = piano_wave.make_spectrum()

piano_wave_segment = piano_wave.segment(start=2.3, duration=0.5)

segment_spectrum_1 = piano_wave_segment.make_spectrum()
segment_spectrum_2 = piano_wave_segment.make_spectrum()
segment_spectrum_3 = piano_wave_segment.make_spectrum()

piano_wave_segment.plot()
pyplot.show()

piano_wave_segment.write(filename="output_segment.wav")

segment_spectrum_1.low_pass(cutoff=500, factor=0)
wave_low_pass = segment_spectrum_1.make_wave()
wave_low_pass.write(filename="output_low_pass.wav")

segment_spectrum_2.high_pass(cutoff=500, factor=0)
wave_high_pass = segment_spectrum_2.make_wave()
wave_high_pass.write(filename="output_high_pass.wav")

segment_spectrum_3.band_stop(low_cutoff=200, high_cutoff=500, factor=0)
wave_band_pass = segment_spectrum_3.make_wave()
wave_band_pass.write(filename="output_band_pass.wav")

wave_band_pass.plot()
pyplot.show()
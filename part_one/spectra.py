from libs import thinkdsp
from matplotlib import pyplot
from libs import thinkplot

# reading wave from file
violin_wave = thinkdsp.read_wave("./music/tos-redalert.wav")
# make spectrum
spectrum = violin_wave.make_spectrum()

# applying low pass filter
spectrum.low_pass(cutoff=600, factor=0.01)

spectrum.plot()
thinkplot.show()

# creating wave from spectrum with low pass filter
wave_low_pass = spectrum.make_wave()
# saving wave as .wav file
wave_low_pass.write(filename="./music/output.wav")


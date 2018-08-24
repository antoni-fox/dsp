from libs import thinkdsp
from matplotlib import pyplot

# reading wave from file
violin_wave = thinkdsp.read_wave("./music/tos-redalert.wav")

violin_wave.plot()
pyplot.show()

# writing wave to file
violin_wave.write(filename="./music/output.wav")




# listening wave
#thinkdsp.play_wave(filename="./music/tos-redalert.wav", player="aplay")

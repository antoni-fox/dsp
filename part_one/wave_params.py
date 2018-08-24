from libs import thinkdsp

# reading wave from file
violin_wave = thinkdsp.read_wave("./music/tos-redalert.wav")

# numpy array with values of signal samples
print(violin_wave.ys)

# numpy array with values of time samples
print(violin_wave.ts)

# samples in one second
print(violin_wave.framerate)

# increasing the volume of the signal
violin_wave.ys *= 2
# wave.scale(2) # the same operation


# shift for one second
violin_wave.ts += 1
# violin_wave.shift(1) # the same operation

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open("output.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, "Int16")
fs = spf.getframerate()


Time = np.linspace(0, len(signal) / fs, num=len(signal))
louder = []
for i in signal:
	louder.append(i * 2)

plt.figure(1)
plt.title("Signal Wave...")
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.plot(Time, louder)
plt.show()

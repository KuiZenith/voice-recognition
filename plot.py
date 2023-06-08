import scipy
import numpy as np
import matplotlib.pyplot as plt

def plotter():
  sampleRate, audioBuffer = scipy.io.wavfile.read("./data/bark - human/human-1.wav")

  duration = len(audioBuffer)/sampleRate

  time = np.arange(0,duration,1/sampleRate) #time vector

  plt.plot(time,audioBuffer)
  plt.xlabel('Time [s]')
  plt.ylabel('Amplitude')
  plt.show()

plotter()

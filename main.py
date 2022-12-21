import numpy as np
import matplotlib.pyplot as plt

waveFrequency = 44100


def createWave(frequency, timeSpan=0.5):
    amp = 4096
    time = np.linspace(0,timeSpan, int(waveFrequency*timeSpan))
    drawWaves = amp * np.sin(2*np.pi*frequency*time)
    return drawWaves


if __name__== '__main__':
    drawWave = createWave(440,1)
    print(drawWave, len(drawWave), np.max(drawWave), np.min(drawWave))
    plt.plot(drawWave[:int(44100/440)])
    plt.xlabel("Time Elapsed")
    plt.ylabel("Frequency Disturbance")
    plt.show()

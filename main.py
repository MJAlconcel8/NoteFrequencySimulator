import numpy as np
import matplotlib.pyplot as plt
import pprint

waveFrequency = 44100


def createWave(frequency, timeSpan=0.5):
    amp = 4096
    time = np.linspace(0,timeSpan, int(waveFrequency*timeSpan))
    drawWaves = amp * np.sin(2*np.pi*frequency*time)
    return drawWaves


def pianoNotesFrequency():
    listOfOctaves = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    startingFrequency = 261.6
    dictionaryOfNoteFrequency = {listOfOctaves[i]:startingFrequency * pow(2, (i/12)) for i in range (len(listOfOctaves))}
    dictionaryOfNoteFrequency[''] = 0.0
    return dictionaryOfNoteFrequency


if __name__== '__main__':
    drawWave = createWave(440,1)
    print(drawWave, len(drawWave), np.max(drawWave), np.min(drawWave))
    plt.plot(drawWave[:int(44100/440)])
    plt.xlabel("Time Elapsed")
    plt.ylabel("Frequency Disturbance")
    plt.show()
    pprint.pprint(pianoNotesFrequency())
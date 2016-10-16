""" This module is used to extract acoustic features for ASR system,
by Jian LI.

date: 2016/10/14 20:52 -
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from wave import open as open_wave
import numpy as np
import math

def read_wave(filename='audio.wav', txtmode='True'):
    """ manipulate wave file
    input: filename
    output: array which stores wave samples
    """

    wave_read = open_wave(filename, 'r')

    # sampling rate
    sampleRate = wave_read.getframerate()
    #Total number of samples
    num_frames = wave_read.getnframes()
    # Number of bytes required to represent the value on a storage medium
    sample_width = wave_read.getsampwidth()
    #Values of all samples in string format
    wave_points = wave_read.readframes(num_frames)

    wave_read.close()
    dtype = {1:np.int8, 2:np.int16, 4:np.int32}
    if sample_width in dtype:
        ys = np.fromstring(wave_points, dtype=dtype[sample_width])
    else:
        raise ValueError('Samplewidth {} is not proper'.format(sample_width))
    newFileName = filename.split('.')[0] + '.out'
    if txtmode:
        info = ' name: {}\n rows: {}'.format(newFileName, num_frames)
        np.savetxt(newFileName, ys, fmt='%d', delimiter=' ', header=info, comments='#')
    else:
        pass # what if you don't want to write it to a file, print?

def windowFunction(sampleArray, windowname='Hamming'):
    nums = sampleArray.size
    y = np.zeros(nums)
    if windowname == 'Hamming':
        for i in range(nums):
            y[i] = (0.54 - 0.46 * np.cos(2 * np.pi * i / (nums - 1))) * sampleArray[i]
        return y
    else:
        return sampleArray


def windowing(sampleArray, sampleRate=16000, frameRate=10000, windowWidth=0.02, windowName = 'Hamming'):
    """ Add window to the samples
    sampleArray: Array which store all the samples for one audio
    sampleRate: The rate of sampling, default value is 16KHz
    frameRate: The rate of producing frames, default value is 10KHz
    windowWidth: The length of window in seconds
    doHamming: if True, using Hamming window; otherwise, rectangular window
    """
    samples = np.loadtxt(sampleArray)
    totalSamples = samples.size # total number of samples
    samplePeriod = 1.0 / sampleRate
    framePeriod = 1.0 / frameRate
    samplePerWindow = int(math.ceil(windowWidth / samplePeriod))
    sampleShift = int(math.ceil(framePeriod / samplePeriod))
    totalFrames = int(math.ceil((totalSamples - samplePerWindow) / sampleShift))
    #print 'samplePeriod is {}, framePeriod is {}'.format(samplePeriod, framePeriod)
    #print 'totalSamples is {}, samplePerWindow is {}, sampleShift is {}, totalFrames is {}'.format\
        #(totalSamples, samplePerWindow, sampleShift, totalFrames)
    output = np.zeros((totalFrames, samplePerWindow))
    for i in range(totalFrames):
        frameContent = samples[i*sampleShift:i*sampleShift+samplePerWindow]
        output[i,:] = windowFunction(frameContent, windowName)

    newFileName = sampleArray.split('.')[0] + '.win'
    info = ' name: {}\n rows: {}\n column: {}'.format(newFileName, totalFrames, samplePerWindow)
    np.savetxt(newFileName, output, fmt='%.2f', delimiter=' ', header=info, comments='#')


def doFFT():
    pass


    
if __name__ == '__main__':
    #read_wave('1.wav')
    windowing('1.out', windowName='rectangular')

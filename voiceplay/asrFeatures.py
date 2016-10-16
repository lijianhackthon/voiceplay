""" This module is used to extract acoustic features for ASR system,
by Jian LI.

date: 2016/10/14 20:52 -
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from wave import open as open_wave
import numpy as np

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

def windowing():
    pass






if __name__ == '__main__':
    read_wave('1.wav')

""" This module is used to extract acoustic features for ASR system,
by Jian LI.

date: 2016/10/14 20:52 -
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from wave import open as open_wave
import numpy as np

def read_wave(filename='audio.wav'):
    """ manipulate wave file
    input: filename
    output: array which stores wave samples
    """

    wave_read = open_wave(filename, 'r')

    #Total number of frames
    num_frames = wave_read.getnframes()
    # Number of bytes required to represent the value on a storage medium
    sample_width = wave_read.getsampwidth()
    #Values of all frames in string format
    wave_points = wave_read.readframes(num_frames)

    ys = np.fromstring(wave_points, dtype=np.int16)
    wave_read.close()
    return ys

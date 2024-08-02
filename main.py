
import os
from pathlib import Path
from pydub import AudioSegment
from scipy.io import wavfile

os.chdir('Sound')

def output_duration(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    return hours, mins


for item in Path('.').glob('*.wav'):
    audio = AudioSegment.from_wav(item)
    sample_rate, data = wavfile.read(item)
    len_data = len(data)
    t = len_data / sample_rate
    hours, mins = output_duration(int(t))
    duration = len(audio) / 1000.0
    dur = '{:02}:{:02}:{:06}'.format(hours, mins, duration)
    dur = str(dur).replace(".", ",")
    print(item, dur, file=open('output.txt', 'a'))

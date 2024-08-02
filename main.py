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
    dur = '{:02}:{:02}:{:06.3f} '.format(hours, mins, duration)
    dur = str(dur).replace(".", ",")
    name = str(item)
    res = name.rstrip('.wav')
    with open(r"..\Dialogs.txt", "r", encoding='utf-8') as fp:
        lines = fp.readlines()
        for row in lines:
            if row.find(res) != -1:
                idx = row.find('=')
                dialog = row[idx + 1:]
                print("1")
                print("00:00:00,000 -->", dur)
                print(dialog)
                print('1', file=open(f'..\Srt\{res}.srt', 'a'))
                print("00:00:00,000 -->", dur, file=open(f'..\Srt\{res}.srt', 'a'))
                print(dialog, file=open(f'..\Srt\{res}.srt', 'a'))

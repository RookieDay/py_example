#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9
# @Author  : RookieDay
# @Site    : 
# @File    : play_back
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 边录边播 然后保存

import pyaudio
import os
import wave

out_wav = os.path.join(os.path.dirname(__file__),'out_wav_play.wav')
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print('* recording')

frames = []

for i in range(0,int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    stream.write(data,CHUNK)
    frames.append(data)

print('* done')
stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open(out_wav,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(WIDTH)
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
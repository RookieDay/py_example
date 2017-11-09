#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9
# @Author  : RookieDay
# @Site    : 
# @File    : record_wav
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition
# Record a few seconds of audio and save to a WAVE file."""
import pyaudio
import wave
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAV_OUTPUT = os.path.join(os.path.dirname(__file__),'out_wav.wav')


# 实例化
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print('* recording')

frames = []

for i in range(0,int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print('* done recording')

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAV_OUTPUT,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
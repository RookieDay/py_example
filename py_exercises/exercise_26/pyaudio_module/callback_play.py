#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9
# @Author  : RookieDay
# @Site    : 
# @File    : callback_play
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import pyaudio
import wave
import os
import time

wav_file = os.path.join(os.path.dirname(__file__),'Alizee.wav')

wf = wave.open(wav_file,'rb')
p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    # print(data)
    return (data,pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
stream.start_stream()

while stream.is_active():
    time.sleep(1)

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
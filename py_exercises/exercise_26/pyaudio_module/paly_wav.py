#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition
# http://people.csail.mit.edu/hubert/pyaudio/docs/#module-pyaudio
# http://people.csail.mit.edu/hubert/pyaudio/
# pyaudio wave

import pyaudio
import wave
import sys,os

wav_path = os.path.join(os.path.dirname(__file__),'Alizee.wav')
CHUNK = 1024

# if len(sys.argv) < 2:
#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)

# 只读方式打开wav文件
wf = wave.open(wav_path,'rb')    #(sys.argv[1],'rb')

# 实例化
p = pyaudio.PyAudio()

# 打开数据流
# 参数明细 http://people.csail.mit.edu/hubert/pyaudio/docs/#pyaudio.Stream.__init__
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# 读取数据
data = wf.readframes(CHUNK)

# 播放
while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

# 停止数据
stream.stop_stream()
stream.close()

# 关闭pyaudio
p.terminate()
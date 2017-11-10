#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8
# @Author  : RookieDay
# @Site    : 
# @File    : record_website
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# pyaudio 参考
# http://people.csail.mit.edu/hubert/pyaudio/
# 百度语音识别
# https://cloud.baidu.com/product/speech
# 以及查看接口文档
# 需要申请ID
""" 你的 APPID AK SK """
# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'
# 对语音中午进行简单jieba分词


import pyaudio
import wave
import os
import jieba
import webbrowser
from aip import AipSpeech

""" 你的 APPID AK SK """
# 这里大家申请下自己填一下即可
APP_ID = '******'
API_KEY = '******'
SECRET_KEY = '******'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

out_wav = os.path.join(os.path.dirname(__file__),'out_speech.wav')
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

def record_save(out_wav):
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)
    print('* recording...')

    frames = []
    for i in range(0,int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        stream.write(data,CHUNK)
        frames.append(data)
    print('* done...')
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf =wave.open(out_wav,'wb')
    wf.setframerate(RATE)
    wf.setsampwidth(WIDTH)
    wf.setnchannels(CHANNELS)
    wf.writeframes(b''.join(frames))
    wf.close()

def get_file_content(out_wav):
    with open(out_wav,'rb') as f:
        return f.read()

def parse_txt(txt):
    content = (txt[0])[:-1].split('，')
    # print(content)
    if '百度' in content:
        webbrowser.open('www.baidu.com')
    else:
        return None
    # seg_list = jieba.lcut(txt)
    # if '百度' in seg_list:
    #     webbrowser.open('www.baidu.com')
    # else:
    #     return None

if __name__ == '__main__':
    record_save(out_wav)
    wav_content = aipSpeech.asr(get_file_content(out_wav), 'wav', 16000, {'lan': 'zh',})
    print(wav_content)
    while wav_content['err_no'] != 0:
        print('* recording please...')
        record_save(out_wav)
        print(wav_content)
        wav_content = aipSpeech.asr(get_file_content(out_wav), 'wav', 16000, {'lan': 'zh', })
    if 'result' in wav_content:
        txt = wav_content['result']
        print(txt)
    # txt = ['和，虎，火，呼呼，虎，嗯，火，黄，嘿嘿，']
    # parse_txt(txt)
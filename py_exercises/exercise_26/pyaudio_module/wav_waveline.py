#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9
# @Author  : RookieDay
# @Site    : 
# @File    : wav_waveline
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

# 参考https://www.cnblogs.com/lzxwalex/p/6922099.html
# 画出语音波形图

import os
import wave
import numpy as np
import matplotlib.pyplot as plt

wav_file = os.path.join(os.path.dirname(__file__),'Alizee.wav')

def wav_processed(wav_file):
    wf = wave.open(wav_file,'rb')
    # 获取wav文件的参数（以tuple形式输出），依次为(声道数，采样精度，采样率，帧数，......)
    # params -->
    # _wave_params(nchannels=2, sampwidth=2, framerate=44100, nframes=9229824, comptype='NONE', compname='not compressed')
    params = wf.getparams()
    # print(params)
    frames_sra, frames_wav = params[2], params[3]
    # read the data
    wav_data = wf.readframes(frames_wav)
    wf.close()

    data_format = np.fromstring(wav_data,dtype=np.short)
    if  params[0] == 2:  #左右声道处理
        # https://www.cnblogs.com/xinyuyuanm/archive/2013/05/18/3086000.html
        data_format.shape = -1,2
        data_format = data_format.T
    time = np.arange(0,frames_wav)*(1.0/frames_sra)
    return data_format, time


if __name__ == '__main__':
    # wav_data, wav_time = wav_processed(wav_file)
    wav_data, wav_time = wav_processed(wav_file)
    plt.title('Alizee wav`s Frames')
    # 画布划分为两行一列
    # 2 -- 行
    # 1 -- 列
    # 1 -- 使用第几个plot
    plt.subplot(211)
    plt.plot(wav_time,wav_data[0],color='pink')
    plt.subplot(212)
    # plt.plot()是用于绘制线条的方法，我们用到了其中的三个参数  （X坐标，y坐标，颜色）
    plt.plot(wav_time,wav_data[1],color='green')
    plt.show()
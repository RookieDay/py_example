#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29
# @Author  : RookieDay
# @Site    : 
# @File    : count_code
# @Software: PyCharm Community Edition
import os
from collections import Counter
import re

re_file = re.compile(r'(.py)$')
code_path = 'D:\\front_end\\py_example'
all_code_line = [0,0,0,0]

def parse_code_word(py_pre_path,code_file):
    global all_code_line
    with open(py_pre_path,encoding='utf-8') as f:
        code_line = 0
        blank_line = 0
        comment_line = 0
        total_line = 0
        lines = f.readlines()
        for line in lines:
            total_line = total_line + 1
            line_strip = line.strip()
            if line_strip.startswith('#'):
                comment_line = comment_line + 1
            elif len(line_strip):
                code_line = code_line + 1
            else:
                blank_line = blank_line + 1
        all_code_line[0] = all_code_line[0] + total_line
        all_code_line[1] = all_code_line[1] + code_line
        all_code_line[2] = all_code_line[2] + comment_line
        all_code_line[3] = all_code_line[3] + blank_line
        print("%s file has %s lines, %s lines code, %s lines comment, %s lines blanks" % (code_file, total_line, code_line, comment_line, blank_line))

def process_all_py(code_path):
    for fpath, dirs, files in os.walk(code_path):
        for file in files:
            py_pre, postfix = os.path.splitext(file)
            if(re_file.match(postfix.lower())):
                py_pre_path = os.path.join(fpath,file)
                parse_code_word(py_pre_path,file)

if __name__ == '__main__':
    process_all_py(code_path)
    print('-'*40)
    print("the path`s .py files has %s lines, %s lines code, %s lines comment, %s lines blanks" % (all_code_line[0], all_code_line[1], all_code_line[2], all_code_line[3]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 09:21
# @Author  : Evescn
# @Site    :
# @File    : 1.3.py
# @Software: PyCharm

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
    # print(previous_lines)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

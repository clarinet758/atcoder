#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import io
import re
import math

N = raw_input()
w = map(str, raw_input().split())

#while '.' in w:
#    w.remove('.')

ws = w[-1]
wsr = re.replace('.', '', ws)
print w
print ws
print wsr

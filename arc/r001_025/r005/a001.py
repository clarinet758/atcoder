#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import io
import re
import math

kai = 0
N = raw_input()
w = map(str, raw_input()[:-1].split())

kai = w.count("Takahashikun")
kai = kai + w.count("takahashikun")
kai = kai + w.count("TAKAHASHIKUN")
print kai

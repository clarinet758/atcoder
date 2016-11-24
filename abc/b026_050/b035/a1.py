#!/usr/bin/env python
# -*- coding: UTF-8 -*-

w,h=map(int,raw_input().split())
print '16:9' if w%16==0 and h/(w/16)==9 else '4:3'

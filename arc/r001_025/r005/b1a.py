#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys, os, re
#tate, yoko, h = int(raw_input()), int(raw_input()), raw_input()
o = map(str, raw_input().split())
#tate, yoko=int(tate),int(yoko)
p = []
a = 0
#y = [map(int, raw_input().split()) for i in xrange(9)]
y = [map(int, list(raw_input())) for i in xrange(9)]
tate = int(o[1])-1
yoko = int(o[0])-1

if  o[2] == 'R':
    if int(o[0])<7:
        for i in xrange(4):
#        p.append(y[tate][yoko+a],y[tate][yoko+1],y[tate][yoko+2],y[tate][yoko+3])
            p.append(str(y[tate][yoko+a]))
            a+=1



print ''.join(p)
#print y

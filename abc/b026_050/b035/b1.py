#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s=raw_input()
t=int(raw_input())
x=y=q=0
for i in s:
    if i=='U': y+=1
    if i=='D': y-=1
    if i=='L': x+=1
    if i=='R': x-=1
    if i=='?': q+=1
if t==1:
    print abs(x)+abs(y)+q
else:
    tmp=abs(x)+abs(y)
    tmp-=q
    if tmp>0:
        print tmp
    elif tmp%2==0:
        print 0
    else:
        print 1

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a,b=map(int, raw_input().split())
d={i:727 for i in range(min(a,b)-21,max(a,b)+21)}
r=[1,5,10]
tmp=set([a])
d[a]=0
while len(tmp):
    w=tmp.pop()
    for i in r:
        if w+i in d and d[w+i]>d[w]+1:
            tmp.add(w+i)
            d[w+i]=d[w]+1
        if w-i in d and d[w-i]>d[w]+1:
            tmp.add(w-i)
            d[w-i]=d[w]+1
print d[b]


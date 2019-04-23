#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

k,t=map(int,input().split())
l=[int(i) for i in input().split()]
if t==1:
    print(l[0]-1)
    exit()
while 1:
    l.sort(reverse=True)
    if l[1]==0: break
    l[0]-=l[1]
    l[1]=0

print(max(0,l[0]-1))

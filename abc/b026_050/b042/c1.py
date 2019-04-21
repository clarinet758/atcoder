#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n,k=map(int,input().split())
d=[int(i) for i in input().split()]
t=n
while 1:
    x=t
    while 1:
        if x%10 in d:
            break
        else:
            x//=10
        if x==0:
            print(t)
            exit()
    t+=1

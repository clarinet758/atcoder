#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

x,y=map(int,input().split())
if x//y>=1 and x%y==0:
    print(-1)
    exit()
a=x*(y-1)
b=x*(y+1)
t=1000000000000000000
if a>0 and a%y and a<=t:
    print(a)
elif b>0 and b%y and b<=t:
    print(b)
else:
    print(-1)



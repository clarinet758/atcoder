#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a=int(raw_input())
b=int(raw_input())
n=int(raw_input())
a,b=max(a,b),min(a,b)
if n%a:
    n-=n%a
    n+=a
cnt=0
while 1:
    if (n+a*cnt)%b==0:
        print n+a*cnt
        break
    cnt+=1

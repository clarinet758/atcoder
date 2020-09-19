#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

n,m,k,e=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a.sort(reverse=True)
b.sort()
ans=chk=0
while 1:
    if len(a)==0:
        ans=1
        break
    if a[-1]<=e:
        e-=a[-1]
        a.pop()
    elif len(b) and k>chk:
        e+=b.pop()
        chk+=1
    else:
        break
if ans:
    print("Yes")
    print(chk)
else:
    print("No")
    print(n-len(a))

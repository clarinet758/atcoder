#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from collections import deque
n=int(input())
d={}
for i in range(n-1):
    a,b=map(int,input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a]=[b]
    if b in d:
        d[b].append(a)
    else:
        d[b]=[a]
f,s=set([1]),set([n])
e=deque([0,1])
u=deque([0,n])
x=0
while 1:
    if len(e)==len(u)==1: break

    if len(e)>0:
        while e[-1]!=0:
            tmp=e.pop()
            for i in d[tmp]:
                if i not in f and i not in s:
                    f.add(i)
                    e.appendleft(i)
        e.rotate()
    if len(u)>0:
        while u[-1]!=0:
            tmp=u.pop()
            for i in d[tmp]:
                if i not in f and i not in s:
                    s.add(i)
                    u.appendleft(i)
        u.rotate()

print(["Fennec","Snuke"][len(f)<=len(s)])

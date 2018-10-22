#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
o,q,e=[],[],[]
for i in a:
    if i%4==0: q.append(i)
    elif i%2==0: e.append(i)
    else: o.append(i)
s=0
for i in range(n):
    if s==0:
        if len(o):
            o.pop()
            s=4
        elif len(e):
            e.pop()
            s=2
        else:
            q.pop()
    elif s==2:
        if len(e):
            e.pop()
            s=2
        elif len(q):
            q.pop()
            s=0
        else:
            print("No")
            exit()
    else:
        if len(q):
            q.pop()
            s=0
        else:
            print("No")
            exit()
print("Yes")

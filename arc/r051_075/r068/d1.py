#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
a.sort()
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

t=[]
for i in d:
    t.append(d[i])
t.sort(reverse=True)
ans=len(t)
chk=0
for i in t:
    i-=1
    if chk==0:
        chk=i%2
    else:
        chk-=i%2
print(ans-chk)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,w=map(int,input().split())
d=[0]*200005
for i in range(n):
    s,t,p=map(int,input().split())
    d[s]+=p
    d[t]-=p
chk=0
for i in range(200004):
    chk+=d[i]
    if chk>w:
        print("No")
        exit()
print("Yes")

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
x,y,h=map(int,input().split())
d=set([(x,y,h)])
t=[x,y,h]
for i in range(n-1):
    x,y,h=map(int,input().split())
    d.add((x,y,h))
    if t[2]==0: t=[x,y,h]

for i in range(101):
    for j in range(101):
        f=0
        p=abs(t[0]-i)+abs(t[1]-j)+t[2]
        for k in d:
            if k[2]!=0 and abs(k[0]-i)+abs(k[1]-j)+k[2]!=p: f=1
            if k[2]==0 and abs(k[0]-i)+abs(k[1]-j)+k[2]<p: f=1
        if f==0:
            print(i,j,p)
            exit()



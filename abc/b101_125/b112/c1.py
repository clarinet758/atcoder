#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
d=[]
for i in range(n):
    a,b,c=map(int,input().split())
    d.append((a,b,c))
    if c!=0:
        x,y,h=a,b,c

for i in range(101):
    for j in range(101):
        p=abs(i-x)+abs(j-y)+h
        for a,b,c in d:
            if (c==0 and p-abs(i-a)-abs(j-b)<1) or (c==(p-abs(i-a)-abs(j-b))):
                pass
            else:
                p=-1
                break
        if p!=-1:
            print(i,j,p)
            exit()
            
            

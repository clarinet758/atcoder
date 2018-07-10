#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
h,w=map(int,input().split())
l=[]
d=[-1,0,1]
for i in range(h):
    a=list(input())
    l.append(a)
for i in range(h):
    for j in range(w):
        cnt=0
        for x in d:
            for y in d:
                if 0<=i+x<h and 0<=j+y<w:
                    if l[i+x][j+y]=="#":
                        cnt+=1
        if l[i][j]==".": l[i][j]=cnt
for i in l:
    print("".join(map(str,i)))
          

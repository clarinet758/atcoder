#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(300000)

def chk():
    cnt=0
    for i in range(8):
        if (w[i].count("Q")>1): return 0
        if (w[i].count("Q")==1): cnt+=1
        a=b=c=d=l=0
        for j in range(8):
            if w[j][i]=="Q": l+=1
            if i+j<8 and w[0+j][i+j]=="Q": a+=1
            if i-j>-1 and w[7-j][i-j]=="Q": b+=1
            if i-j>-1 and w[i-j][0+j]=="Q": c+=1
            if i+j<8 and w[i+j][7-j]=="Q": d+=1
        if l>1 or a>1 or b>1 or c>1 or d>1: return 0
    if cnt==8:
        for i in w:
            print("".join(i))
        exit()
    return 1

def sol(a):
    for i in range(a,64,1):
        x=i//8
        y=i%8
        if w[x][y]=="Q": continue
        w[x][y]="Q"
        if chk():
            sol(i+1)
        w[x][y]="."

w=[]
for i in range(8):
    w.append(list(input()))
sol(0)
            
print("No Answer")



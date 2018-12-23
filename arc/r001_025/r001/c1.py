#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def chk(y,x):
    for i in range(1,8):
        if 0<=1*i+y<8 and c[1*i+y][x]=="Q": return 0
        if 0<=1*i+x<8 and c[y][1*i+x]=="Q": return 0
        if 0<=-1*i+y<8 and c[-1*i+y][x]=="Q": return 0
        if 0<=-1*i+x<8 and c[y][-1*i+x]=="Q": return 0
        if 0<=1*i+y<8 and 0<=-1*i+x<8 and c[1*i+y][-1*i+x]=="Q": return 0
        if 0<=-1*i+y<8 and 0<=-1*i+x<8 and c[-1*i+y][-1*i+x]=="Q": return 0
        if 0<=-1*i+y<8 and 0<=1*i+x<8 and c[-1*i+y][1*i+x]=="Q": return 0
        if 0<=1*i+y<8 and 0<=1*i+x<8 and c[1*i+y][1*i+x]=="Q": return 0
    return 1

def test():
    for i in range(64):
        if c[i//8][i%8]=="Q" and chk(i//8,i%8)==0:
            print("No Answer")
            exit()
    return 1

def sol(q):
    if q==0 and test():
        for i in c:
            print(*i, sep="")
        exit()
    for i in range(64):
        if c[i//8][i%8]=="Q" or chk(i//8,i%8)==0: continue
        c[i//8][i%8]="Q"
        sol(q-1)
        c[i//8][i%8]="."

c=[]
q=8
for i in range(8):
    t=input()
    if t.count("Q")>1:
        print("No Answer")
        exit()
    if "Q" in t: q-=1
    c.append(list(t))
sol(q)

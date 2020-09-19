#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def sol():
    import sys
    input=sys.stdin.readline
    n=int(input())
    a=[]
    d={}
    x=y=0
    for i in range(n):
        t=int(input())
        a.append(t)
        if t in d:
            d[t]+=1
        else:
            d[t]=1
        if t>x:
            y=x
            x=t
        elif t>y:
            y=t
    for i in a:
        if i==x and d[i]==1:
            print(y)
        else:
            print(x)

if __name__=="__main__":
    sol()

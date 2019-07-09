#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    import sys
    input=sys.stdin.readline
    mod=10**9+7
    n=int(input())
    d=[int(input())]
    for i in range(n-1):
        w=int(input())
        t=[mod]*2
        for j in range(len(d)):
            if d[j]>=w and t[0]>d[j]:
                t[0]=w
                t[1]=j
        if t[0]!=mod:
            d[t[1]]=t[0]
        else:
            d.append(w)
    print(len(d))

if __name__=="__main__":
    sol()

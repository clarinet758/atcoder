#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
input=sys.stdin.readline

def qul(d,l,p):
    if p in d:
        for j in d[p]:
            if j in d:
                if j not in l:
                    l.append(j)
                qul(d,l,j)
            else:
                l.append(j)
def sol():
    d={}
    n,q=map(int,input().split())
    for i in range(n-1):
        a,b=map(int,input().split())
        if a in d:
            d[a].append(b)
        else:
            d[a]=[b]
    w=[0]*(n+1)
    for i in d:
        d[i].sort(reverse=True)
    for i in range(q):
        p,x=map(int,input().split())
        w[p]+=x
    for i in range(n,0,-1):
        l=[]
        qul(d,l,i)
        for j in l:
            w[j]+=w[i]
        #print(i,l)
    print(*w[1:])

if __name__=="__main__":
    sol()

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

def sol():
    n,m=map(int,input().split())
    d={}
    for i in range(m):
        u,v=map(int,input().split())
        if u in d:
            d[u].append(v)
        else:
            d[u]=[v]
    s,t=map(int,input().split())
    ans=chk=0
    w=deque([0,s])
    tmp=[[0,0,0] for i in range(n+1)]
    ans=1
    n+=n//2
    n*=2
    while n:
        x=w.pop()
        if x==0:
            ans+=1
            n-=1
            w.appendleft(0)
        elif x in d:
            for j in d[x]:
                if ans%3==0 and j==t:
                    print(ans//3)
                    exit()
                if tmp[j][ans%3]==0:
                    w.appendleft(j)
                    tmp[j][ans%3]=1
    print(-1)

if __name__=="__main__":
    sol()

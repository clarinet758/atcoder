#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from collections import deque
def sol():
    n=int(input())
    d=[-1]*n
    l=deque([])
    for i in range(n-1):
        u,v,w=map(int,input().split())
        u,v=min(u,v),max(u,v)
        l.append((u-1,v-1,w))
    f=0
    while len(l):
        x=l.popleft()
        if f:
            if x[2]%2 and d[x[0]]==0:
                d[x[1]]=1
            elif x[2]%2 and d[x[0]]==1:
                d[x[1]]=0
            elif x[2]%2==0 and d[x[0]]==1:
                d[x[1]]=1
            elif x[2]%2==0 and d[x[0]]==0:
                d[x[1]]=0
            elif x[2]%2 and d[x[1]]==0:
                d[x[0]]=1
            elif x[2]%2 and d[x[1]]==1:
                d[x[0]]=0
            elif x[2]%2==0 and d[x[1]]==1:
                d[x[0]]=1
            elif x[2]%2==0 and d[x[1]]==0:
                d[x[0]]=0
            else:
                l.append(x)
        else:
            f=1
            if x[2]%2:
                d[x[0]]=0
                d[x[1]]=1
            else:
                d[x[0]]=0
                d[x[1]]=0
    for i in d:
        print(i)

if __name__=="__main__":
    sol()

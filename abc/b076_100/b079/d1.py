#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    h,w=map(int,input().split())
    c=[]
    for i in range(10):
        l=[int(i) for i in input().split()]
        c.append(l)
    a=[]
    for i in range(h):
        l=[int(i) for i in input().split()]
        a.append(l)
    p=[0]*10
    for i in range(10):
        if i==1: continue
        d=[1003]*10
        d[i]=0
        q=set([i])
        while 1:
            if len(q)==0: break
            x=q.pop()
            for j in range(10):
                if i==j: continue
                if (d[j]>d[x]+c[x][j]):
                    d[j]=d[x]+c[x][j]
                    q.add(j)
        p[i]=d[1] 
    ans=0
    for i in range(h):
        for j in range(w):
            if a[i][j]==-1: pass
            else: ans+=p[a[i][j]]
    print(ans)

if __name__=="__main__":
    sol()

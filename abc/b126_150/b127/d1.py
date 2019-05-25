#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import heapq
def sol():
    n,m=map(int,input().split())
    a=[int(i) for i in input().split()]
    d={}
    w=[]
    q=[]
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            w.append(i)
    for i in w: heapq.heappush(q, i)
    for i in range(m):
        b,c=map(int,input().split())
        while b:
            if c>q[0]:
                x=min(b,d[q[0]])
                if c in d:
                    d[c]+=x
                    b-=x
                    d[q[0]]-=x
                    if d[q[0]]==0:
                        heapq.heappop(q)
                else:
                    d[c]=x
                    b-=x
                    d[q[0]]-=x
                    heapq.heappush(q,c)
                    if d[q[0]]==0:
                        heapq.heappop(q)
            else:
                break
    ans=chk=0
    for i in d:
        ans+=i*d[i]
    print(ans)

if __name__=="__main__":
    sol()

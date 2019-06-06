#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    chk=set([])
    n,m=map(int,input().split())
    d=[[0]*1001 for i in range(n)]
    ans=0
    for i in range(m):
        a,b,l=map(int,input().split())
        d[a-1][l-1000]+=1
        d[b-1][l-1000]+=1
    for i in d:
        for j in range(271):
            if j==270 and i[j]>1:
                ans+=(i[j]*(i[j]-1))//2
            elif j!=270 and 0<=540-j<=1000 and i[540-j]>0 and i[j]>0:
                ans+=i[j]*i[540-j]
    print(ans)

if __name__=="__main__":
    sol()

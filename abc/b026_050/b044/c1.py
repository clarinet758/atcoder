#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    n,a=map(int,input().split())
    x=[int(i) for i in input().split()]
    ans=chk=0
    d=[[0]*2501 for j in range(51)]
    d[0][0]=1
    for i in x:
        for j in range(2500,i-1,-1):
            for k in range(50,0,-1):
                d[k][j]+=d[k-1][j-i]
    for i in range(1,51):
        ans+=d[i][i*a]
    print(ans)

if __name__=="__main__":
    sol()

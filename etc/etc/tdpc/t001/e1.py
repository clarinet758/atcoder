#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


mod=10**9+7
d=int(input())
n="0"+input()
x=len(n)
l=[int(i) for i in n]
ans=0
dp1=[[0]*101 ,[0]*101]
dp2=[[0]*101 ,[0]*101]
dp1[0][0]=1
for i in range(1,x):
    for j in range(0,d+1):
        if dp1[i%2-1][j]:
            for k in range(l[i]):
                k=[(k+j)%d,d][(k+j)%d==0]
                dp2[i%2][k]+=1
                dp2[i%2][k]%=mod
            x=(j+l[i])%d
            if x==0: x=d
            dp1[i%2][x]=1
            dp1[i%2-1][j]=0
        if dp2[i%2-1][j]:
            for k in range(10):
                k=[(k+j)%d,d][(k+j)%d==0]
                dp2[i%2][k]+=dp2[i%2-1][j]
                dp2[i%2][k]%=mod
            dp2[i%2-1][j]=0


print((dp1[0][d]+dp1[1][d]+dp2[0][d]+dp2[1][d]-1)%mod)

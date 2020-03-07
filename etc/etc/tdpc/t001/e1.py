#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def dd(x,d): return [x%d,d][x%d==0]
mod=10**9+7

d=int(input())
n="0"+input()
l=[int(i) for i in n]
x=len(n)
dp=[[[0]*(d+1),[0]*(d+1)] for i in "xx"]
# dp[0]==n dp[1]<n
dp[0][0][0]=1
for ii in range(1,x):
    i=ii%2
    dp[i][1][0]=1
    for j in range(d+1):
        if dp[i-1][0][j]:
            dp[i][0][dd(j+l[ii],d)]=1
            p=[0,1][ii==1]
            for k in range(p,l[ii]):
                dp[i][1][dd(j+k,d)]+=1
        if dp[i-1][1][j]:
            for k in range(10):
                if j+k==0:
                    dp[i][1][0]=1
                else:
                    dp[i][1][dd(j+k,d)]+=dp[i-1][1][j]
        dp[i][0][j]%=mod
        dp[i][1][j]%=mod
        dp[i-1][0][j]=0
        dp[i-1][1][j]=0
            
#for i in dp:
#    print(i)
print((dp[0][0][-1]+dp[0][1][-1]+dp[-1][0][-1]+dp[-1][1][-1])%mod)

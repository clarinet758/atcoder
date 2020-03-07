#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=10**9+7
d=int(input())
n=input()
l=[int(i) for i in "0"+n]
dp=[[[0]*(d+2),[0]*(d+2)] for _ in "ww"]
dp[0][0][0]=1
#print(dp)
for i,j in enumerate(n,start=1):
    j=int(j)
    for k in range(d+1):
        if dp[i%2-1][0][k]:
            dp[i%2][0][[(k+j)%d,d][(k+j)%d==0]]=1
            for p in range(j):
                dp[i%2][1][[[(p+k)%d,d][(p+k)%d==0],0][k==p==0]]+=1
        if dp[i%2-1][1][k]:
            for p in range(10):
                if k==p==0:
                    dp[i%2][1][0]=1
                else:
                    dp[i%2][1][[(p+k)%d,d][(p+k)%d==0]]+=dp[i%2-1][1][k]
    
    for k in range((d+2)*2):
        a,b=k//(d+2),k%(d+2)
        dp[i%2-1][a][b]=0
        dp[i%2][a][b]%=mod
print((dp[0][0][d]+dp[0][1][d]+dp[1][0][d]+dp[1][1][d])%mod)

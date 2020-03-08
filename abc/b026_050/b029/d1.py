#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=input()
l=[int(i) for i in "0"+n]
dp=[[[0]*12,[0]*12] for _ in "ww"]
dp[0][0][0]=1
for i,j in enumerate(l):
    if i==0: continue
    #dp[i%2][1][0]=1
    #print(dp)
    for k in range(11):
        if dp[i%2-1][0][k]:
            dp[i%2][0][k+(j==1)]=1
            dp[i%2][1][k+1]+=(j>1)
            dp[i%2][1][k]+=[[1,j-1][j>1],0][j==0]
        if dp[i%2-1][1][k]:
            dp[i%2][1][k+1]+=dp[i%2-1][1][k]
            dp[i%2][1][k]+=dp[i%2-1][1][k]*9
    for k in range(24):
        dp[i%2-1][k//12][k%12]=0
ans=0
for i in range(4):
    for j in range(1,12):
        ans+=dp[i//2][i%2][j]*j
    
print(ans)

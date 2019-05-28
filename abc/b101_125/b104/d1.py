#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
mod=1000000007

s=input()
x=len(s)
dp=[[0 for i in range(4)] for j in range(100005)]
for i in range(x,-1,-1):
    for j in range(3,-1,-1):
        if i==x:
            dp[i][j]=[0,1][j==3]
        else:
            dp[i][j]=dp[i+1][j]*([1,3][s[i]=="?"])
            if (j<3 and (s[i]=="?" or s[i]=="ABC"[j])):
                dp[i][j]+=dp[i+1][j+1]
            dp[i][j]%=mod
print(dp[0][0])

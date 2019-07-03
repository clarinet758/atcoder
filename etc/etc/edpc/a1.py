#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
h=[int(i) for i in input().split()]
dp=[100000 for i in range(n+1)]
dp[0],dp[1]=0,0
for i in range(2,n+1):
    dp[i]=min(dp[i-2]+abs(h[i-1]-h[max(0,i-3)]),dp[i-1]+abs(h[i-1]-h[i-2]))
print(dp[n])

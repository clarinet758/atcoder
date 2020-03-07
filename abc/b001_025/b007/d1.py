#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def cnt(x):
    dp=[[[0,0],[0,0]] for _ in "ww"]
    dp[0][0][0]=1
    l=[int(i) for i in "0"+str(x)]
    for i,j in enumerate(l):
        if i==0: continue
        if dp[i%2-1][0][1] or j in (4,9):
            dp[i%2][0][1]=1
        else:
            dp[i%2][0][0]=1

        if dp[i%2-1][0][0]:
            dp[i%2][1][1]+=[0,1][j>4]
            dp[i%2][1][0]+=[j,j-1][j>4]
        if dp[i%2-1][0][1]:
            dp[i%2][1][1]+=j

        if dp[i%2-1][1][1]:
            dp[i%2][1][1]+=dp[i%2-1][1][1]*10
        if dp[i%2-1][1][0]:
            dp[i%2][1][1]+=dp[i%2-1][1][0]*2
            dp[i%2][1][0]+=dp[i%2-1][1][0]*8
        for p in range(4):
            dp[i%2-1][p//2][p%2]=0

    return dp[0][0][1]+dp[1][0][1]+dp[0][1][1]+dp[1][1][1]
    
a,b=map(int,input().split())
a-=1
print(cnt(b)-cnt(a))

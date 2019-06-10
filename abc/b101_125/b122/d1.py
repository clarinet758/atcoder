#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=10**9+7
n=int(input())
memo=[{} for i in range(n+1)]

def ok(last4):
    for i in range(4):
        t=list(last4)
        if i>=1:
            t[i-1],t[i]=t[i],t[i-1]
        if "".join(t).count("AGC")>=1:
            return 0
    return 1

def dfs(cur,last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur==n:
        return 1
    ret=0
    for c in "ACGT":
        if ok(last3+c):
            ret=(ret+dfs(cur+1,last3[1:]+c))%mod
    memo[cur][last3]=ret
    return ret
print(dfs(0,"TTT"))
    
"""
d=[[1,1,1,1] for i in range(100)]
d[1]=[4,4,4,4]
d[2]=[16,14,15,16]
for i in range(3,100):
    for j in range(4):
        t=d[i-1][0]+d[i-1][1]+d[i-1][2]+d[i-1][3]
        if j==0 or j==3:
            d[i][0]=t
            d[i][3]=t
        elif j==1:
            d[i][1]=t-(d[i-2][0]+d[i-2][2]+(d[i-3][0]*2))
        else:
            d[i][2]=t-d[i-2][0]
    for j in range(4):
        d[i][j]=abs(d[i][j])%mod
print((d[n-1][0]+d[n-1][1]+d[n-1][2]+d[n-1][3])%mod)
"""

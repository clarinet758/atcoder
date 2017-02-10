#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

IS=float('inf')*-1

n,m,y,z=[int(i) for i in input().split()]
d={}
c,p=[],[]
for i in range(m):
    a,b=input().split()
    c.append(a)
    p.append(int(b))
w=input()

dp=[[IS]*m for i in range(1<<m)]
dp[0][0]=0

for i in range(n):
    num=0
    for j in range(m):
        if c[j]==w[i]:
            num=j
            break
    next_dp=[[dp[i][j] for j in range(m)] for i in range(1<<m)]

    for j in range(1<<m):
        for k in range(m):
            if dp[j][k]==IS:
                continue
            if dp[j][k]<=dp[(1<<m)-1][k]+min(0,z) and j!=(1<<m)-1:
                continue

            next_dp[j][k]=max(next_dp[j][k],dp[j][k])

            next_i=j|(1<<num)
            next_score=dp[j][k]

            next_score+=p[num]

            if j!=0 and k==num:
                next_score+=y

            next_dp[next_i][num]=max(next_dp[next_i][num],next_score)
    dp=[[next_dp[j][k] for k in range(m)] for j in range(1<<m)]
ret=IS

for i in range((1<<m)-1):
    for j in range(m):
        if dp[i][j]==IS:
            continue
        ret=max(ret,dp[i][j])

for i in range(m):
    if dp[(1<<m)-1][i]==IS:
        continue
    ret=max(ret,dp[(1<<m)-1][i]+z)

print(ret)


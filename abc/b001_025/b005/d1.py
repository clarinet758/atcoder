#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
dp=[0]*(n*n+1)
l=[]

for i in range(n):
    tmp=map(int,raw_input().split())
    dp[1]=max(dp[1],max(tmp))
    l.append(tmp)
b=[[0 for i in range(n)] for j in range(n)]
tmp=l[0][0]
b[0][0]=tmp
for i in range(1,n):
    b[0][i]=b[0][i-1]+l[0][i]
for i in range(1,n):
    b[i][0]=b[i-1][0]+l[i][0]
for i in range(1,n):
    for j in range(1,n):
        b[i][j]=b[i-1][j]+b[i][j-1]+l[i][j]-b[i-1][j-1]

q=int(raw_input())
chk=[]
for i in range(q):
    chk.append(int(raw_input()))

for i in range(n):
    for j in range(n):
        for y in range(i,n):
            for x in range(j,n):
                w=(y-i+1)*(x-j+1)
                if i==j==0:
                    dp[w]=max(dp[w],b[y][x])
                elif i==0:
                    dp[w]=max(dp[w],b[y][x]-b[y][j-1])
                elif j==0:
                    dp[w]=max(dp[w],b[y][x]-b[i-1][x])
                else:
                    dp[w]=max(dp[w],b[y][x]+b[i-1][j-1]-b[i-1][x]-b[y][j-1])
tmp=dp[1]
for i in range(1,n*n+1):
    dp[i]=tmp=max(tmp,dp[i])
for i in chk:
    print dp[i]

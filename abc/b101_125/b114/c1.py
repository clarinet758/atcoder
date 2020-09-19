#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def f(a,b):
#a=7,5,3  b=0-7
#no=0, 3=1, 5=2, 7=4, all=7
    if a==7 and b>=4: return b
    if a==7 and b<4: return b+4
    if a==5 and b in (2,3,6,7): return b
    if a==5 and b not in (2,3,6,7): return b+2
    if a==3 and b in (1,3,5,7): return b
    if a==3 and b not in (1,3,5,7): return b+1

n=input()

#a,b=map(int, input().split())
#print(f(a,b))
l=[int(i) for i in "0"+n]
dp=[[[0]*9,[0]*9] for _ in "ww"]
dp[0][0][0]=1

chk=(7,5,3)
for i,j in enumerate(l):
    if i==0: continue
    elif i==1:
        if j in chk: dp[i%2][0][f(j,0)]=1
        if j not in chk: dp[i%2][0][0]=1
        if j>7: dp[i%2][1][4]+=1
        if j>5: dp[i%2][1][2]+=1
        if j>3: dp[i%2][1][1]+=1
        dp[i%2][1][0]=1
    else:
        dp[i%2][1][0]=1
        dp[i%2][1][4]+=1
        dp[i%2][1][2]+=1
        dp[i%2][1][1]+=1
        for k in range(8):
            if dp[i%2-1][0][k] and (k==0 or j not in chk): dp[i%2][0][0]=1
            elif dp[i%2-1][0][k] and j in chk: dp[i%2][0][f(j,k)]=1

            if dp[i%2-1][0][k] and k!=0:
                if j>7: dp[i%2][1][f(7,k)]+=1
                if j>5: dp[i%2][1][f(5,k)]+=1
                if j>3: dp[i%2][1][f(3,k)]+=1
            if dp[i%2-1][1][k] and k!=0:
                dp[i%2][1][f(7,k)]+=dp[i%2-1][1][k]
                dp[i%2][1][f(5,k)]+=dp[i%2-1][1][k]
                dp[i%2][1][f(3,k)]+=dp[i%2-1][1][k]
    for k in range(9):
        dp[i%2-1][0][k]=0
        dp[i%2-1][1][k]=0

print(dp[0][0][7]+dp[0][1][7]+dp[1][0][7]+dp[1][1][7])

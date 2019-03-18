#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#syakyo https://atcoder.jp/contests/dp/submissions/3956913
s=input()
t=input()

dp=[[0]*len(s) for i in range(len(t))]
dp[0][0]=0

for i in range(len(t)):
    for j in range(len(s)):
        if s[j]==t[i]:
            if i==0 or j==0:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
ans=""
j=len(t)-1
i=len(s)-1

while 1:
    if j==0:
        if dp[0][i]==1:
            ans+=t[0]
        break
    if i==0:
        if dp[j][0]==1:
            ans+=s[0]
        break
    else:
        if dp[j][i]==dp[j-1][i]:
            j-=1
        elif dp[j][i]==dp[j][i-1]:
            i-=1
        else:
            ans+=t[j]
            j-=1
            i-=1
print(ans[::-1])

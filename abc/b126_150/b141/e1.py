#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
n=int(input())
s=input()
w=[[0]*n for i in range(n)]
ans=chk=0
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if s[i]==s[j]:
            if i==n-1 or j==n-1:
                w[i][j]=1
            else:
                w[i][j]=w[i+1][j+1]+1
for i in range(1,n):
    for j in range(i):
        ans=max(ans,w[i][j]-[0,w[i][j]-(i-j-w[i][j]+1)][j+w[i][j]>=i+1])
print(ans)

if __name__=="__main__":
    sol()

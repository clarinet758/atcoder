#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n=int(input())
a=[int(i) for i in input().split()]
w=[0]*n
for i in range(n-1,-1,-1):
    cnt=0
    for j in range(i,n,i+1):
        cnt+=w[j]
    if cnt%2!=a[i]:
        w[i]=1
print(w.count(1))
if w.count(1):
    ans=[]
    for i in range(n):
        if w[i]==1:
            ans.append(i+1)
    print(*ans)

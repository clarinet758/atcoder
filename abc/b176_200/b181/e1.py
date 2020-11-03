#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import bisect

f=10000000001
n,m=map(int,input().split())
h=[int(i) for i in input().split()]
w=[int(i) for i in input().split()]
h.sort()
at,bt=[0],[0]

for i in range(0,n-1,2):
    at.append(at[-1]+h[i+1]-h[i])
for i in range(1,n-1,2):
    bt.append(bt[-1]+h[i+1]-h[i])

ans=sum(at)*2+f
for i in w:
    x=bisect.bisect_right(h,i)
    if x==0:
        ans=min(ans,bt[-1]+h[0]-i)
    elif x==n:
        ans=min(ans,at[-1]+i-h[-1])
    elif x%2:
        ans=min(ans,i-h[x-1]+at[x//2]+bt[-1]-bt[x//2])
    else:
        ans=min(ans,h[x]-i+at[x//2]+bt[-1]-bt[x//2])

print(ans)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,x=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()
ans=chk=0
for i in a:
    if x>=i:
        ans+=1
        x-=i
    else:
        x=0
if (x>0): ans=max(0,ans-1)
print(ans)

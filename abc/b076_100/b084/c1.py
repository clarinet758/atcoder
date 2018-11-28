#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
c=[]
for i in range(n-1):
    x,y,z=map(int,input().split())
    c.append((x,y,z))
for i in range(n-1):
    ans=0
    for j in range(i,n-1):
        ans=[c[j][1]+((ans-c[j][1]+c[j][2]-1)//c[j][2])*c[j][2],c[j][1]][ans<c[j][1]]
        ans+=c[j][0]
    print(ans)
ans=chk=0
print(ans)

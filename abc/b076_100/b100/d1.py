#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
l000=[]
l001=[]
l010=[]
l100=[]
for i in range(n):
    x,y,z=map(int,input().split())
    l000.append((x+y+z,x,y,z))
    l001.append((x+y-z,x,y,z))
    l010.append((x-y+z,x,y,z))
    l100.append((-x+y+z,x,y,z))
l000.sort()
l001.sort()
l010.sort()
l100.sort()
dx=[0]*8
dy=[0]*8
dz=[0]*8
for i in range(m):
    dx[0]+=l000[i][1]
    dy[0]+=l000[i][2]
    dz[0]+=l000[i][3]
    dx[1]+=l000[-i-1][1]
    dy[1]+=l000[-i-1][2]
    dz[1]+=l000[-i-1][3]
    dx[2]+=l001[i][1]
    dy[2]+=l001[i][2]
    dz[2]+=l001[i][3]
    dx[3]+=l001[-i-1][1]
    dy[3]+=l001[-i-1][2]
    dz[3]+=l001[-i-1][3]
    dx[4]+=l010[i][1]
    dy[4]+=l010[i][2]
    dz[4]+=l010[i][3]
    dx[5]+=l010[-i-1][1]
    dy[5]+=l010[-i-1][2]
    dz[5]+=l010[-i-1][3]
    dx[6]+=l100[i][1]
    dy[6]+=l100[i][2]
    dz[6]+=l100[i][3]
    dx[7]+=l100[-i-1][1]
    dy[7]+=l100[-i-1][2]
    dz[7]+=l100[-i-1][3]
ans=abs(dx[-1])+abs(dy[-1])+abs(dz[-1])
for i in range(7):
    ans=max(ans,abs(dx[i])+abs(dy[i])+abs(dz[i]))
print(ans)

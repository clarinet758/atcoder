#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def cnt(x,y):
    z=set([])
    while x>0:
        z.add(x%10)
        x//=10
    if len(z)<=y: return 1
    else: return 0

qq=9999999999999999
a,k=map(str,input().split())
k=int(k)
a="0"+a
l=[int(i) for i in a]
dp=[1,0,-1]
s=0
for i,j in enumerate(l):
    p=dp[0]*10
    q=dp[1]*10
    r=dp[2]*10
    s=s*10+j
# make 0
    tmp=[qq]*2
    for m in range(9,-1,-1):
        pm=p+m
        if q!=-10:qm=q+m
        else: qm=qq+m
        if pm>s and cnt(pm,k) and abs(tmp[0]-s)>abs(pm-s): tmp[0]=pm
        if qm>s and cnt(qm,k) and abs(tmp[1]-s)>abs(qm-s): tmp[1]=qm
    if abs(tmp[0]-s)<abs(tmp[1]-s): dp[0]=tmp[0]
    else: dp[0]=tmp[1]
# make 1
    if dp[1]!=-1:
        if cnt(q+j,k): dp[1]=q+j
        else: dp[1]=-1
# make 2
    tmp=[qq]*2
    for m in range(10):
        rm=r+m
        if q!=-10:qm=q+m
        else: qm=qq+m

        if rm<s and cnt(rm,k) and abs(tmp[0]-s)>abs(rm-s): tmp[0]=rm
        if qm<s and cnt(qm,k) and abs(tmp[1]-s)>abs(qm-s): tmp[1]=qm
    if abs(tmp[0]-s)<abs(tmp[1]-s): dp[2]=tmp[0]
    else: dp[2]=tmp[1]

a=int(a) 
ans=[abs(i-a) for i in dp if i!=-1 ]
print(min(ans))

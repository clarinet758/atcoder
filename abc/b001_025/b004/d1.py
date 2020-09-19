#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol(f):
    s="0"+str(f)
    l=[int(i) for i in s]
    dp1=[0]*len(s)
    dp2=[0]*len(s)
    for i,j in enumerate(l):
        if j not in [4,9]:
            dp1[i]=1
        else:
            break
    for i,j in enumerate(l):
        if i==0: continue
        x=y=0
        if dp1[i]==1 or dp1[i-1]+dp1[i]==1:
            y=l[i]-(l[i]>4)
        dp2[i]=(dp2[i-1]*8)+(x*8)+y
    return f-(dp1[-1]+dp2[-1]-1)
            
a,b=map(int,input().split())
print(sol(b)-sol(a-1))

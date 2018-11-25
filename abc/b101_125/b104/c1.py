#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
d,g=map(int,input().split())
g//=100
l={}
t=[]
cnt=ans=0
for i in range(d):
    p,c=map(int,input().split())
    c//=100
    l[i+1]=[p,c]
    t.append((i+1)*p+c)
    ans+=p

for i in range(1<<d):
    x=[0,0,0]
    for j in range(d):
        if (i&(1<<j)):
            x[0]+=l[j+1][0]
            x[1]+=t[j]
        else:
            x[2]=j
    if x[1]>=g:
        ans=min(ans,x[0])
    elif ((g-x[1])+x[2])//(x[2]+1)<=l[x[2]+1][0]:
        ans=min(ans,x[0]+((g-x[1])+x[2])//(x[2]+1))
print(ans)
        

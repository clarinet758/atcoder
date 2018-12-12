#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
o,e=[],[]
ot,et=[0]*n,[0]*n
for i in range(n):
    if i%2:
        o.append(a[i])
        e.append(0) 
    else:
        e.append(a[i])
        o.append(0)
    if i==0:
        ot[0]=o[0]
        et[0]=e[0]
    else:
        ot[i]=ot[i-1]+o[i]
        et[i]=et[i-1]+e[i]

if min(a)<0: ans=min(a)*n
else: ans=0
for i in range(n):
    chk=[0]*3
    for j in range(n):
        if i==j: continue
        if i<j:
            if i%2:
                t=sum(e[i:j+1])
                b=sum(o[i:j+1])
                if chk[2]==0 or b>chk[1]:
                    chk=[t,b,1]
            else:
                t=sum(o[i:j+1])
                b=sum(e[i:j+1])
                if chk[2]==0 or b>chk[1]:
                    chk=[t,b,1]
        else:
            if j%2:
                t=sum(e[j:i+1])
                b=sum(o[j:i+1])
                if chk[2]==0 or b>chk[1]:
                    chk=[t,b,1]
            else:
                print(i,j,)
                t=sum(o[j:i+1])
                b=sum(e[j:i+1])
                if chk[2]==0 or b>chk[1]:
                    chk=[t,b,1]
        ans=max(ans,chk[0])
print(ans)

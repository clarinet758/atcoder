#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
o,e=[],[]
for i in range(n):
    if i%2:
        e.append(a[i])
        o.append(0) 
    else:
        o.append(a[i])
        e.append(0)

if min(a)<0: ans=min(a)*n
else: ans=0
for i in range(n):
    chk=[0]*3
    for j in range(n):
        if i==j: continue
        elif i<j:
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
        elif i>j:
            if j%2:
                t=sum(e[j:i+1])
                b=sum(o[j:i+1])
                if chk[2]==0 or b>chk[1]:
                    chk=[t,b,1]
            else:
                t=sum(o[j:i+1])
                b=sum(e[j:i+1])
                if chk[2]==0 or b>chk[1]:
                    chk=[t,b,1]
    ans=max(ans,chk[0])
print(ans)

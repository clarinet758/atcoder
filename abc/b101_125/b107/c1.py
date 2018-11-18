#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
x=[int(i) for i in input().split()]
l,r=[],[]
for i in range(n):
    if x[i]<0 and i+1<n: l.append(abs(x[i]-min(x[i+1],0)))
    elif x[i]<0: l.append(-x[i])
    if x[i]>=0 and i>0: r.append(x[i]-max(0,x[i-1]))
    elif x[i]>=0: r.append(x[i])

l=l[::-1]
l=l[:k]
r=r[:k]

ll=len(l)
rr=len(r)
lx=sum(l)
rx=sum(r)

if ll<k: lx=lx*2+sum(r[:(k-ll)])
if rr<k: rx=rx*2+sum(l[:(k-rr)])
ans=min(lx,rx)
o=[ll,[0,k-ll][ll<k]]
p=[rr,[0,k-rr][rr<k]]


for i in range(1,k):
    if o[1]==0: lx*=2
    if p[1]==0: rx*=2
    if o[1]+1<=rr and o[0]>0:
        lx-=l[o[0]-1]*2
        lx+=r[o[1]]
        o[0]-=1
        o[1]+=1
        ans=min(ans,lx)
    if p[1]+1<=ll and p[0]>0:
        rx-=r[p[0]-1]*2
        rx+=l[p[1]]
        p[0]-=1
        p[1]+=1
        ans=min(ans,rx)
print(ans)


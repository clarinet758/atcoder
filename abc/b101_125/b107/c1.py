#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
x=[int(i) for i in input().split()]
l,r=[],[]
for i in x:
    if i<0: l.append(-i)
    if i>=0: r.append(i)
l.sort()
r.sort()
l=l[:n]
r=r[:n]
ll=len(l)
rr=len(r)
lx,rx=[],[]
for i in range(ll):
    if i==0: lx.append(l[i])
    else: lx.append(l[i]-l[i-1])
for i in range(rr):
    if i==0: rx.append(r[i])
    else: rx.append(r[i]-r[i-1])

ans=sum(lx)*2+sum(rx)*2
for i in range(ll):
    if n-1==i: ans=min(ans,sum(lx))
    elif i+rr+1>=n: ans=min(ans,sum(lx[:i+1])*2+sum(rx[:n-i]))
    print("#",lx[:i+1],rx[:n-i])

print(ans)
for i in range(rr):
    if n-1==i: ans=min(ans,sum(r))
    elif i+ll+1>=n: ans=min(ans,sum(rx[:i+1])*2+sum(lx[:n-i]))
    print("#",rx[:i+1],lx[:n-i])

print(ans)
    #if i+rr+1>=n and i+1<n:

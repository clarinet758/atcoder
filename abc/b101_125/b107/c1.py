#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#WAA TLEEEEEEEEEE
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

ans=sum(l)*2+sum(r)*2
if ll==k: ans=min(ans,sum(l))
if rr==k: ans=min(ans,sum(r))
for i in range(1,k):
    if rr>=k-(ll-i): ans=min(ans,(sum(l[:-i])*2)+sum(r[:k-(ll-i)]))
    if ll>=k-(rr-i): ans=min(ans,(sum(r[:-i])*2)+sum(l[:k-(rr-i)]))

print(ans)

"""
    print(rr,i,"#",len(l[:-i]),i,k)
    if k-1==i: ans=min(ans,sum(l))
    elif i+rr+1>=k: ans=min(ans,sum(l[:i+1])*2+sum(r[:k-i-1]))
    if k-1==i: ans=min(ans,sum(r))
    elif i+ll+1>=k: ans=min(ans,sum(r[:i+1])*2+sum(l[:k-i-1]))

exit()
for i in range(ll):
    if k-1==i: ans=min(ans,sum(l))
    elif i+rr+1>=k: ans=min(ans,sum(l[:i+1])*2+sum(r[:k-i-1]))

for i in range(rr):
    if k-1==i: ans=min(ans,sum(r))
    elif i+ll+1>=k: ans=min(ans,sum(r[:i+1])*2+sum(l[:k-i-1]))
print(ans)
    #if i+rr+1>=n and i+1<n:
   # print(l[:i+1],r[:k-i-1])
    #print(r[:i+1],l[:k-i-1])
"""

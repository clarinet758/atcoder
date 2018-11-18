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

"""
-30 -10 10 20 50
print(o)
print(p)
[2, 1]
[3, 0]
"""

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

#    if rr>=k-(ll-i): ans=min(ans,(sum(l[:-i])*2)+sum(r[:k-(ll-i)]))
#    if ll>=k-(rr-i): ans=min(ans,(sum(r[:-i])*2)+sum(l[:k-(rr-i)]))


"""
print(l)
print(r)
exit()
    if ll-i>0 and i<=rr and min(i,rr)+(ll-i)>=k:
        rx=rx-(r[-i]*2)+l[i-1]
        ans=min(ans,rx)
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

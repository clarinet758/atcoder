#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

n,a,b=map(int,raw_input().split())
v=[int(i) for i in raw_input().split()]
chk=[i for i in set(v)]
chk.sort()
if len(chk)==1:
    print chk[0]*1.0
    print sum(pscl(n)[a:b+1])
    exit()
d={}
for i in v:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
total=ans=tmp=0
t=a
for p,i in enumerate(chk[::-1]):
    if d[i]<t:
        total=total+i*d[i]
        t=t-d[i]
    elif p==0 and d[i]>=t:
        print i*1.0
        print sum(pscl(d[i])[a:min(b,d[i])+1])
        break
    else:
        total=total+i*t
        print total*1.0/a
        print pscl(d[i])[t]
        break

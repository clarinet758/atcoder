#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,a,b=map(int,raw_input().split())
ans=chk=0
for i in range(n):
    s,d=map(str,raw_input().split())
    d=int(d)
    if a>d: d=a
    if b<d: d=b
    if s[0]=='E':
        ans+=d
    else:
        ans-=d
print 'East {}'.format(abs(ans)) if ans>0 else 'West {}'.format(abs(ans))  if ans<0 else 0


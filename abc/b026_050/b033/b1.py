#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
d={}
ans=chk=0
for i in range(n):
    s,p=map(str,raw_input().split())
    p=int(p)
    if s in d:
        d[s]+=p
    else:
        d[s]=p
    ans=max(ans,d[s])
    chk+=p
if ans>=chk/2+1:
    for i in d:
        if d[i]==ans:
            print i
            break
else:
    print 'atcoder'

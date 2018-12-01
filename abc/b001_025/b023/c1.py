#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

r,c,k=map(int,input().split())
n=int(input())
d={}
x=[0]*c
y=[0]*r
ans=0
for i in range(n):
    a,b=map(int,input().split())
    a-=1
    b-=1
    x[b]+=1
    y[a]+=1
    if a in d: d[a].add(b)
    else: d[a]=set([b])

s={}
for a,i in enumerate(x):
    if i in s: s[i].add(a)
    else: s[i]=set([a])

for a,i in enumerate(y):
    i=k-i
    if i in s:
        #ans+=len(s[i])-[0,1][len(s[i]&d[a])]
        ans+=len(s[i])
        #if a in d:ans-=[0,1][len(s[i]&d[a])]
        if a in d:ans-=len(s[i]&d[a])
    if i+1 in s and a in d and len(s[i+1]&d[a]):
        ans+=len(s[i+1]&d[a])
print(ans)

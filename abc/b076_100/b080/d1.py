#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,c=map(int,input().split())
d=[[] for i in range(c)]
w=[0]*100002
for i in range(n):
    s,t,x=map(int,input().split())
    d[x-1].append((s,t))
for i in range(c):
    d[i].sort()
    e=0
    for j in range(len(d[i])):
        if len(d[i])==1:
            w[d[i][0][0]]+=1
            w[d[i][0][1]+1]-=1
        elif j==0:
            w[d[i][0][0]]+=1
            e=d[i][0][1]
        elif j+1==len(d[i]):
            if e!=d[i][j][0]:
                w[e+1]-=1
                w[d[i][j][0]]+=1
            w[d[i][j][1]+1]-=1
        else:
            if e!=d[i][j][0]:
                w[e+1]-=1
                w[d[i][j][0]]+=1
            e=d[i][j][1]
ans=chk=0
for i in w:
    chk+=i
    ans=max(ans,chk)
print(ans)

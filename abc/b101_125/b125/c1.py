#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
d={}
for i,j in enumerate(a):
    if i<2:
        k=1
        while 1:
            if k*k>j: break
            if j%k==0:
                if k in d:
                    d[k]+=1
                else:
                    d[k]=1
            if j%k==0 and k*k!=j:
                if j//k in d:
                    d[j//k]+=1
                else:
                    d[j//k]=1
            k+=1
    else:
        for k in d:
            if j%k==0:
                if k in d:
                    d[k]+=1
            elif j%k==0 and k*k!=j:
                if j//k in d:
                    d[j//k]+=1
#print(d)
ans=chk=0
for i in d:
    if d[i]>=n-1:
        ans=max(ans,i)
print(ans)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k,q=map(int,input().split())
ans=[0]*n
for i in range(q):
    a=int(input())
    ans[a-1]+=1
for i in ans:
    print(["No","Yes"][i>q-k])

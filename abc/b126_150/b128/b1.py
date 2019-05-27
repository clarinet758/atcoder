#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=[]
for i in range(n):
    s,p=map(str,input().split())
    ans.append((s,int(p)*-1,i+1))
ans.sort()
for i in ans: print(i[2])

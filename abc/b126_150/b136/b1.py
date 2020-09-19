#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
ans=0
for i in range(1,n+1):
    if len(str(i))%2: ans+=1
print(ans)

#print(len([i for i in range(1,int(input())+1) if len(str(i))%2]))

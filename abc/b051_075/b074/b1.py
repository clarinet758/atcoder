#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
k=int(input())
x=[int(i) for i in input().split()]
ans=chk=0
for i in x:
    ans+=min(i,abs(i-k))
print(ans*2)

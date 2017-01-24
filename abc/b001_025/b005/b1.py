#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
ans=101
for i in range(n):
    ans=min(ans,int(raw_input()))
print ans

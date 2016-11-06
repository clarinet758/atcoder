#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s=raw_input()
n=int(raw_input())
ans=chk=0
for i in range(len(s)):
    for j in range(len(s)):
        chk+=1
        if chk==n:
            print s[i]+s[j]

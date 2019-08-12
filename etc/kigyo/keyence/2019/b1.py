#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
ans=0
t="keyence"
if s[:7]==t or s[-7:]==t:
    ans=1
for i in range(1,7):
    if s[:i]==t[:i] and s[-7+i:]==t[-7+i:]:
        ans=1
print(["NO","YES"][ans])

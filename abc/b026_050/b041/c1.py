#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
a=map(int,raw_input().split())
l={i:a+1 for a,i in enumerate(a)}
a.sort()
for i in a[::-1]:
    print l[i]


#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
l=[2,1]
for i in range(85):
    l.append(l[-1]+l[-2])
n=int(input())
print(l[n])

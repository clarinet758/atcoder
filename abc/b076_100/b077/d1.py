#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,z,w=map(int,input().split())
a=[int(i) for i in input().split()]
if n>1:
    print(max(abs(a[-2]-a[-1]),abs(w-a[-1])))
else:
    print(abs(w-a[-1]))

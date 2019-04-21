#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a=[int(i) for i in input().split()]
a.sort()
print("YES" if a[0]==a[1]==5 and a[2]==7 else "NO")

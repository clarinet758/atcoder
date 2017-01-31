#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=input()
w=set()
for i in range(n):
    w.add(input())
w.remove(max(w))
print max(w)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
k=int(input())
w=k%len(s)
print(s[w:]+s[:w])

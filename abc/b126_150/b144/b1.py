#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=set([i*j for i in range(1,10) for j in range(1,10)])
print("Yes" if n in d else "No")

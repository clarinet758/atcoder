#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a=[int(i) for i in input().split()]
a.sort()
print(a[0] if a[1]==a[2] else a[2])

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

int(input())
a=[int(i) for i in input().split()]
b=[abs(int(i)) for i in a]
c=[int(i) for i in a if i<0]
print(sum(b)-[0,min(b)*2][len(c)%2])


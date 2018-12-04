#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=input()
x=0
for i in n:
    x+=int(i)
print(x if int(n)%10 else 10)

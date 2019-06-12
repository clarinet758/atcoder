#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import fractions
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(fractions.gcd(a,b))

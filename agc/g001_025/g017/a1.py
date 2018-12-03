#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,p=map(int,input().split())
a=len([i for i in input().split() if int(i)%2])
print(2**(n-1) if a else 2**n if p==0 else 0)

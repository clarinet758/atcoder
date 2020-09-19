#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,a,b=map(int,input().split())
print(0 if a==0 else (n//(a+b)*a)+min(n%(a+b),a))

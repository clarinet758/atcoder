#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pscl 要修正
a,b=map(int,input().split())
"""
if (a*b)%2:
    print("Odd")
else:
    print("Even")
#print(["Even","Odd"][a*b%2])
#print("Odd" if a*b%2 else "Even")
"""
print("Even" if a%2==0 else "Even" if b%2==0 else "Odd")

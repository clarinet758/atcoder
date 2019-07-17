#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
t=(n-1)//20
print([21-(n%20),1][n%20==0] if t%2 else [n%20,20][n%20==0])

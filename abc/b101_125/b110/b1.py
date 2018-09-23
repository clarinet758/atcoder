#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#n=int(input())
n,m,a,b=list(map(int,input().split()))
#n,m,a,b=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
print("No War" if (max(x)<min(y) and a<b and a<min(y) and b>max(x)) else "War")

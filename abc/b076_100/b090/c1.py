#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,m=map(int,input().split())
print(1 if n==m==1 else max(n,m)-2 if min(n,m)==1 else (n-2)*(m-2))

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
print([0,1][n%k!=0])

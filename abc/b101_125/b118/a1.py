#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
print([b-a,a+b][b%a==0])

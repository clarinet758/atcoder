#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,t=map(int,input().split())
chk=b-a
print(((t-a+chk-1)//chk)*chk+a)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
chk=0
while 1:
    if int((n+chk)**0.5)**2==n+chk: break
    chk+=1
print(chk)

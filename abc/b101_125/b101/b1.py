#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
tmp=n
chk=0
while tmp:
    chk+=tmp%10
    tmp//=10
print("No" if n%chk else "Yes")

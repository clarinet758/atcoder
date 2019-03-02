#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=int(input())

chk=s
d={s:0}
for i in range(130):
    if chk%2: chk=chk*3+1
    else: chk//=2
    if chk in d:
        print(i+2)
        break
    else:
        d[chk]=0
        

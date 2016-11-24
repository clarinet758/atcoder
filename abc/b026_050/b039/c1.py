#!/usr/bin/env python
# -*- coding: UTF-8 -*-

k='WBWBWWBWBWBW'*4
d={0:'Do',2:'Re',4:'Mi',5:'Fa',7:'So',9:'La',11:'Si'}
s=raw_input()
for i in range(20):
    if s==k[i:i+20]:
        print d[i]
        break

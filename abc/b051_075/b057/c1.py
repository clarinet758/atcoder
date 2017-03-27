#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import math
n=int(input())
tmp=math.ceil(n**0.5)+1
ans=1000000
for i in range(1,tmp):
    if n%i==0:
        tmp=n//i
        ans=min(ans,len(str(tmp)))

print(ans)

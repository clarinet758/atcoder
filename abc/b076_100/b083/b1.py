#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n,a,b=map(int,input().split())
chk=0
ans=[]
for i in range(1,n+1):
    chk=i%10
    tmp=10000
    p=i
    for j in range(4):
        chk+=i//tmp
        i%=tmp
        tmp//=10
    if a<=chk<=b: ans.append(p)
    
print(sum(ans))

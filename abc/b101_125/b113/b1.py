#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
t,a=map(int,input().split())
h=[int(i) for i in input().split()]
ans=[0,abs(a-(t-h[0]*0.006))]
for i in range(1,n):
    tmp=abs(a-(t-h[i]*0.006))
    if tmp<ans[1]: ans=[i,tmp]
print(ans[0]+1)

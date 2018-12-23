#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
def pd(x):
  i = 2
  table = []
  while i * i <= x:
    while x % i == 0:
      x //= i
      table.append(i)
    i += 1
  if x > 1:
    table.append(x)
  return table

n,p=map(int,input().split())
if n==1 or p==1:
    print(p)
    exit()
l=pd(p)
ans=1
r={}
for i in l:
    while p%i==0:
        if i in r: r[i]+=1
        else: r[i]=1
        p//=i
    if i>=p: break
for i in r:
    if (r[i]//n)>0: ans*=(i**(r[i]//n))
print(r)
print(ans)


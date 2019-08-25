#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# from https://atcoder.jp/contests/abc133/submissions/6272850
n=int(input())
a=[int(i) for i in input().split()]
c=[0]
s=sum(a)

for i in range(2*n):
    print("#",i,(i*2+1)%n)
    c.append(c[-1]+a[(i*2+1)%n])
print(*c)
ans=[0]*n
for i in range(n):
    ans[i*2%n]=s-2*(c[i+n//2]-c[i])
print(*ans)

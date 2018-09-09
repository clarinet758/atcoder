#!/usr/bin/env python3

#import math
import fractions
a,b=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
s=abs(x[-1]-b)
d=set()
for i in range(a-1):
    s=min(s,abs(x[i]-b))
    d.add(x[i+1]-x[i])
if a==1:
    print(abs(b-x[0]))
    exit()
ans=s
while d:
    ans=fractions.gcd(ans,d.pop())
print(ans)


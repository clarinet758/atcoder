#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


ans=chk=0
d=[]
for i in range(5):
    x=int(input())
    if x%10:
        d.append((x%10,x))
    else:
        ans+=x
d.sort(reverse=True)
for i in d:
    ans+=((i[1]+10)//10)*10
if len(d): ans-=10-d[-1][1]%10

print(ans)

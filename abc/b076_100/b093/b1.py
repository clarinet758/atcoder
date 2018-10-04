#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a,b,k=map(int,input().split())
#l=[int(i) for i in input().split()]
#ans=chk=0
ans={a,b}
for i in range(a,min(a+k,b)):
    ans.add(i)
for i in range(b,max(a,b-k),-1):
    ans.add(i)
ans=list(ans)
ans.sort()
for i in ans:
    print(i)


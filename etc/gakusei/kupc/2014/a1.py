#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

l=[int(i) for i in input().split()]
x=["123","132","213","231","312","321"]
ans=6000000
for i in x:
    a,b,c=int(i[0])-1,int(i[1])-1,int(i[2])-1
    ans=min(ans,abs(l[3]-l[a])+abs(l[4]-l[b])+abs(l[5]-l[c]))
print(ans)

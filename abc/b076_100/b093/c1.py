#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#a,b,c=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort()
ans=l[2]-l[1]+(l[1]-l[0])%2*2
#print(ans)
ans+=(l[1]-l[0])//2
print(ans)

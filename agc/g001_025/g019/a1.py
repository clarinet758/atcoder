#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#1,2,4,8
q=[int(i) for i in input().split()]
n=int(input())*4
ans=max(q)*n*4
for i in range(4):
    for j in range(4):
        if i==j and i<3:
            ans=min(ans,[q[0]*n,q[1]*n//2,q[2]*n//4][i])
        elif i==j==3 and n%8==0:
            ans=min(ans,q[3]*n//8)
        elif i==3 and n%8 and j<3:
            t=[q[0]*4,q[1]*2,q[2]][j]
            ans=min(ans,q[3]*(n//8)+t)
print(ans)

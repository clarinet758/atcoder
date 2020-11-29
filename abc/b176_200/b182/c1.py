#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=input()
p=[0]*3
for i in n:
    x=int(i)%3
    p[x]+=1

d=(p[1]+(p[2]*2))%3
if d==0:
    print(0)
elif p[1]>0 and ((p[1]-1)+(p[2]*2))%3==0 and (p[0]+(p[1]-1)+(p[2]*2))>0:
    print(1)
elif p[2]>0 and (p[1]+((p[2]-1)*2))%3==0 and (p[0]+p[1]+((p[2]-1)*2))>0:
    print(1)
elif p[1]>1 and ((p[1]-2)+(p[2]*2))%3==0 and (p[0]+(p[1]-2)+(p[2]*2))>0:
    print(2)
elif p[2]>1 and (p[1]+((p[2]-2)*2))%3==0 and (p[0]+p[1]+((p[2]-2)*2))>0:
    print(2)
else:
    print(-1)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
    
x,y=map(int,input().split())
ans=0
if y==0:
    ans=abs(x)+[0,1][x>0]
elif x==0:
    ans=abs(y)+[0,1][y<0]
elif (x*y)>=0:
    ans=abs(y-x)+[0,2][y-x<0]
else:
    ans=abs(abs(y)-abs(x))+1
print(ans)

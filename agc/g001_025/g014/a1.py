#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
l=[int(i) for i in input().split()]
chk=[0]*3
ans=0
st=100
while st:
    st-=1
    for i in range(3):
        for j in l:
            if j%2:
                print(ans)
                exit()
        if len(set(l))==1:
            print(-1)
            exit()
        chk[i]=l[(i+1)%3]//2+l[(i+2)%3]//2
    l=[i for i in chk]
    chk=[0]*3
    ans+=1
    

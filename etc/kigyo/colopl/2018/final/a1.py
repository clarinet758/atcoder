#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()
d=[]
ans=chk=t=0
for i in s:
    if i=="A":
        chk+=1
    elif i=="B" and chk>0:
        d.append(chk)
        d.append(0)
        chk=0
    elif i=="B" and len(d)==0:
        d.append(0)
if chk>0: d.append(chk)
if d[0]==0 or d[-1]==0:
    for j in d:
        ans+=(j+1)*j//2
    print(ans*n)
    exit()
tmp=[]
if len(d)<6:
    for i in range(n):
        for j in d:
            if j==0:
                ans+=(t+1)*t//2
                t=0
            else:
                t+=j
    ans+=(t+1)*t//2
else:
    tmp.append(d[0])
    tmp.append(0)
    for i in d[2:-2]:
        tmp[-1]+=(i+1)*i//2
    tmp.append(d[-1])
    for i in range(n):
        for j in range(2):
            if i==j==0:
                ans+=(tmp[0]+1)*tmp[0]//2
            elif j==0:
                ans+=(tmp[0]+tmp[2]+1)*(tmp[0]+tmp[2])//2
            elif j==1:
                ans+=tmp[1]
    ans+=(tmp[2]+1)*tmp[2]//2
print(ans)

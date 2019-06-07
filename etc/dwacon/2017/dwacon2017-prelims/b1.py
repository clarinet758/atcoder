#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=input()
p=len(t)
t+="00"
ans=chk=0
for i in range(0,p,2):
    if (t[i]=="2" or t[i]=="?") and (t[i+1]=="5" or t[i+1]=="?"):
        chk+=2
        ans=max(ans,chk)
    else:
        chk=0
chk=0
for i in range(1,p,2):
    if (t[i]=="2" or t[i]=="?") and (t[i+1]=="5" or t[i+1]=="?"):
        chk+=2
        ans=max(ans,chk)
    else:
        chk=0
print(ans)

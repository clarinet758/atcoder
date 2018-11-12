#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
t=input()
a,b={},{}
cnt=1
# osoi
for i in range(len(s)):
    if s[i] not in a and t[i] not in b:
        a[s[i]]=cnt
        b[t[i]]=cnt
        cnt+=1
    elif s[i] in a and t[i] in b and (a[s[i]]==b[t[i]]):
        pass
    else:
        print("No")
        exit()
print("Yes")


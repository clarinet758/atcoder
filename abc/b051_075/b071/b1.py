#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
s=input()
ans=""
for i in range(97,123):
    ans+=chr(i)
for i in s:
    ans=ans.replace(i,"")
print(ans[0] if len(ans) else "None")

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

ans=[0]*6
s=raw_input()
for i in s:
    ans[ord(i)-ord('A')]+=1
print ' '.join(map(str,ans))

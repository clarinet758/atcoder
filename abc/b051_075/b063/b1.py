#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
chk=len(s)
ans=set([i for i in s])
print('yes' if len(ans)==chk else 'no')

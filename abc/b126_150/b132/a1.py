#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=list(input())
s.sort()
print(["No","Yes"][s[0]==s[1] and s[2]==s[3] and s[1]!=s[2]])

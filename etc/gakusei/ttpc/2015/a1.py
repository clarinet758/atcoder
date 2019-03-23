#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s=input()
print("Doctor" if s[2]=="D" else "Master" if s[2]=="M" else "Bachelor",s[:2])

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
input()
l=[int(i) for i in input().split()]
print(["No","Yes"][max(l)<sum(l)-max(l)])

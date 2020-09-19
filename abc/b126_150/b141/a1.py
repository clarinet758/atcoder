#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

ans=["Sunny","Cloudy","Rainy"]
s=input()
print(ans[(ans.index(s)+1)%3])

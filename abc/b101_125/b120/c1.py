#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=input()
print(len(n)-abs(n.count("0")-n.count("1")))

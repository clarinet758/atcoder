#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

l,x=map(int,input().split())
print(x%l if (x//l)%2==0 else l-x%l)

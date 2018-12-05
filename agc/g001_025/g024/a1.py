#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a,b,c,k=map(int,input().split())
print([a-b,b-a][k%2])

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
l=set([i for i in input().split()])
print(["Three","Four"][len(l)==4])

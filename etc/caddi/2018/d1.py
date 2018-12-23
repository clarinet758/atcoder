#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
print(["second","first"][any([int(input())%2 for i in range(n)])])

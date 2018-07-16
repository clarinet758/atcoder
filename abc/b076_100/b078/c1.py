#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
a,b=map(int,input().split())
ans=(1900*b+100*(a-b))*(2**b)
print(ans)

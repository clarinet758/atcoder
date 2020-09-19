#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=1000000007
n=int(input())
#print(0 if n==1 else pow(10,n,mod)-pow(9,n,mod)-pow(9,n,mod)+pow(8,n,mod))
print(0 if n==1 else (pow(10,n)-pow(9,n)-pow(9,n)+pow(8,n))%mod)

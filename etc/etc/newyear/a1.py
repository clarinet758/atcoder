#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=bin(int(input()))[2:]
print(["No","Yes"][n==n[::-1]])

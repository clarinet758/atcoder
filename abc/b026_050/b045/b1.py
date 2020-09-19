#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a=list(input())
b=list(input())
c=list(input())
a=a[::-1]
b=b[::-1]
c=c[::-1]
t="a"

while 1:
    if len(a) and t=="a":
        t=a.pop()
    elif len(b) and t=="b":
        t=b.pop()
    elif len(c) and t=="c":
        t=c.pop()
    else:
        print(["A","B","C"][ord(t)-ord("a")])
        break

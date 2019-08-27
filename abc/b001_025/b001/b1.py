#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

m=int(input())
if m<100:
    print("00");
elif m<=5000:
    print("{0:02}".format(m//100))
elif m<=30000:
    print(m//1000+50)
elif m<=70000:
    print((m//1000-30)//5+80)
else:
    print(89)

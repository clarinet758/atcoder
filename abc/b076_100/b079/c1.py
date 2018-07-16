#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
o=["+","-"]
a,b,c,d=list(input())
for i in o:
    for j in o:
        for k in o:
            t=a+i+b+j+c+k+d
            if eval(t)==7:
                print(t+"=7")
                exit()

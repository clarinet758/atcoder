#!/usr/bin/env python3

n=int(input())
d=set()
m=""
for i in range(n):
    s=input()
    if i>0 and (s in d or s[0]!=m[-1]):
        print("No")
        exit()
    m=s
    d.add(s)
        
print("Yes")

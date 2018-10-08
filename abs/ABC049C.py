#!/usr/bin/env python3

s=input()
s=s.replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
print("NO" if len(s) else "YES")

#print(["YES","NO"][len(input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream",""))>0])

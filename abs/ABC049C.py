#!/usr/bin/env python3

s=input()
s=s[::-1]
#print(s)
#d={""}
#chk0={"dream","dreamer","erase","eraser"}
#chk={"dream","dreamer","erase","eraser"}
s=s.replace("resare","").replace("esare","").replace("remaerd","").replace("maerd","")
print("NO" if len(s) else "YES")
exit()
while(d):
    tmp=d.pop()
    #if tmp+"dream"==s[:len(tmp)+5]: dadd(
    #print(d)
    if tmp==s:
        print("YES")
        exit()
    #for i in chk:
    #    if tmp+i==s[:len(tmp)+len(i)]: d.add(tmp+i)
    #for i in chk:
    #    if tmp+i==s[:len(tmp)+len(i)]: d.add(tmp+i)
    #a=[tmp+i for i in chk if tmp+i==s[:len(tmp)+len(i)]]
    a={tmp+i for i in chk if tmp+i==s[:len(tmp)+len(i)]}
    for i in a:
        d.add(i)
print("NO")


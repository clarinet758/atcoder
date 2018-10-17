
n=int(input())
s=input()
ans=s.count("E")
if s[0]=="E": ans-=1
chk=ans
for a,i in enumerate(s[1:]):
    if i=="E": chk-=1
    if s[a]=="W": chk+=1
    ans=min(ans,chk)
print(ans)


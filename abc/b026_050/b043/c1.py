n=int(input())
a=[int(i) for i in input().split()]
av=sum(a)//n
ans=40000000
for i in range(av-2,av+2):
    chk=0
    for j in a:
        chk+=(i-j)**2
    ans=min(ans,chk)
print(ans)

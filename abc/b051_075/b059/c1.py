n=int(input())
l=[int(i) for i in input().split()]
chk1=ans1=chk2=ans2=0

for a,i in enumerate(l):
    chk1+=i
    chk2+=i
    if a%2:
        if chk1<=0:
            ans1+=1-chk1
            chk1=1
        if chk2>=0:
            ans2+=chk2+1
            chk2=-1
    else:
        if chk1>=0:
            ans1+=1+chk1
            chk1=-1
        if chk2<=0:
            ans2+=1-chk2
            chk2=1
print(min(ans1,ans2))
     

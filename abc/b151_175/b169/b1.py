n=int(input())
v=1000000000000000000
ans=1
a=[int(i) for i in input().split()]
for x in a:
  if(x==0):
    ans=0
    break
  ans*=x
  if(ans>v):
    ans=v+1

if(ans>v):
  print(-1)
else:
  print(ans)
n,q=map(int, input().split())

x=[0]*(n+1)
for i in range(q):
    l,r=map(int, input().split())
    x[l-1]+=1
    x[r]-=1
t=0
ans=""
for i in x:
    t+=i%2
    if t%2: ans+="1"
    else: ans+="0"
print(ans[:n])

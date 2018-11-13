

n,a,b=map(int, input().split())
s=[]
for i in range(n):
    s.append(int(input()))
s.sort()
if s[0]==s[-1]:
    print(-1)
else:
    p=b/(s[-1]-s[0])
    q=a-(p*(sum(s)/n))
    print(p,q)

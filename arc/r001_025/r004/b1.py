n=int(input())
l=[int(input()) for i in range(n)]
s=sum(l)
m=max(l)
print(s)
print(abs(s-m-m) if s-m<=m else 0)

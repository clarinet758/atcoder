n,a=map(int,input().split())
l=[int(i) for i in input().split()]
ans=0
dp=[[[0 for i in range(2501)] for j in range(51)] for k in range(51)]
dp[0][0][0]=1

for i in range(n):
    for j in range(50):
        for k in range(2501):
            if dp[i][j][k]:
                dp[i+1][j][k]+=dp[i][j][k]
                dp[i+1][j+1][k+l[i]]+=dp[i][j][k]
for i in range(1,n+1):
    ans+=dp[n][i][i*a]
print(ans)

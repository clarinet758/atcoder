#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    long long n,w,ans=0;
    scanf("%lld %lld",&n,&w);
    long long dp[n+1][1000*n+1];
    for (int i=0;i<=n;i++) for (int j=0;j<=1000*n;j++) dp[i][j]=mod;
    for (int i=1;i<=n;i++) {
        long long a,b;
        scanf("%lld %lld",&a,&b);
        dp[i][b]=min(dp[i][b],a);
        for (int j=1;j<=1000*n-b;j++) {
            if (dp[i-1][j]<w) {
                dp[i][j]=min(dp[i][j],dp[i-1][j]);
                dp[i][j+b]=min(dp[i][j+b], dp[i-1][j]+a);
            }
        }
    }
    for (int i=0;i<=n;i++) for (long long j=0;j<=1000*n;j++) {
        if (dp[i][j]<=w) {
            ans=max(ans,j);
        }
    }
    printf("%lld\n",ans);
    return 0;
}

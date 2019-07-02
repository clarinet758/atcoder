#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,mod=1000000007;
    scanf("%d",&n);
    vector <int> h(n);
    for (auto&e:h) scanf("%d",&e);
    int dp[n+1];
    for (int i=0;i<n+1;i++) dp[i]=mod;
    dp[1]=0;
    for (int i=1;i<n;i++) {
        dp[i+1]=min(dp[i+1],dp[i]+abs(h[i]-h[i-1]));
        if (i+2<=n) dp[i+2]=min(dp[i+2],dp[i]+abs(h[i+1]-h[i-1]));
    }
    printf("%d\n",dp[n]);
    return 0;
}

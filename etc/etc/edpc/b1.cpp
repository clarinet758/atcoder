#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,k,ans;
    scanf("%d %d",&n,&k);
    vector <int> h(n);
    for (auto&e:h) scanf("%d",&e);
    int dp[n+1];
    for (int i=0;i<=n;i++) dp[i]=mod;
    dp[1]=0;
    for (int i=1;i<n;i++) {
        for (int j=1;j<=k;j++) {
            if (i+j>n) break;
            dp[i+j]=min(dp[i+j],dp[i]+abs(h[i-1]-h[i-1+j]));
        }
    }
    printf("%d\n",dp[n]);
    return 0;
}

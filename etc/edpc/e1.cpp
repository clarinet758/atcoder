#include<bits/stdc++.h>
using namespace std;

int main(){
    int mod=1000000007;
    int n,w,ans=0;
    scanf("%d %d",&n,&w);
    int x=n*1000+1;
    int dp[x];
    for (int i=1;i<x;i++) dp[i]=mod;
    for (int i=0;i<n;i++) {
        int a,b;
        scanf("%d %d",&a,&b);
        for (int j=x-1-b;j>0;j--) if (dp[j]<mod) dp[j+b]=min(dp[j+b],dp[j]+a);
        dp[b]=min(dp[b],a);
    }
    for (int i=x-1;i>0;i--) if (dp[i]<=w) {
        ans=i;
        break;
    }
    printf("%d\n",ans);
    return 0;
}

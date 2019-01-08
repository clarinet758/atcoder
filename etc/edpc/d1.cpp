#include<bits/stdc++.h>
using namespace std;
 
int main(){
    int n,w;
    scanf("%d %d",&n,&w);
    long long dp[w+1]={0};
    long long ans=0;
    for (int i=0;i<n;i++) {
        long long  a,b;
        scanf("%lld %lld",&a,&b);
        for (int j=w-a;j>0;j--) {
            if (dp[j]!=0) dp[j+a]=max(dp[j+a],dp[j]+b);
        }
        dp[a]=max(dp[a],b);
    }
    for (int i=0;i<w+1;i++) ans=max(ans,dp[i]);
    printf("%lld\n",ans);
    return 0;
}

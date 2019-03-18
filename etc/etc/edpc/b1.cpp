#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,k;
    scanf("%d %d",&n,&k);
    int h[n],dp[n];
    for (int i=0;i<n;i++) scanf("%d",&h[i]);
    for (int i=1;i<n;i++) dp[i]=-1;
    dp[0]=0;
    dp[1]=abs(h[1]-h[0]);
    for (int i=2;i<n;i++) for (int j=1;j<=k;j++) {
        if (i-j<0) break;
        if (dp[i]==-1) dp[i]=abs(h[i]-h[i-j])+dp[i-j];
        else dp[i]=min(dp[i],abs(h[i]-h[i-j])+dp[i-j]);
    }
    printf("%d\n",dp[n-1]);
    return 0;
}

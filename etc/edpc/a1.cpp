#include<bits/stdc++.h>
using namespace std;

// 1 3 5 1 8
int main(){
    int n;
    scanf("%d",&n);
    int h[n],dp[n];
    for (int i=0;i<n;i++) scanf("%d",&h[i]);
    for (int i=1;i<n;i++) dp[i]=-1;
    dp[0]=0;
    dp[1]=abs(h[1]-h[0]);
    for (int i=2;i<n;i++) dp[i]=min(abs(h[i]-h[i-1])+dp[i-1],abs(h[i]-h[i-2])+dp[i-2]);
    printf("%d\n",dp[n-1]);
    return 0;
}

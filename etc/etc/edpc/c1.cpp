#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    scanf("%d",&n);
    int m[n][3];
    int dp[n][3];
    for (int i=0;i<n;i++) scanf("%d %d %d",&m[i][0],&m[i][1],&m[i][2]);
    for (int i=0;i<3;i++) dp[0][i]=m[0][i];
    for (int i=1;i<n;i++) for (int j=0;j<3;j++) {
        if (j==0) dp[i][j]=max(dp[i-1][1],dp[i-1][2])+m[i][0];
        if (j==1) dp[i][j]=max(dp[i-1][0],dp[i-1][2])+m[i][1];
        if (j==2) dp[i][j]=max(dp[i-1][0],dp[i-1][1])+m[i][2];
    }
    printf("%d\n",max(dp[n-1][0],max(dp[n-1][1],dp[n-1][2])));
    return 0;
}

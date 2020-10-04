#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int n,ans,mod=1e9+7;
int dp[4][4][4][105];
int main(){
    sc1(n);
    rep(i,4) rep(j,4) rep(k,4) {
        if (((i==0 && j==1 && k==2) || (i==0 && j==2 && k==1) || (i==1 && j==0 && k==2))!=true) {
            dp[i][j][k][3]=1;
        } //0:A 1:G 2:C 3:T
    }     //ACG,  AGC, GAC, A?GC, AG?C
    for (int i=3;i<101;i++) {
        rep(a,4) rep(b,4) rep(c,4){
            if (b==0 && c==2) {
                dp[b][c][0][i+1] = (dp[b][c][0][i+1] + dp[a][b][c][i])%mod;
                dp[b][c][2][i+1] = (dp[b][c][2][i+1] + dp[a][b][c][i])%mod;
                dp[b][c][3][i+1] = (dp[b][c][3][i+1] + dp[a][b][c][i])%mod;
            } else if ((b==0 && c==1) || (b==1 && c==0) || (a==0 && c==1) || (a==0 && b==1)) {
                dp[b][c][0][i+1] = (dp[b][c][0][i+1] + dp[a][b][c][i])%mod;
                dp[b][c][1][i+1] = (dp[b][c][1][i+1] + dp[a][b][c][i])%mod;
                dp[b][c][3][i+1] = (dp[b][c][3][i+1] + dp[a][b][c][i])%mod;
            } else {
                rep(p,4) dp[b][c][p][i+1] = (dp[b][c][p][i+1] + dp[a][b][c][i])%mod;
            }
        }
    }
    int ans=0;
    rep(i,4) rep(j,4) rep(k,4) ans=(ans+dp[i][j][k][n])%mod;
    printf("%d\n",ans);
    return 0;
}

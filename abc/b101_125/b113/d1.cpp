#include<bits/stdc++.h>
using namespace std;
/// from  https://atcoder.jp/contests/abc113/submissions/3540482

int main(){
    const int mod=1000000007;
    int h,w,k;
    scanf("%d %d %d",&h,&w,&k);
    vector<vector<int>> dp(h+1,vector<int>(w,0));
    dp[0][0]=1;
    for (int i=0;i<h;i++) {
        for (int j=0;j<w;j++) {
            for (int kk=0;kk<1<<(w-1);kk++) {
                bool ok=true;
                for (int l=0;l<w-2;l++) {
                    if (((kk>>l)&1) && ((kk>>(l+1))&1)) ok=false;
                }
                if (ok) {
                    if (j>=1 && ((kk>>(j-1))&1)) {
                        dp[i+1][j-1]+=dp[i][j];
                        dp[i+1][j-1]%=mod;
                    } else if (j<=w-2 && ((kk>>j)&1)) {
                        dp[i+1][j+1]+=dp[i][j];
                        dp[i+1][j+1]%=mod;
                    } else {
                        dp[i+1][j]+=dp[i][j];
                        dp[i+1][j]%=mod;
                    }
                }
            }
        }
    }
    printf("%d\n",dp[h][k-1]);
    return 0;
}

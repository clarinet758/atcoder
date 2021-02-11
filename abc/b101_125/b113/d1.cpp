#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int mod=1000000007;
    int h,w,k;
    sc3(h,w,k);
    vector<vector<int> > dp(h+1, vector<int> (w,0)); dp[0][0]=1;
    rep(i,h) rep(j,w) for (int p=0;p < 1<<(w-1);p++)  {
        bool ok=1;
        rep(l,w-2) if (((p>>l) & 1) && ((p>>(l+1)) &1)) ok=0;
        if (ok) {
            if (j>=1 && ((p >> (j-1))&1)) {
                dp[i+1][j-1]+=dp[i][j];
                dp[i+1][j-1]%=mod;
            } else if (j<=w-2 && ((p>>j)&1)) {
                dp[i+1][j+1]+=dp[i][j];
                dp[i+1][j+1]%=mod;
            } else {
                dp[i+1][j]+=dp[i][j];
                dp[i+1][j]%=mod;

            }
        }
    }
    printf("%d\n",dp[h][k-1]);
    return 0;
}

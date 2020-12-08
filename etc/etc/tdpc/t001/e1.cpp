#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

char c[10005];
int dp[10005][2][105];
int main(){
    int mod=1000000007;
    int d,n,m=0,ans=0;
    sc1(d);
    dp[0][0][0]=1;
    scanf("%s",c);
    long p=strlen(c);
    for(long i=0;i<p;i++) {
        int x=c[i]-'0';
        rep(j,101) {
            if (dp[i][0][j]>0 || dp[i][1][j]>0) rep(k,10) {
                    if (k==x) dp[i+1][0][(j+k)%d]+=dp[i][0][j];
                    if (k<x) dp[i+1][1][(j+k)%d]+=dp[i][0][j];
                    dp[i+1][1][(j+k)%d]+=dp[i][1][j];
                    dp[i+1][0][(j+k)%d]%=mod; dp[i+1][1][(j+k)%d]%=mod;
            }
        }
    }
    ans+=dp[p][0][0]; ans+=dp[p][1][0]; ans%=mod;
    printf("%d\n",ans-1);
    return 0;
}

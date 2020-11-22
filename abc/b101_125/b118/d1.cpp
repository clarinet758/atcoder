#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int dp[10][10015];
bool c[15];

int main(){
    int a,n,m;
    sc2(n,m);
    rep(i,m) { sc1(a); c[a]=1; }
    //           1 2 3 4 5 6 7 8 9
    int b[10]={0,2,5,5,4,5,6,3,7,6};
    rep(i,n+3) {
        bool f=0;
        rep(j,10) {
            int x=b[j];
            if (c[j]==0 || (i>0 && dp[0][i]==0)) continue;
            if (dp[0][i]+1>dp[0][i+x]) {
                f=1;
            } else if (dp[0][i]+1==dp[0][i+x]) {
                for (int k=9;k>0;k--) {
                    if ((dp[k][i]+(j==k))>dp[k][i+x]) {f=1; break;}
                    if ((dp[k][i]+(j==k))<dp[k][i+x]) {f=0; break;}
                }
            }
            if (f) {
                for (int k=1;k<10;k++) dp[k][i+x]=dp[k][i];
                dp[0][i+x]=dp[0][i]+1;
                dp[j][i+x]++;
            }
        }
    }
    for (int i=9;i>0;i--) if (dp[i][n]>0) rep(j,dp[i][n]) printf("%d",i);
    puts("");
    return 0;
}

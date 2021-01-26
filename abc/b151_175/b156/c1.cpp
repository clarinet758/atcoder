#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int p[105];
int main(){
    int n,m,ans=1000000007;
    sc1(n);
    rep(i,n) {
        int x;
        sc1(x);
        rep(j,101) {
            p[j]+=(j-x)*(j-x);
        }
    }
    rep(i,100) ans=min(ans,p[i+1]);
    printf("%d\n",ans);
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)

int main(){
    int n,m;
    long long chk,ans=-1ll;
    sc1(n);
    long long  w[30][2];
    rep(i,30) rep(j,2) w[i][j]=0ll;
    rep(i,n) sl2(w[i][0],w[i][1]);
    for (int i=0;i<n;i++) for (int j=0;j<n;j++) {
        chk=0ll;
        for (int k=0;k<n;k++) {
            chk+=abs(w[i][0]-w[k][0])+(w[k][1]-w[k][0])+abs(w[j][1]-w[k][1]);
        }
        if (ans==-1) ans=chk;
        else ans=min(ans,chk);
    }
    printf("%lld\n",ans);
    return 0;
}

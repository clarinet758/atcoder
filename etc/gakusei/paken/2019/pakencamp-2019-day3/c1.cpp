#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,m;
    sc2(n,m);
    int a[100][100];
    long long ans=0ll;
    rep(i,n) rep(j,m) sc1(a[i][j]);
    for (int i=0;i<m-1;i++) for (int j=i+1;j<m;j++) {
        long long chk=0ll;
        rep(k,n) chk+=max(a[k][i],a[k][j]);
        ans=max(ans,chk);
    }
    printf("%lld\n",ans);
    return 0;
}

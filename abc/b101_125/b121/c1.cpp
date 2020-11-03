#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)

vector <pair<long long,long long>> a(100005);

int main(){
    long long n,m;
    long long ans=0ll;
    sl2(n,m);
    rep(i,n) {
        scanf("%lld %lld",&a[i].first,&a[i].second);
        a[i].first*=-1ll;
    }
    sort(a.begin(),a.end());
    for (int i=n-1;i>-1;i--) {
        ans+=(min(m,a[i].second)*(a[i].first*-1))*1ll;
        m-=a[i].second;
        if (m<=0) break;
    }
    printf("%lld\n",ans);
    return 0;
}

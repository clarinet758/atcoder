#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sl1(a)  scanf("%lld",&a)

int main(){
    int x,y,z,k;
    scanf("%d %d %d %d",&x,&y,&z,&k);
    vector<long long> a(x),b(y),c(z);
    rep(i,x) sl1(a[i]);
    rep(i,y) sl1(b[i]);
    rep(i,z) sl1(c[i]);
    sort(a.begin(),a.end(),greater<long long> ());
    sort(b.begin(),b.end(),greater<long long> ());
    sort(c.begin(),c.end(),greater<long long> ());
    vector<long long> w(x*y);
    int p=0;
    rep(i,x) rep(j,y){
        w[p]=a[i]+b[j];
        p++;
    }
    sort(w.begin(),w.end(),greater<long long> ());
    vector<long long> ans(min(x*y,3000)*z);
    p=0;
    for(int i=0;i<min(x*y,3000);i++) for (int j=0;j<z;j++) {
        ans[p]=w[i]+c[j];
        p++;
    }
    sort(ans.begin(),ans.end(),greater<long long> ());
    rep(i,k) printf("%lld\n",ans[i]);
    return 0;
}

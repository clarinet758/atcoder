#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)

int main(){
    int mod=1000000007;
    int n,k;
    sc2(n,k);
    vector<vector<int>> ds(n);
    rep(i,n) {
        int t,d;
        sc2(t,d);
        --t;
        ds[t].push_back(d);
    }
    vector<int> y0,y1;
    rep(i,n) {
        if (ds[i].size() == 0) continue;
        sort(ds[i].begin(),ds[i].end());
        y1.push_back(ds[i].back());
        ds[i].pop_back();
        y0.insert(y0.end(), ds[i].begin(),ds[i].end());
    }
    sort(y0.rbegin(),y0.rend());
    sort(y1.rbegin(),y1.rend());
    long long ans=0;
    int Y=max(0, k-int(y0.size()));
    long long X=0;
    rep(i,Y) X+=y1[i];
    rep(i,k-Y) X+=y0[i];
    while(1) {
        ans=max(ans,X+(long long)Y*Y);
        if (Y>=k || Y>=y1.size()) break;
        X+=y1[Y];
        X-=y0[k-Y-1];
        ++Y;
    }
    printf("%lld\n",ans);
    return 0;
}

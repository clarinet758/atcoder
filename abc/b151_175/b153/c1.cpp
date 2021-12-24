#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sl1(a)  scanf("%lld",&a)

int main(){
    int n,k;
    long long ans=0ll;
    sc2(n,k);
    vector <int> h(n);
    rep(i,n) sc1(h.at(i));
    sort(h.begin(),h.end());
    rep(i,max(0,n-k))  ans+=1ll*h.at(i);
    printf("%lld\n",ans);
    return 0;
}

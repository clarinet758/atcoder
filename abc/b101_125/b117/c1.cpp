#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,m,ans=0;
    sc2(n,m);
    vector <int> a(m);
    vector <int> b;
    rep(i,m) sc1(a[i]);
    sort(a.begin(),a.end());
    rep(i,m-1) b.push_back(a[i+1]-a[i]);
    sort(b.begin(),b.end());
    rep(i,m-n) ans+=b[i];
    printf("%d\n",ans);
    return 0;
}

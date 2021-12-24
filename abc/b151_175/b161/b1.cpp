#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int n,m,x,ans=1;
    sc2(n,m);
    vector <int> a(n);
    rep(i,n) cin >> a.at(i);
    sort(a.begin(),a.end());
    x=accumulate(a.begin(),a.end(),0);
    rep(i,m) if (a.at(n-1-i)*4*m<x) ans=0; 
    printf("%s\n",ans?"Yes":"No");
    return 0;
}

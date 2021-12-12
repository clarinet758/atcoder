#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)


int main(){
    int n,ans=0;
    sc1(n);
    vector <int> p(n);
    vector <int> w(n);
    rep(i,n) sc1(p.at(i));
    rep(i,n) {
        if (i==0) w.at(0)=p.at(0);
        else w.at(i)=min(w.at(i-1),p.at(i));
    }
    rep(i,n) ans+=p.at(i)<=w.at(i);
    printf("%d\n",ans);
    return 0;
}

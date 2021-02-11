#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int mod=1000000007;
    int n,m,chk=-1,ans;
    sc2(n,m);
    vector <pair<int,int>> w;
    vector <pair<int,int>> s;
    map <pair<int,int>,int> t;
    rep(i,m) {
        int a,b;
        sc2(a,b);
        w.push_back({a,b});
        s.push_back({a,b});
    }
    sort(w.begin(),w.end());
    rep(i,m) {
        if (w[i].first!=chk) {
            t[{w[i].first,w[i].second}]=1;
            chk=w[i].first;
        } else {

            t[{w[i].first,w[i].second}]=t[{w[i-1].first,w[i-1].second}]+1;
        }

    }
    rep(i,m) {
        printf("%06d%06d\n",s[i].first,t[{s[i].first,s[i].second}]);
    }
    return 0;
}

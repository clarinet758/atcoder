#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)


int main(){
    int n,m,ans=0;
    vector <vector <int>> w(3,vector <int> (3));
    rep(i,3) rep(j,3) cin >> w.at(i).at(j);
    cin >> n;
    rep(i,n) {
        cin >> m;
        rep(j,3) rep(k,3) if (w.at(j).at(k)==m) w.at(j).at(k)=0;
    }
    rep(i,3) {
        if (w.at(i).at(0)==w.at(i).at(1) && w.at(i).at(1)==w.at(i).at(2) && w.at(i).at(2)==0) ans=1;
        if (w.at(0).at(i)==w.at(1).at(i) && w.at(1).at(i)==w.at(2).at(i) && w.at(2).at(i)==0) ans=1;
    }
    if (w.at(0).at(0)==w.at(1).at(1) && w.at(1).at(1)==w.at(2).at(2) && w.at(2).at(2)==0) ans=1;
    if (w.at(0).at(2)==w.at(1).at(1) && w.at(1).at(1)==w.at(2).at(0) && w.at(2).at(0)==0) ans=1;
    printf("%s\n",ans?"Yes":"No");
    return 0;
}

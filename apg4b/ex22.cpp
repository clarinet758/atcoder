#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,ans;
    sc1(n);
    vector <pair<int,int>> w(n);
    rep(i,n) {
        w.at(i).first=0;
        w.at(i).second=0;
        cin >> w.at(i).second >> w.at(i).first;
    }
    sort(w.begin(),w.end());
    rep(i,n) cout << w.at(i).second << " " << w.at(i).first << endl;

    return 0;
}

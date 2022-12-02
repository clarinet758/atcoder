#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,ans=1;
    sc1(n);
    vector<int> w(n);
    rep(i,n) cin >> w.at(i);
    sort(w.begin(),w.end());
    rep(i,n) if (i>0 && w.at(i)>w.at(i-1)) ans++;
    cout << ans << endl;
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int n;
    string s,t;
    cin >> n;
    cin >> s >> t;
    rep(i,n) cout << s.at(i) << t.at(i);
    puts("");
    return 0;
}

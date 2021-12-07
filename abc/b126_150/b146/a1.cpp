#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int ans=7;
    string s;
    vector <string> w ={"SUN","MON","TUE","WED","THU","FRI","SAT"};
    cin >> s;
    rep(i,7) {
        if (s==w.at(i)) {
            cout << ans-i << endl;
        }
    }
    return 0;
}

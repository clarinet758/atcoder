#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int ans=0,a,b,c,x;
    cin >> a >> b >> c >> x;
    rep(i,a+1) {
        rep(j,b+1) {
            rep(k,c+1) {
                if (500*i+100*j+50*k == x) ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}

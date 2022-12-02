#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int n,m=0,ans=1000000;
    cin >> n;
    rep(i,n) {
        int x;
        cin >> x;
        m=0;
        for(;;) {
            if(x%2) break;
            m++;
            x/=2;
        }
        ans=min(ans,m);
    }
    cout << ans << endl;
    return 0;
}

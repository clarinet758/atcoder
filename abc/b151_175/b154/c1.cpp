#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

bool w[1000000007];

int main(){
    int n;
    cin >> n;
    rep(i,n) {
        int a;
        cin >>a;
        if (w[a]) {
            cout << "NO" << endl;
            return 0;
        }
        w[a]=1;
    }
    cout << "YES" << endl;
    return 0;
}

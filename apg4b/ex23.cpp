#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,ans=0,cnt=0;
    sc1(n);
    map<int, int> w;
    rep(i,n) {
        cin >> m;
        w[m]+=1;
        if (w[m]>cnt) {
            cnt=w[m];
            ans=m;
        }
    }
    cout << ans << " " << cnt << endl;
    return 0;
}

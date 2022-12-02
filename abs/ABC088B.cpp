#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m,a=0,b=0;
    sc1(n);
    vector <int> w(n);
    rep(i,n) cin >> w.at(i);
    sort(w.begin(),w.end());
    rep(i,n) {
        if((i%2==0 && n%2) || (i%2 && n%2==0)) a+=w.at(i);
        else b+=w.at(i);
    }
    cout << a-b << endl;
    return 0;
}

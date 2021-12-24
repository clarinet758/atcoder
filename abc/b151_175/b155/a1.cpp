#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    vector <int> a(3);
    rep(i,3) cin >> a.at(i);
    sort(a.begin(),a.end());
    printf("%s",(a.at(0)!=a.at(2) && (a.at(0)==a.at(1) || a.at(1)==a.at(2)))?"Yes":"No");
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int mod=1000000007;
    int n,ans=0;
    string s;
    cin >> n;
    cin >> s;
    rep(i,n-2) ans+=(s.at(i)=='A' && s.at(i+1)=='B' && s.at(i+2)=='C');
    printf("%d\n",ans);
    return 0;
}

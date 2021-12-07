#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    string s;
    cin >> s;
    int ans=0,p=s.size();
    rep(i,p) {
        ans+=(s.at(i) != s.at(p-i-1));
    }
    printf("%d\n",ans/2);
    return 0;
}

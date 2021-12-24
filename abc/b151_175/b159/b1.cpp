#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

string s;
bool sol(string s,int n) {
    bool p=1;
    rep(i,n) if (s.at(i)!=s.at(n-i-1)) p=0;
    return p;
}

int main(){
    bool ans=1;
    cin >> s;
    int n=s.size();
    ans=sol(s,n);
    if (ans) ans=sol(s,(n-1)/2);
    printf("%s\n",ans?"Yes":"No");
    return 0;
}

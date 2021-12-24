#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int ans=0;
    string s;
    cin >> s;
    rep(i,3) if (s.at(i)=='7') ans=1;
    printf("%s\n",ans?"Yes":"No");
    return 0;
}

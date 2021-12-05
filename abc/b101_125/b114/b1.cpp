#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)

int main(){
    int mod=1000000007;
    char s[15];
    int n,m,ans=mod;
    scanf("%s",s);
    long l=strlen(s);
    rep(i,l) {
        int w=0;
        rep(j,l-i) {
            w*=10;
            w+=s[i+j]-'0';
            if ( w<1000 && w>99) ans=min(ans,abs(w-753));
        }
    }
    printf("%d\n",ans);
    return 0;
}

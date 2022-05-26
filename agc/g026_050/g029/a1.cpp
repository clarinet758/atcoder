#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    long long m=0ll,ans=0ll;
    char s[200009];
    scanf("%s",s);
    long h=strlen(s);
    bool w=0;
    for(long i=strlen(s)-1;i>=0l;i--) {
        if (s[i]=='W') m++;
        else ans+=m;
    }
    printf("%lld\n",ans);
    return 0;
}

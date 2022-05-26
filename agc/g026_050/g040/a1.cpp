#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define per(i,n)  for(int i=n-1;i>=0;--i)

char s[500009];
int  w[500009];

int main(){
    long long ans=0ll;
    scanf("%s",s);
    long l = strlen(s);
    rep(i,500009) w[i]=-1;

    for(long i=0l;i<l;i++) {
        if (i==0l && s[i]=='<') w[0]=0;
        if (i>0l && s[i-1]=='<' && s[i]=='>') w[i]=w[i-1]+1;
        if (i!=0l && s[i]=='<') w[i]=w[i-1]+1;
        if (i>0l && s[i-1]=='>' && s[i]=='<') w[i]=0;
        if (s[i]=='<' && i==l-1l) w[i+1]=w[i]+1;
    }
    for(int i=l-1l;i>=0;i--) {
        if (i==l-1l && s[i]=='>') w[i+1]=0;
        if (s[i]=='>') w[i]=max(w[i],w[i+1]+1);
    }

    //rep(i,25) cout<<w[i]<<endl;
    rep(i,500009) if (w[i]>0l) ans+=w[i]*1ll;
    printf("%lld\n",ans);
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)
#define sl1(a)  scanf("%lld",&a)
#define sl3(a,b,c)  scanf("%lld %lld %lld",&a,&b,&c)

int main(){
    int a,b,q;
    long long t,f=1000000000000005;
    sc3(a,b,q);
    vector<long long> kami(a);
    vector<long long> tera(b);
    rep(i,a) sl1(kami[i]);
    rep(i,b) sl1(tera[i]);
    rep(i,q) {
        sl1(t);
        long long kl = upper_bound(kami.begin(),kami.end(),t)-kami.begin();
        if (kl!=0) kl=t-kami[kl-1];
        else kl=f;

        long long tl = upper_bound(tera.begin(),tera.end(),t)-tera.begin();
        if (tl!=0) tl=t-tera[tl-1];
        else tl=f;

        long long kr = lower_bound(kami.begin(),kami.end(),t)-kami.begin();
        if (kr!=a) kr=kami[kr]-t;
        else kr=f;
        long long tr = lower_bound(tera.begin(),tera.end(),t)-tera.begin();
        if (tr!=b) tr=tera[tr]-t;
        else tr=f;

        long long ans=min(min(max(kl,tl),max(kr,tr)),min(min(kr,tl)*2+max(kr,tl),min(kl,tr)*2+max(kl,tr)));
        printf("%lld\n",ans);
    }
    return 0;
}

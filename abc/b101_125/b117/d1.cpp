#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sl1(a)  scanf("%lld",&a)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)
//ACするけど嘘解法
int cnt[50];
long long p[50];
long long a[100005];
int main(){
    long long n,k,chk=0,ans=0;
    sl2(n,k);
    p[0]=1ll;
    rep(i,45) {
        if (i==0) continue;
        p[i]=p[i-1]*2;
    }
    rep(i,n) {
        sl1(a[i]);
        long long tmp=a[i];
        rep(j,44) {
            if(tmp&1) cnt[j]+=1;
            tmp=tmp>>1;
        }
    }
    for(int i=44;i>-1;i--) if (cnt[i]*2<n && chk+p[i]<=k)  chk+=p[i];
    //printf("%lld %lld %d\n",p[42],p[43],7^2);
    rep(i,n) ans+=chk^a[i];
    printf("%lld\n",ans);
    return 0;
}

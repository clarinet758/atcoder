#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)
#define sl2(a,b)  scanf("%lld %lld",&a,&b)

long long a[55],p[55];

long long f (long long N,long long X) {
    if (N==0) {
        if (X<=0) return 0;
        else return 1;
    } else if (X<=1 + a[N-1]) {
        return f(N-1,X-1);
    } else {
        return p[N-1] + 1 + f(N-1,X-2-a[N-1]);
    }
    return 0ll;
}

int main(){
    long long n,x;
    sl2(n,x);
    a[0]=1,p[0]=1;
    rep(i,52) {
        a[i+1]=a[i]*2+3;
        p[i+1]=p[i]*2+1;
    }
    printf("%lld\n",f(n,x));
    return 0;
}

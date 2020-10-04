#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sl1(a)  scanf("%lld",&a)

int main(){
    long long n,a,b=1e15+5,c,ans=0ll;
    sl1(n);
    rep(i,5) {
        sl1(a);
        b=min(a,b);
    }
    c=n/b+(n%b>0?1:0);
    printf("%lld\n",5+c-1);
    return 0;
}

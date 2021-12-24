#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n;
    long long ans=0ll;
    sc1(n);
    rep(i,n+1) {
        if(i%3==0) true;
        else if(i%5==0) true;
        else ans+=i;
    }
    printf("%lld\n",ans);
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define sl2(a,b)  scanf("%lld %lld",&a,&b)

int main(){
    long long  n,m,ans=1;
    sl2(n,m);
    vector <long long > w;
    for (long long i=1;i*i<=m;i++) {
        if (m%i==0) {
            w.push_back(i);
            w.push_back(m/i);
        }
    }
    for(auto x:w)  if (n*x<=m) ans=max(ans,x); 
    printf("%lld\n",ans);
    return 0;
}

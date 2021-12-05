#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int mod=1000000007;
    int n,ans=0;
    sc1(n);
    vector<int> a(n),b(n),c(n-1);
    rep(i,n) sc1(a.at(i));
    rep(i,n) sc1(b.at(i));
    rep(i,n-1) sc1(c.at(i));
    rep(i,n) {
        ans+=b.at(a.at(i)-1);
        if (i>0 && a.at(i)-a.at(i-1)==1)  ans+=c.at(a.at(i-1)-1);
    }
    printf("%d\n",ans);
    return 0;
}
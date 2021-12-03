#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,ans=0;
    sc1(n);
    vector <int> d(n);
    rep (i,n) sc1(d.at(i));
    rep(i,n-1) for(int j=i+1;j<n;j++) {
        ans+=d.at(i)*d.at(j);
    }
    printf("%d\n",ans);
    return 0;
}

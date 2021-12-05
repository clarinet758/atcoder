#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int mod=1000000007;
    int n,a;
    sc1(n);
    vector <int> ans(n);
    rep(i,n){
        sc1(a);
        ans.at(a-1)=i+1;
    }
    rep(i,n) {
        if (i<n-1) printf("%d ",ans.at(i));
        else printf("%d\n",ans.at(i));
    }
    return 0;
}

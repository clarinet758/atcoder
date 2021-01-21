#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n,m=0,ans=0;
    sc1(n);
    rep(i,n){
        int p;
        sc1(p);
        ans+=p;
        m=max(m,p);
    }
    printf("%d\n",ans-(m/2));
    return 0;
}

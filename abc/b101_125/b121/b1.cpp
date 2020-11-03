#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int a,b[105];

int main(){
    int mod=1000000007;
    int n,m,c,t=0,ans=0;
    sc3(n,m,c);
    rep(i,m) sc1(b[i]);
    rep(i,n) {
        t=0;
        rep(j,m) {
            sc1(a);
            t+=a*b[j];
        }
        ans+=(t+c)>0;
        
    }
    printf("%d\n",ans);
    return 0;
}

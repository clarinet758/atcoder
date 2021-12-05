#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int b[25],a[25];
int main(){
    int n,m,c,ans=0;
    sc3(n,m,c);
    rep(i,m) sc1(b[i]);
    rep(i,n) {
        int x=c;
        rep(j,m) {
            sc1(a[j]);
            x+=a[j]*b[j];
        }
        ans+=(x>0);
    }
    printf("%d\n",ans);
    return 0;
}

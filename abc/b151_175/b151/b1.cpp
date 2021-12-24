#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc3(a,b,c)  scanf("%d %d %d",&a,&b,&c)

int main(){
    int a,n,k,m,s=0,ans=0;
    sc3(n,k,m);
    rep(i,n-1) {
        sc1(a);
        s+=a;
    }
    printf("%d\n",n*m-s-k>0?-1:max(0,n*m-s));
    return 0;
}

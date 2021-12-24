#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,m,a;
    sc2(n,m);
    rep(i,m) {
        sc1(a);
        n-=a;
    }
    printf("%d\n",max(n,-1));
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m,l;
    int p,q,r;
    int ans;
    scanf("%d %d %d",&n,&m,&l);
    scanf("%d %d %d",&p,&q,&r);
    ans=max((n/p)*(m/q),(m/p)*(n/q))*(l/r);
    ans=max(ans,max((n/p)*(l/q),(l/p)*(n/q))*(m/r));
    ans=max(ans,max((m/p)*(l/q),(l/p)*(m/q))*(n/r));
    printf("%d\n",ans);
    return 0;
}

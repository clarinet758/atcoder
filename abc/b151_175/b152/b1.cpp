#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b,ans=0;
    sc2(a,b);
    rep(i,max(a,b)) ans=ans*10+min(a,b);
    printf("%d\n",ans);
    return 0;
}

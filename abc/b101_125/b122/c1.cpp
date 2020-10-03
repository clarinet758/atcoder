#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int w[100005];
char s[100005];

int main(){
    int a,b,n,q,x;
    sc2(n,q);
    scanf("%s",s);
    for (int i=1;i<n;i++)  w[i]=w[i-1]+((s[i-1]=='A' && s[i]=='C')-0) ;

    rep(i,q) {
        sc2(a,b);
        printf("%d\n",w[b-1]-w[a-1]);
    }
    return 0;
}

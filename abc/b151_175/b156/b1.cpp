#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int n,k,t=1;
    sc2(n,k);
    rep(i,100) {
        t*=k;
        if (n<t) {
            printf("%d\n",i+1);
            break;
        }
    }
    return 0;
}

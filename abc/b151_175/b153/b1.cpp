#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int h,n,a;
    sc2(h,n);
    rep(i,n) {
        sc1(a);
        h-=a;
    }
    printf("%s\n",h<=0?"Yes":"No");
    return 0;
}

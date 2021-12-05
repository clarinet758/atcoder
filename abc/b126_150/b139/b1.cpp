#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc2(a,b)  scanf("%d %d",&a,&b)

int main(){
    int a,b,c;
    sc2(a,b);
    c=1;
    rep(i,100) {
        if (c>=b) {
            printf("%d\n",i);
            break;
        }
        c+=(a-1);
    }
    return 0;
}

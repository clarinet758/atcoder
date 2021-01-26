#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n;
    sc1(n);
    int x=n*100/108;
    rep(i,2) {
        if (n==(x+i)*108/100) {
            printf("%d\n",x+i) ;
            return 0;
        }
    }
    printf(":(\n");
    return 0;
}

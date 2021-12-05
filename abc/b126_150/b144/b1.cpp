#include<bits/stdc++.h>
using namespace std;

#define rep(i,n)  for(int i=0;i<n;++i)
#define sc1(a)  scanf("%d",&a)

int main(){
    int n;
    sc1(n);
    rep(i,9) rep(j,9) {
        if ((i+1)*(j+1)==n) {
            printf("Yes\n");
            return 0;
        }
    }
    printf("No\n");
    return 0;
}
